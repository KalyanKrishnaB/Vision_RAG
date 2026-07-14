from page import PageData
from tokenizer import Tokenizer

class DocumentBuffer:
    def __init__(self, max_tokens:int = 512):
        self.tokenizer = Tokenizer()
        self.max_tokens = max_tokens
        self.pages = []
        
    def add_page(self, page:PageData):
        self.pages.append(page)
        
    def clear(self):
        self.pages.clear()
        
    @property
    def text(self):
        return "\n".join(page.text for page in self.pages)
    
    @property
    def page_numbers(self):
        return [page.page_number for page in self.pages]
    
    @property
    def token_count(self):
        return self.tokenizer.count_tokens(self.text)
    
    @property
    def is_full(self):
        return self.token_count >= self.max_tokens