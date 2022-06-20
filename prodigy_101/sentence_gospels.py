import json
import spacy

"""A quick Python script to segment sentences

1. Segment sentences using a spaCy pipeline
2. Save output into jsonl format for Prodigy
"""

# Load a small English language model to help us segment sentences
nlp = spacy.load("en_core_web_sm")

with open('./gospels.txt') as f:
    gospels = f.readlines()

# Load each gospel into spaCy efficiently
docs = nlp.pipe(gospels)

# Loop over gospels and sentences, and write them as jsonl
doc_num = 1
with open('./gospels.jsonl', 'w') as out_f:
    for doc in docs:
        for index, sentence in enumerate(doc.sents):
            if sentence.text == "\n":  # Skip empty lines
                continue
            line_dict = {"ID":f"{doc_num}.{index}", "text":sentence.text}
            print(line_dict)
            json.dump(line_dict, out_f, ensure_ascii=False)
            out_f.write('\n')
        doc_num +=1