def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words_with_prefix = [prefix + word for word in vocab_words[1:]]
    return f'{prefix} :: ' + ' :: '.join(words_with_prefix)
        
def remove_suffix_ness(word):
    if word.endswith("ness"):
        root = word[:-4]
        if root.endswith("i"):
            return root[:-1] + "y"
        return root
    return word

def adjective_to_verb(sentence, index):
    words = sentence.split()
    return words[index].strip(".,") + "en"
