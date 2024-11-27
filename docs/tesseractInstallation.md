# Installation and Troubleshooting Guide for Tesseract OCR

## Installation Guide for Tesseract OCR

1. **Download and Install Tesseract**
   - Visit the [official Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract).
   - Download the appropriate version for your operating system.
   - Install Tesseract. By default, it is installed at `C:\Program Files\Tesseract-OCR`.

2. **Verify the Path to Tesseract**
   - Ensure that Tesseract is installed correctly by verifying its path in your Python script:
     ```python
     import pytesseract

     # Path to Tesseract executable
     pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"

     # Use Tesseract on an image
     text = pytesseract.image_to_string(image, lang="eng")
     print(text)
     ```
   - Replace `C:\Tesseract-OCR\tesseract.exe` with the actual location of Tesseract on your system.

3. **Add Tesseract to PATH (Optional)**
   - To use Tesseract commands directly in the terminal:
     1. Press `Win + S` and type **Environment Variables**.
     2. Select **Edit the system environment variables**.
     3. Click **Environment Variables**.
     4. Under **System Variables**, select **Path** and click **Edit**.
     5. Add the directory containing `tesseract.exe` (e.g., `C:\Tesseract-OCR`).
     6. Restart your terminal or IDE.

---

## Troubleshooting Guide for Tesseract

### 1. Verify the Path to `tesseract.exe`
   - Ensure your script points to the correct path for `tesseract.exe`. Update as necessary:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
     ```

### 2. Avoid Running with Admin Privileges
   - **Reinstall Tesseract in a Non-Restricted Directory**:
     - Uninstall Tesseract from `C:\Program Files`.
     - Reinstall it in a simpler location, such as `C:\Tesseract-OCR`.
     - Update your script with the new path.

### 3. Run Command Prompt as Administrator (if required)
   - Right-click on your terminal (e.g., Command Prompt or PowerShell).
   - Select **Run as Administrator**.
   - Re-run your Python script.

### 4. Debug Tesseract Execution
   - Test if Tesseract is working manually:
     1. Open Command Prompt as Administrator.
     2. Check the version:
        ```bash
        tesseract --version
        ```
     3. Test with an image:
        ```bash
        tesseract example_image.png output -l eng
        ```
     - This generates `output.txt` containing the extracted text.

### 5. Disable UAC Restrictions (Last Resort)
   - If permissions still block Tesseract:
     1. Press `Win + S` and type **UAC**.
     2. Select **Change User Account Control settings**.
     3. Lower the slider to **Never Notify**.
     4. Restart your computer.
   - **Warning**: Disabling UAC exposes your system to potential security risks. Proceed only if absolutely necessary.

---

### Additional Note
- If any issues persist, consult the [Tesseract GitHub Issues page](https://github.com/tesseract-ocr/tesseract/issues) for solutions or further assistance.
