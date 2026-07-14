from vector_store import VectorStore


class SemanticSearchEngine:

    def __init__(self):

        self.vector_store = VectorStore()

    def search(self, query, k=5):

        return self.vector_store.search(
            query=query,
            k=k,
        )