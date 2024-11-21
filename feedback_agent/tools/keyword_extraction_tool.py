import random
from typing import List

def extract_keywords(text: str) -> List[str]:
    words = text.split()
    return random.sample(words, min(len(words), 5))
