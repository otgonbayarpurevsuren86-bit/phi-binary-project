# One is One Principle – Deduplication for efficient learning
# Phi-Binary Research Initiative – 2025

def deduplicate_data(data_list):
    """
    Давтагдсан мэдээллийг арилгаж, нэг л удаа үлдээх.
    Жишээ: [1, 2, 1, 3, 2] → [1, 2, 3]
    """
    seen = set()
    unique = []
    for item in data_list:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique

def phi_stability_check(data):
    """
    Phi-Binary overlay – мэдээлэл авалтын дараа тэнцвэр шалгах
    """
    import math
    PHI = (1 + math.sqrt(5)) / 2
    length = len(data)
    s = math.floor(length / PHI)
    ratio = (length - s) / s if s > 0 else float('inf')
    return ratio, abs(ratio - PHI) < 0.1

# Туршилт
sample_data = [1, 2, 1, 3, 4, 2, 5, 1] * 1000
clean_data = deduplicate_data(sample_data)
ratio, stable = phi_stability_check(clean_data)

print(f"Өмнө: {len(sample_data)} элемент")
print(f"Дэдүп хийсний дараа: {len(clean_data)} элемент")
print(f"Φ ratio: {ratio:.4f} | Тогтвортой: {stable}")
