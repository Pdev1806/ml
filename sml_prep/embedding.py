from tokenizers import Tokenizer
import torch
import torch.nn as nn

# load tokenizer
tokenizer = Tokenizer.from_file(
    "my_tokenizer.json"
)

# tokenize text
encoded = tokenizer.encode(
    "Transformers are amazing"
)

token_ids = encoded.ids

print("TOKEN IDS:")
print(token_ids)

# convert to tensor
tokens = torch.tensor(token_ids)

# embedding layer
embedding = nn.Embedding(
    num_embeddings=100,
    embedding_dim=8
)

# get vectors
vectors = embedding(tokens)

print("\nEMBEDDINGS:")

print("\nSHAPE:")
print(vectors.shape)