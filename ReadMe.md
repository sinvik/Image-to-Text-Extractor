# Image-to-Text Extractor

## Overview
Image-to-Text Extractor is a Python-based project that leverages Tesseract OCR for extracting text from images and PDF files. The extracted data is processed with pandas and can be exported to Excel or CSV for further analysis.

## Features
- Extract text from images in formats like PNG, JPEG, and TIFF.
- OCR support for scanned PDF documents.
- Process and clean extracted text using Python and pandas.
- Export processed data to Excel or CSV formats for structured storage.

## Tools and Technologies
- **Python**: Core language for scripting and data processing.
- **Tesseract OCR**: Optical Character Recognition engine for text extraction.
- **pandas**: For data manipulation and analysis.
- **Excel**: For structured data export.
- **PDF**: Support for PDF-based text extraction.

## Prerequisites
- Python 3.7 or higher
- Tesseract OCR (Install from [here](https://github.com/tesseract-ocr/tesseract))
- Required Python libraries:
  - `pandas`
  - `pytesseract`
  - `pdf2image`
  - `openpyxl`

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd image-to-text-extractor
