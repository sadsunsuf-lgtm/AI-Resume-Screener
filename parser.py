from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extracts all text from a given PDF file path."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {e}"

# This part is for testing the script by itself
if __name__ == "__main__":
    # You will need to put a sample PDF in your folder to test this!
    print("PDF Parser logic is ready.")