from pdf_reader import extract_pages
from text_splitter import get_text_splitter
from embeddings import EmbeddingModel

splitter = get_text_splitter()
model = EmbeddingModel()

for document in extract_pages("sample.pdf"):

    chunks = splitter.split_documents([document])
    
    print(f"\npage {document.metadata['page_number']} has {len(chunks)} chunks:")
    
    for index, chunk in enumerate(chunks, start= 1):
        print("-"*40)
        print(f"chunk {index +1}: {chunk.page_content[:250]}... (length: {len(chunk.page_content)})")
        print(model.encode(chunk.page_content))