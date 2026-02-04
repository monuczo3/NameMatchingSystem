from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import os
from sentence_transformers import SentenceTransformer
from dataset import names_dataset
load_dotenv()

index_name = os.getenv("PINECONE_INDEX_NAME")

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def initialize_pinecone():

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

    # Check if index exists, if not create it
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=384,
            metric="cosine",
            spec=ServerlessSpec(
                cloud='aws',
                region='us-east-1'
            )
        )

    index = pc.Index(index_name)
    return index


def store_names_in_pinecone(index, names):
    """Generate embeddings and store names in Pinecone"""
    vectors = []

    for idx, name in enumerate(names):
        # Generate embedding
        embedding = model.encode(name.lower()).tolist()

        # Prepare vector with metadata
        vectors.append({
            "id": f"name_{idx}",
            "values": embedding,
            "metadata": {"name": name}
        })

    # Upsert to Pinecone in batches
    index.upsert(vectors=vectors)
    print(f"Successfully stored {len(names)} names in Pinecone")

if __name__ == "__main__":
    index = initialize_pinecone()
    store_names_in_pinecone(index,names_dataset)
