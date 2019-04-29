from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
class Vectorizer:
    MAX_NB_WORDS = 5000
    MAX_SEQUENCE_LENGTH = 100

    def __init__(self):
        self.tokenizer = Tokenizer(num_words=self.__class__.MAX_NB_WORDS)

    def fit(self, texts):
        self.tokenizer.fit_on_texts(texts)
        self.word_index = self.tokenizer.word_index

    def transform(self, texts):
        sequences = self.tokenizer.texts_to_sequences(texts)
        return pad_sequences(sequences, maxlen=self.__class__.MAX_SEQUENCE_LENGTH)

    def fit_transform(self, texts):
        self.fit(texts)
        return self.transform(texts)
