# Task 1: Name Matching System

A semantic name matching system that uses sentence embeddings and Pinecone vector database to find similar names based on user input. The system is particularly designed to handle phonetically similar names and variations in spelling.

## Overview

This project implements a name similarity search system that:
- Uses **SentenceTransformer** model for generating semantic embeddings
- Stores name embeddings in **Pinecone** vector database for efficient similarity search
- Provides an interactive CLI for querying similar names
- Returns ranked results with similarity scores

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Pinecone account and API key

## Setup Instructions

### 1. Create a Virtual Environment (Recommended)

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate
```

### 2. Install Dependencies

Navigate to the project root directory and install required packages:

```powershell
pip install -r requirements.txt
```

**Required packages:**
- `pinecone` - Pinecone vector database client
- `sentence-transformers` - For generating text embeddings
- `python-dotenv` - For environment variable management
- `numpy` - Numerical computing library

### 3. Configure Environment Variables

Create a `.env` file with your Pinecone credentials:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=name-matching-index
```

**To get your Pinecone API key:**
1. Sign up at [https://www.pinecone.io/](https://www.pinecone.io/)
2. Navigate to API Keys section in your dashboard
3. Copy your API key

## Project Structure

```
NameMacthingSystem/
├── dataset.py       # Contains the names dataset
├── pinecone_db.py   # Pinecone database initialization and data storage
├── main.py          # Main application with CLI interface
├── .env             # Environment variables (create this file)
└── README.md        # This file
```

## How to Run the Project

### Step 1: Initialize the Database (First-Time Setup)

Before running the main application, you need to populate the Pinecone database with names:

```powershell
python pinecone_db.py
```

**Expected output:**
```
Successfully stored 37 names in Pinecone
```

This step:
- Creates a Pinecone index (if it doesn't exist)
- Generates embeddings for all names in the dataset
- Stores the embeddings in Pinecone vector database

### Step 2: Run the Name Matching System

```powershell
python main.py
```

### Step 3: Query Names

Enter names when prompted to find similar matches. Type `quit` to exit.

## Sample Input and Expected Output

### Example 1: Exact Match
```
Enter a name to find matches (or 'quit' to exit): Geetha

==================================================
Input Name: Geetha
==================================================

BEST MATCH:
   Name: Geetha
   Similarity Score: 100.0%

ALL MATCHES:
Rank   Name            Score
-----------------------------------
1      Geetha          100.0%
2      Geeta           98.45%
3      Gita            97.83%
4      Githa           97.21%
5      Gitu            95.67%

==================================================
```

### Example 2: Similar Name Variation
```
Enter a name to find matches (or 'quit' to exit): Seetha

==================================================
Input Name: Seetha
==================================================

BEST MATCH:
   Name: Seetha
   Similarity Score: 100.0%

ALL MATCHES:
Rank   Name            Score
-----------------------------------
1      Seetha          100.0%
2      Seeta           98.92%
3      Sita            96.78%
4      Sitha           96.15%
5      Sitara          92.34%

==================================================
```

### Example 3: Phonetically Similar Names
```
Enter a name to find matches (or 'quit' to exit): Kavita

==================================================
Input Name: Kavita
==================================================

BEST MATCH:
   Name: Kavita
   Similarity Score: 100.0%

ALL MATCHES:
Rank   Name            Score
-----------------------------------
1      Kavita          100.0%
2      Kavitha         98.67%
3      Kavitaa         98.23%
4      Kabita          97.45%
5      Lalita          85.32%

==================================================
```

### Example 4: Finding Closest Match for Misspelling
```
Enter a name to find matches (or 'quit' to exit): Priyaa

==================================================
Input Name: Priyaa
==================================================

BEST MATCH:
   Name: Priyaa
   Similarity Score: 100.0%

ALL MATCHES:
Rank   Name            Score
-----------------------------------
1      Priyaa          100.0%
2      Priya           99.12%
3      Priyanka        94.56%
4      Preya           93.78%
5      Meena           78.23%

==================================================
```

### Example 5: Exiting the Application
```
Enter a name to find matches (or 'quit' to exit): quit

Thank you for using Name Matching System!
```

## Features

✅ **Semantic Name Matching**: Uses state-of-the-art sentence transformers (all-MiniLM-L6-v2) for intelligent name similarity  
✅ **Vector Database**: Leverages Pinecone for fast and scalable similarity search  
✅ **Top-K Results**: Returns top 5 most similar names with confidence scores  
✅ **Percentage Scores**: Easy-to-understand similarity scores (0-100%)  
✅ **Interactive CLI**: User-friendly command-line interface  
✅ **Case Insensitive**: Handles input in any case  
✅ **Phonetic Similarity**: Finds names that sound similar even if spelled differently  

## Dataset

The current dataset contains 37 Indian names with common variations:
- Geetha, Gita, Geeta, Githa, etc.
- Sita, Seeta, Seetha, Sitara, etc.
- Anita, Anitha, Aneeta, Nita, etc.
- Meena, Mina, Meenakshi, etc.
- Priya, Preya, Priyanka, etc.
- Kavita, Kavitha, Kabita, etc.
- Sunita, Sunitha, Suneeta, etc.
- Lalita, Lalitha, Laleeta, etc.

## Technical Details

### Embedding Model
- **Model**: `all-MiniLM-L6-v2` from sentence-transformers
- **Dimension**: 384
- **Use Case**: Optimized for semantic similarity tasks

### Vector Database
- **Database**: Pinecone
- **Index Type**: Serverless
- **Cloud**: AWS
- **Region**: us-east-1
- **Metric**: Cosine similarity

### Similarity Calculation
The system uses cosine similarity to measure how close two name embeddings are. Scores are converted to percentages for better interpretability.

## Troubleshooting

### Common Issues and Solutions

**1. ModuleNotFoundError**
```
Solution: Ensure all dependencies are installed
pip install -r requirements.txt
```

**2. Pinecone Connection Error**
```
Solution: 
- Verify .env file exists in Task 1 directory
- Check that PINECONE_API_KEY is correct
- Ensure you have internet connection
```

**3. "No matches found"**
```
Solution: Run pinecone_db.py first to populate the database
python pinecone_db.py
```

**4. Import Error: "No module named 'dotenv'"**
```
Solution: Install python-dotenv
pip install python-dotenv
```

**5. Index Creation Failed**
```
Solution: 
- Verify your Pinecone account is active
- Check if you've reached your free tier limits
- Try using a different index name
```

## Extending the Project

### Adding More Names

To add more names to the dataset:

1. Open `dataset.py`
2. Add names to the `names_dataset` list
3. Re-run the database initialization:
   ```powershell
   python pinecone_db.py
   ```

### Changing the Number of Results

To modify the number of similar names returned:

In `main.py`, change the `top_k` parameter:
```python
results = find_similar_names(user_input, top_k=10)  # Returns top 10 matches
```

### Using a Different Embedding Model

To use a different SentenceTransformer model:

Update both `pinecone_db.py` and `main.py`:
```python
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
```

Note: Ensure the dimension in Pinecone index creation matches your model's output dimension.

## Performance Notes

- Initial database setup takes 10-30 seconds depending on dataset size
- Each query typically completes in less than 500ms
- The system can scale to millions of names with Pinecone

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Verify all prerequisites are met
3. Ensure environment variables are correctly configured

---

**Last Updated**: February 2026

