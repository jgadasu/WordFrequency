"""Analyze the word frequencies in a book downloaded from Project Gutenberg."""

import string


def get_word_list(file_name):
    """Read the specified project Gutenberg book.

    Header comments, punctuation, and whitespace are stripped away. The function
    returns a list of the words used in the book as a list. All words are
    converted to lower case.
    """
    with open (file_name,'r') as file:
        text=file.read()
    start = text.find('START OF THIS PROJECT GUTENBERG EBOOK')
    text = text[start+len('START OF THIS PROJECT GUTENBERG EBOOK'):]
    text = text.translate( string.punctuation).lower().strip()
    return text.split()

def get_top_n_words(word_list, n):
    """Take a list of words as input and return a list of the n most
    frequently-occurring words ordered from most- to least-frequent.

    Parameters
    ----------
    word_list: [str]
        A list of words. These are assumed to all be in lower case, with no
        punctuation.
    n: int
        The number of words to return.

    Returns
    -------
    int
        The n most frequently occurring words ordered from most to least.
    frequently to least frequentlyoccurring
    """
    count = {}
    for elem in word_list:
        init = count.get(elem,0)
        count[elem] = init + 1
    word_freq = sorted(count.items(), key = lambda x: -x[1])
    return [elem for elem, frequency in word_freq[:n]]


if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(string.punctuation)
    word_list = get_word_list('pg32325.txt')
    print (get_top_n_words(word_list,100))
