""" Avito Python practice for 13.10.2022 (Classes) """
from typing import List
import numpy as np


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
    tf_transformed = tf_transform(count_matrix)
    for string in tf_transformed:
        print(string)
    print('-' * 50)
    idf_transformed = idf_transform(count_matrix)
    print('Idf matrix:')
    print(idf_transformed)
    print('-' * 50)
    transformer = TfidfTransformer()
    tfidf_matrix = transformer.fit_transform(count_matrix)
    for string in tfidf_matrix:
        print(string)
    print('-' * 50)
    print('-' * 50)
    print('Для TfidfVectorizer:')
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    print('Список уникальных слов:')
    print(tfidf_vectorizer.get_features_names())
    print('\nМатрица:')
    for string in tfidf_matrix:
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
            _matrix.append([item[n_string]
                            for word, item in _dict_words.items()])
        self._feature_names = list(_dict_words)
        return _matrix

    def get_features_names(self):
        """
        Just return feature words
        """
        return self._feature_names


def tf_transform(count_matrix):
    """Term frequency transform"""
    tf_matrix = []
    for item in count_matrix:
        tf_matrix.append([round(amount/sum(item), 3) for amount in item])
    return tf_matrix


def idf_transform(count_matrix):
    """Inverse Document-frequency"""
    idf_matrix = []
    count_matrix = np.array(count_matrix)
    count_docs = np.sum(count_matrix > 0, axis=0)
    print(count_docs)
    for count in count_docs:
        idf_matrix.append(round(np.log((count_matrix.shape[0] + 1) /
                                       (count + 1)) + 1, 1))
    return idf_matrix


class TfidfTransformer:
    """Tf - idf transforming matrix """
    @staticmethod
    def count_tf_transform(count_matrix):
        """Term frequency transform"""
        tf_matrix = []
        for item in count_matrix:
            tf_matrix.append([round(amount / sum(item), 3) for amount in item])
        return tf_matrix

    @staticmethod
    def count_idf_transform(count_matrix):
        """Inverse Document-frequency"""
        idf_matrix = []
        count_matrix = np.array(count_matrix)
        count_docs = np.sum(count_matrix > 0, axis=0)
        for count in count_docs:
            idf_matrix.append(round(np.log((count_matrix.shape[0] + 1) /
                                           (count + 1)) + 1, 1))
        return idf_matrix

    def fit_transform(self, count_matrix):
        """Count tf-idf matrix"""
        tf_matrix = np.array(self.count_tf_transform(count_matrix))
        idf_matrix = np.array(self.count_idf_transform(count_matrix))
        tf_idf_matrix = tf_matrix * idf_matrix
        return tf_idf_matrix


class TfidfVectorizer(CountVectorizer):
    """tf - idf vectorizer"""
    def __init__(self):
        super().__init__()
        self._count_matrix = []
        self._transformer = TfidfTransformer()
        self._tf_matrix = []

    def fit_transform(self, text):
        """Return transformed matrix"""
        self._count_matrix = super().fit_transform(text)
        self._tf_matrix = self._transformer.fit_transform(self._count_matrix)
        return self._tf_matrix


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
