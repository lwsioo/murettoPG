import csv, json, sys

keep_pos = {"NOUN","ADJ","ADV","VER"}
lemmas = set()

with open("morph-it_048.txt", encoding="latin-1") as f:  # leggi Morph-it! in latin-1
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) < 3:
            continue
        lemma = parts[1].lower()
        tag = parts[2].split(":")[0]
        if tag in keep_pos:
            lemmas.add(lemma)

for aux in ["essere","avere"]:
    lemmas.discard(aux)

# Scrive il JSON in UTF-8
with open("lemmi.json", "w", encoding="utf-8") as out:
    json.dump(sorted(lemmas), out, ensure_ascii=False)
