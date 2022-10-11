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
        self._matrix = []
        self._dict_words = {}

    def fit_transform(self, text: List[str]):
        """
        Input: List of strings (n_strings)
        Return: List of shape (n_strings, n_words)

        Count the matrix of the amount of each word in each string
        """
        self._feature_names = []
        self._matrix = []
        self._dict_words = {}
        for string in text:
            words = string.lower().split()
            for word in words:
                self._dict_words[word] = 0
        self._feature_names = self._dict_words.keys()
        for string in text:
            words = string.lower().split()
            _dict_words_temp = self._dict_words.copy()
            for word in words:
                _dict_words_temp[word] += 1
            self._matrix.append(list(map(lambda x: x[1], _dict_words_temp.items())))
        return self._matrix

    def get_features_names(self):
        """
        Just return feature words
        """
        return list(self._feature_names)


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
