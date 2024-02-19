from pinecone import Pinecone, ServerlessSpec
from app.services.openai_service import get_embedding
import os

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
pinecone = Pinecone(api_key=PINECONE_API_KEY, environment='MyLLMTest')
EMBEDDING_DIMENSION = 1536

def embed_chunks_and_upload_to_pinecone(chunks, index_name):
    if index_name in pinecone.list_indexes().names():
        print("\nIndex already exists. Deleting index ...")
        pinecone.delete_index(name=index_name)
    
    print("\nCreating a new index: ", index_name)
    pinecone.create_index(name=index_name,
                          dimension=EMBEDDING_DIMENSION, metric='cosine',
                          spec=ServerlessSpec(
                            cloud="aws",
                            region="us-west-2")
    )

    index = pinecone.Index(index_name)

    # Embedding each chunk and preparing for upload
    print("\nEmbedding chunks using OpenAI ...")
    embeddings_with_ids = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        embeddings_with_ids.append((str(i), embedding, chunk))

    print("\nUploading chunks to Pinecone ...")
    upserts = [(id, vec, {"chunk_text": text}) for id, vec, text in embeddings_with_ids]
    index.upsert(vectors=upserts)

    print(f"\nUploaded {len(chunks)} chunks to Pinecone index\n'{index_name}'.")


def get_most_similar_chunks_for_query(query, index_name):
    print("\nEmbedding query using OpenAI ...")
    question_embedding = get_embedding(query)

    print("\nQuerying Pinecone index ...")
    index = pinecone.Index(index_name)
    query_results = index.query(vector=question_embedding, top_k=3, include_metadata=True)
    context_chunks = [x['metadata']['chunk_text'] for x in query_results['matches']]

    return context_chunks   


def delete_index(index_name):
  if index_name in pinecone.list_indexes():
    print("\nDeleting index ...")
    pinecone.delete_index(name=index_name)
    print(f"Index {index_name} deleted successfully")
  else:
     print("\nNo index to delete!")