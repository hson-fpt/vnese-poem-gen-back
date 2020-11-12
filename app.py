import sys
import torch
from transformers import AutoModel, AutoTokenizer
from transformers import pipeline

def get_poem(text: str) -> str:
    custokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
    custokenizer.add_tokens('\n')

    make_poem = pipeline('text-generation', model="./gpt2", tokenizer=custokenizer, device=0)
    poem = make_poem('<s>' + text)
    final_res = (poem[0]['generated_text'][3:])
    print(final_res)
    return final_res

if __name__ == "__main__":
    sentence = ' '.join(sys.argv[1:])
    print("\n".join(str(get_poem(sentence)).split("\n")[:4]))