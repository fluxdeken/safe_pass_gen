import secrets

def get_phrase(num: int) -> str:
    with open("phrases.txt", "r") as f:
        text = f.read()
        arr = text.split()
        words = arr[1::2]
        r_words = [secrets.choice(words) for _ in range(num)]
        sep = '-'
        return sep.join(r_words)

phrase = get_phrase(7)
print(phrase)