from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace

# create tokenizer using BPE algorithm
tokenizer = Tokenizer(BPE())

# split words by spaces first
tokenizer.pre_tokenizer = Whitespace()

# settings for training
trainer = BpeTrainer(

    # maximum vocabulary size
    vocab_size=100,

    # special tokens used in NLP models
    special_tokens=[
        "[PAD]",
        "[UNK]",
        "[CLS]",
        "[SEP]",
        "[MASK]"
    ]
)

# train tokenizer using text file
tokenizer.train(
    ["data.txt"],
    trainer
)

# save tokenizer to file
tokenizer.save("my_tokenizer.json")

print("Tokenizer trained!")

# test tokenizer on sample sentence
output = tokenizer.encode(
    "Transformers use tokenization"
)

# print learned tokens
print("\nTOKENS:")
print(output.tokens)

# print token IDs
print("\nTOKEN IDS:")
print(output.ids)