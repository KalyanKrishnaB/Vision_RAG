from page import PageData

class DocumentBuffer:
    def __init__(self):
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
    def text_length(self):
        return len(self.text)