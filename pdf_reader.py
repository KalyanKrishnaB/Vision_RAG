import fitz

from page import PageData


def extract_pages(pdf_path: str):
    """
    Generator that yields one PageData object at a time.
    """

    document = fitz.open(pdf_path)

    try:
        for page_number in range(document.page_count):

            page = document.load_page(page_number)

            yield PageData(
                page_number=page_number + 1,
                text=page.get_text().strip(),
                image_count=len(page.get_images(full=True)),
                width=page.rect.width,
                height=page.rect.height,
                rotation=page.rotation,
            )

    finally:
        document.close()