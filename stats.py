def get_word_count(book_content):
    words = book_content.split()
    return len(words)

def get_letter_count(book_content):
    chars = {}
    for c in book_content:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_by_count(letter_dict):
    def num_return(k):
        return k["num"]

    sorted_list=[]
    for (k,v) in letter_dict.items():
        sorted_list.append({"char": k, "num": v})

    sorted_list.sort(key=num_return, reverse=True)

    return sorted_list
