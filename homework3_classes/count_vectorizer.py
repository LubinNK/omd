""" Implementing Class CountVectorizer """
from typing import List


def main_print(corpus: List[str]):
    """Launching and printing"""
    print('-' * 50)
    print(f'Текст:\n {corpus}')
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print('Список уникальных слов:')
    print(vectorizer.get_features_names())
    print('\nМатрица:')
    for string in count_matrix:
        print(string)
    print('-' * 50)


class CountVectorizer:
    """ Count the amount of words from the vocabulary in the text """
    def __init__(self):
        self._feature_names = []

    def fit_transform(self, text: List[str]):
        """
        Input: List of strings (n_strings)
        Return: List of shape (n_strings, n_words)

        Count the matrix of the amount of each word in each string
        """
        self._feature_names = []
        _matrix = []
        _dict_words = {}
        for n_string, string in enumerate(text):
            words = string.lower().split()
            for word in words:
                if word in _dict_words:
                    _dict_words[word][n_string] += 1
                else:
                    _dict_words[word] = [0] * len(text)
                    _dict_words[word][n_string] = 1
        for n_string in range(len(text)):
            _matrix.append([item[n_string] for word, item in _dict_words.items()])
        self._feature_names = list(_dict_words)
        return _matrix

    def get_features_names(self):
        """
        Just return feature words
        """
        return self._feature_names


if __name__ == '__main__':
    corpus_1 = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    corpus_2 = [
        'Triple CTC try guesT',
        'Double int was triple'
    ]
    corpus_3 = corpus_1 + corpus_2
    main_print(corpus_1)
    main_print(corpus_2)
    main_print(corpus_3)
