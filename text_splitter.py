from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter():
    return RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        model_name="gpt-4o",
        chunk_size = 1024,
        chunk_overlap = 256,
        
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            "",
        ],
        
    )