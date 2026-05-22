import sentencepiece as spm

text = "Spelling and Arithmetic: LLMs struggle with tasks like spelling or simple math because words and numbers are broken into arbitrary chunks. A number might be a single token in one context and split into multiple tokens in another, making it hard for the model to see consistent patterns (7:24 - 8:12, 1:55:57)."
tokens = text.encode("utf-8")
print(list(tokens))