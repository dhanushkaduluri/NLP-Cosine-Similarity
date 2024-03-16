import random
from sklearn.metrics.pairwise import cosine_similarity
import torch
import pandas as pd

file_path=r"AI interview sample dataset.xlsx"

df=pd.read_excel(file_path)

terms_dict=pd.Series(df.Definition.values, index=df.Term).to_dict()

for index, value in terms_dict.items():
    print(f"Term: {index}, Value:{value}")

# Load model and tokenizer
model_name='bert-base-nli-mean-tokens'
model= SentenceTransformer(model_name)

# Function to encode text to vector using SentenceTransformer
def encode(text):
    return model.encode(text, convert_to_tensor=True)

random.seed(42)

random_term=random.choice(list(terms_dict.keys()))
answer=terms_dict[random_term]
print(f"Please describe: {random_term}")
user_input=input("Your Answer: ")

# Encoding
answer_vector=encode(answer).unsqueeze(0) # Reshape to 2D array
user_input_vector=encode(user_input).unsqueeze(0) # Reshape to 2D array

# Cosine Similarity
similarity = cosine_similarity(answer_vector,user_input_vector)

print(f"Answer: {answer}")
print(f"Cosine Similarity: {similarity[0][0]}")