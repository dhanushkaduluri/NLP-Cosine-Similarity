# NLP-Cosine-Similarity
Text comparison  
# Description
- This script reads a dataset from an Excel file, where each row represents a term and its corresponding definition. It then randomly selects a term from the dataset and prompts the user to provide their own description of that term.

- The script uses a pre-trained BERT model (bert-base-nli-mean-tokens) to encode both the user's input and the actual definition of the term into numerical vectors. These vectors are then compared using cosine similarity to determine how similar the user's input is to the actual definition.

- Finally, it prints out the actual definition of the term, the cosine similarity score between the user's input and the actual definition, and the random term for which the user was prompted.

- This script essentially simulates a system where a user can input their understanding of a term, and the script evaluates how closely it aligns with the provided definition in the dataset.
# Author
@dhanushkaduluri
