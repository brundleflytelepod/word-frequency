banned_chars = [".", ",", '"', "'", "?", "!", "@", "&", "%",
                "$", "' ", " - ", " '"]
spaced_banned = ["' ", " - ", " '",]

def clean_it(word):
    """Strips unwanted characters from the file."""
    banned_chars = [".", ",", '"', "'", "?", "!", "@", "&", "%",
                    "$", "' ", " - ", " '"]
    spaced_banned = ["' ", "-", " '", ' ']

    word = word.lower()

    for char in word:
        if char in banned_chars:
            word = word.replace(word, '')

        elif char in spaced_banned:
            word = word.replace(word, ' ')

    return word



def word_frequency(file_name):
    "Determines how many times a word occurs in a text file."""

    with open(file_name) as text:
        file = text.readlines()
        word_dict = {}
        clean_list = []
        final_list = []

        for word in file:
            word = word.split()
            clean_list.extend(word)

        for word in clean_list:
            final_list.append(clean_it(word))

        for word in final_list:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    sorted_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    top_20 = sorted_dict[1:20] # couldn't figure out how to leave spaces out of count, so I started at the next highest value
    for key, value in top_20:
        print("{}: {}".format(key, value))


print(word_frequency("sample.txt"))




##Big props to Zack Cooper and Lee
