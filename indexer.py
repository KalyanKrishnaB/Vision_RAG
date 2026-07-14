from pathlib import Path

from pdf_reader import extract_pages
from text_splitter import get_text_splitter
from tokenizer import Tokenizer

class DocumentIndexer:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.splitter = get_text_splitter()
        self.tokenizer = Tokenizer()
        
    def index_pdf(self,pdf_path: str):
        document_name = Path(pdf_path).stem
        chunk_counter = 0
        for page in extract_pages(pdf_path):
            chunks = self.splitter.split_documents([page])
            for index,chunk in enumerate(chunks):
                chunk_counter += 1
                chunk.metadata.update({
                    "document_name": document_name,
                    "chunk_index" : chunk_counter,
                    "chunk_id" : f"{document_name}_p{page.metadata['page']}_c{index}",
                    "token_count" : self.tokenizer.count_tokens(chunk.page_content)
                })
                
            self.vector_store.add_documents(chunks)
