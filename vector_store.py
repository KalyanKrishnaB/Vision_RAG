import chromadb
from embeddings import EmbeddingModel

class VectorStore:

    def __init__(
        self,
        collection_name: str = "documents",
    ):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )
        
        self.embedding_model = EmbeddingModel()
        
    def add_documents(self, documents):

        ids = []
        embeddings = []
        metadatas = []
        texts = []

        for index, doc in enumerate(documents):

            ids.append(doc.metadata["chunk_id"])

            texts.append(doc.page_content)

            metadatas.append(doc.metadata)

            embeddings.append(
                self.embedding_model.encode(
                    doc.page_content
                ).tolist()
            )

        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
        )   
        
    def search(
        self,
        query: str,
        k: int = 5,
    ):

        query_embedding = self.embedding_model.encode(query).tolist()

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=k,
        )

        return results
            