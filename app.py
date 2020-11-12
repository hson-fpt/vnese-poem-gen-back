import sys
import torch
from transformers import AutoModel, AutoTokenizer
from transformers import pipeline

def get_poem(text: str) -> str:
    custokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
    custokenizer.add_tokens('\n')

    make_poem = pipeline('text-generation', model="./gpt2", tokenizer=custokenizer, device=0)
    poem = make_poem('<s>' + text)
    return "\n".join(str(poem[0]['generated_text'][3:]).split("\n")[:4])

if __name__ == "__main__":
    sentence = ' '.join(sys.argv[1:])
    print(get_poem(sentence))