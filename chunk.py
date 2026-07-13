from dataclasses import dataclass

@dataclass
class ChunkData:
    chunk_id : str
    document_name : str
    page_numbers : list[int]
    chunk_index : int
    text : str
    
    @property
    def text_length(self) -> int:
        return len(self.text)