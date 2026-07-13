import tiktoken

class Tokenizer:
    def __init__(self, model_name: str = "gpt-4o"):
        self.encoding = tiktoken.encoding_for_model(model_name)
        
    def count_tokens(self, text:str) -> int:
        return len(self.encoding.encode(text))
    
    def encode(self, text:str) -> list[int]:
        return self.encoding.encode(text)
    
    def decode(self, tokens:list[int]) -> str:
        return self.encoding.decode(tokens)