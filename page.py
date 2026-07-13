from dataclasses import dataclass

@dataclass
class PageData:
    page_number: int
    text : str
    image_count : int
    width : float
    height : float
    rotation : int
    
    @property
    def has_text(self) -> bool:
        return bool(self.text.strip())
    
    @property
    def text_length(self) -> int:
        return len(self.text)
    