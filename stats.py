def count_words(text):
    words = text.split()
    return len(words)


# python
# python
def count_characters(text):
    counts = {}
    for ch in text.lower():
        if 'a' <= ch <= 'z':  # only ASCII letters
            counts[ch] = counts.get(ch, 0) + 1
    return counts

# This is the helper function for sorting.
# It tells the .sort() method to use the "num" value of each dictionary.


def sort_on(d):
    return d["num"]


# python
# python
def chars_dict_to_sorted_list(char_counts_dict):
    items = [{"char": c, "num": n} for c, n in char_counts_dict.items()]
    items.sort(key=lambda d: (-d["num"], d["char"]))
    return items
