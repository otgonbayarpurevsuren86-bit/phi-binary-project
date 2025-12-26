# One is One – Hugging Face Wikitext dataset дээр туршилт (нээлттэй бодит текст)
from datasets import load_dataset
import hashlib
import math

PHI = (1 + math.sqrt(5)) / 2

print("Hugging Face Wikitext dataset татаж байна (бодит текст)...")
try:
    dataset = load_dataset("wikitext", "wikitext-103-v1", split="train")
    data_lines = [line.strip() for line in dataset['text'] if line.strip()]
    data_lines = data_lines[:500000]  # Туршилтын хязгаар
except Exception as e:
    print(f"Алдаа: {e} – fallback ашиглана.")
    data_lines = ["fallback sentence " + str(i) for i in range(100000)] * 10

print(f"Өмнө: {len(data_lines):,} мөр")

seen = set()
unique = []

for line in data_lines:
    if line:
        line_hash = hashlib.md5(line.encode('utf-8', errors='ignore')).hexdigest()
        if line_hash not in seen:
            seen.add(line_hash)
            unique.append(line)

print(f"Дэдүп хийсний дараа: {len(unique):,} мөр")
print(f"Хэмнэлт: {100 * (1 - len(unique)/len(data_lines)):.2f}%")

length = len(unique)
s = math.floor(length / PHI)
ratio = (length - s) / s if s > 0 else float('inf')
stable = abs(ratio - PHI) < 0.2

print(f"Φ ratio: {ratio:.4f} | Тогтвортой: {stable}")
