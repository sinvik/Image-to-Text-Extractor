from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import re


def curr_time_stamp():
    from datetime import datetime

    # Get the current date and time
    current_time = datetime.now()

    # Format the date and time
    formatted_time = current_time.strftime("%d:%m:%Y %H:%M:%S")

    # Print the result
    print(formatted_time)


def dump_dict_to_sheet(file, sheet, data):
    import pandas as pd
    from pandas import DataFrame

    if isinstance(data, dict):
        data = DataFrame.from_dict(data)

    with pd.ExcelWriter(file, engine='openpyxl') as writer:
        data.to_excel(writer, sheet_name=sheet)


def extract_upper(input_text):
    words = input_text.split()
    result = []
    for word in words:
        if word.isupper():
            result.append(word)
    return result


def extract_text(input_text):
    try:
        start_text = "individual person (see instructions)"
        end_text = "CAUTION Do not individually list"
        splitter = "2a Name of Participating"

        start = input_text.find(start_text) + len(start_text)
        end = input_text.find(end_text)
        first_clean = input_text[start:end].split(splitter)
        pattern = r'\n([A-Z ]+)\n(\d{2}-\d{7}) ([0-9]*\.?[0-9]+) (\d+)'
        extract_data = []
        for _text in first_clean:
            # Find all matches
            matches = re.findall(pattern, _text)

            # Process and print results
            for match in matches:
                extract_data.append(match)
        return extract_data

    except ValueError:
        return "Start or end text not found!"


def extract_title(input_text, start, end):
    try:
        start_index = input_text.index(start) + len(start)
        end_index = input_text.index(end, start_index)
        return input_text[start_index:end_index].strip()
    except ValueError:
        return "Start or end text not found!"


if __name__ == "__main__":
    # Set the Tesseract executable path
    print("Start Time: ", end=' ')
    curr_time_stamp()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Path to the PDF
    pdf_path = r"D:\projects\use_cases\Image-to-Text Extractor\resource\CREDIT UNIONS - Sample Multiple Employer Plan.pdf"
    poppler_path = r"D:\projects\tools\Release-24.07.0-0\poppler-24.07.0\Library\bin"

    # Convert PDF to images
    images = convert_from_path(pdf_path, poppler_path=poppler_path)

    extract = {
        "PLAN_NAME": [],
        "NAME_OF_EMPLOYER": [],
        "EIN": [],
        "CONTRIBUTION IN %": [],
        "AGG_ACC_BAL": []
    }

    # Initialize an empty string to hold the extracted text
    extracted_text = ""
    title_page = 1

    # Extract Plan Name
    text = pytesseract.image_to_string(images[0], lang="eng")
    start_text = "1a Name of plan"
    end_text = "1b Three-digit plan"

    plan_name = extract_title(text, start_text, end_text)

    content_pages = range(25, 37 + 1)
    # Process each page

    for page_number, image in enumerate(images, start=1):
        if page_number in content_pages:
            print(f"Processing page {page_number}...")
            try:
                # Perform OCR on the image
                page_content = pytesseract.image_to_string(image, lang="eng")

                employer_info = extract_text(page_content)
                for _employer in employer_info:
                    if len(_employer) == 4:
                        extract["PLAN_NAME"].append(plan_name)
                        extract["NAME_OF_EMPLOYER"].append(_employer[0])
                        extract["EIN"].append(_employer[1])
                        extract["CONTRIBUTION IN %"].append(_employer[2])
                        extract["AGG_ACC_BAL"].append(_employer[3])
                    else:
                        print(f"ERROR: Page {page_number} have some issues!! skipping for now!")
                        break
            except:
                print(f"ERROR: Unhandled error on page number {page_number}! skipping for now!")
                continue

    dump_dict_to_sheet("output.xlsx", "output", extract)
    print("End Time: ", end=' ')
    curr_time_stamp()
