from pdf_reader import extract_pages
from chunker import DocumentBuffer

PDF_PATH = "sample.pdf"

def inspect_pdf(pdf_path:str):
    print("="*70)
    print("pdf inspector")
    print("="*70)
    
    for page in extract_pages(pdf_path):

        print("-" * 70)
        print(f"Page {page.page_number}")
        print(f"Has Text : {page.has_text}")
        print(f"Images   : {page.image_count}")
        print(f"Length   : {page.text_length}")

        if page.has_text:
            print(page.text[:200].replace("\n", " "))


if __name__ == "__main__":
    inspect_pdf(PDF_PATH)