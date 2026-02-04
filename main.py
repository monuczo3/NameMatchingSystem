from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
load_dotenv()
from pinecone_db import initialize_pinecone

index = initialize_pinecone()

# Initialize embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


def find_similar_names(input_name, top_k):
    """Find most similar names from Pinecone db

    Args:input_name: User's input name
        top_k: Number of similar names to return

    Returns: Dictionary with best match and list of all matches
    """
    # Generate embedding of input name
    query_embedding = model.encode(input_name.lower()).tolist()

    # Search in Pinecone
    results = index.query(
        vector=query_embedding,
        top_k=top_k,
        include_metadata=True
    )

    # Process results
    matches = []
    for match in results['matches']:
        similarity_score = round(match['score'] * 100, 2)  # Convert to percentage
        matches.append({
            "name": match['metadata']['name'],
            "score": similarity_score
        })

    #Output
    output = {
        "input_name": input_name,
        "best_match": matches[0] if matches else None,
        "all_matches": matches
    }

    return output


def display_results(results):
    """Display matching results"""
    print(f"\n{'=' * 50}")
    print(f"Input Name: {results['input_name']}")
    print(f"{'=' * 50}\n")

    if results['best_match']:
        print("BEST MATCH:")
        print(f"   Name: {results['best_match']['name']}")
        print(f"   Similarity Score: {results['best_match']['score']}%\n")

        print("ALL MATCHES:")
        print(f"{'Rank':<6} {'Name':<15} {'Score'}")
        print("-" * 35)

        for idx, match in enumerate(results['all_matches'], 1):
            print(f"{idx:<6} {match['name']:<15} {match['score']}%")
    else:
        print("No matches found.")

    print(f"\n{'=' * 50}\n")


def main():

    print("Welcome to Name Matching System!")
    print("-" * 50)

    while True:
        user_input = input("\nEnter a name to find matches (or 'quit' to exit): ").strip()

        if user_input.lower() == 'quit':
            print("Thank you for using Name Matching System!")
            break

        if not user_input:
            print("Enter a valid name.")
            continue

        # Find similar names
        results = find_similar_names(user_input, top_k=5)

        # Display results
        display_results(results)


if __name__ == "__main__":
    main()


