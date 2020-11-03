import os
from spellchecker import SpellChecker
import re
import secrets
import nltk
import numpy as np
from nltk.corpus import stopwords
from PIL import Image
from flask import url_for, jsonify
from flaskblog import app
from tensorflow.keras import backend as K
from gensim.test.utils import common_texts
from gensim.models import Word2Vec, KeyedVectors
from tensorflow.keras.models import Sequential, load_model, model_from_config
from tensorflow.keras.layers import Dropout, Dense, Input, Embedding, LSTM, Dense, Dropout, Lambda, Flatten
from sklearn.model_selection import train_test_split
from pymagnitude import Magnitude
from nltk.tokenize import sent_tokenize

num_features = 300
num_features = 300
min_word_count = 40
num_workers = 4
context = 10
downsampling = 1e-3
model = Magnitude(
    'C://Users//Bevan//Desktop//New folder (3)//flask//GoogleNews-vectors-negative300.magnitude')


def paper_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'static/writingpaper', picture_fn)
    output_size = (350, 450)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def calculate_mean(array):
    minval = 11
    maxval = 13
    array = array.reshape(array.shape[0])
    mean_array = array[(array > 5) & (array != np.nan)]
    mean = np.mean(mean_array)*25/60
    return (mean-minval)/(maxval-minval)*25


def load_model():

    K.clear_session()
    nmodel = Sequential()
    nmodel.add(LSTM(units=96, return_sequences=True, input_shape=(30, 300)))
    nmodel.add(Dropout(0.2))
    nmodel.add(LSTM(units=96, return_sequences=True))
    nmodel.add(Dropout(0.2))
    nmodel.add(LSTM(units=96, return_sequences=True))
    nmodel.add(Dropout(0.2))
    nmodel.add(LSTM(units=96, return_sequences=False))
    nmodel.add(Dropout(0.2))
    nmodel.add(Dense(units=5, activation='softmax'))
    nmodel.compile(loss='categorical_crossentropy',
                   optimizer='adam', metrics=['accuracy'])
    nmodel.load_weights('Cohesion LSTM V2.h5')

    return nmodel


def get_model():
    """Define the model."""
    K.clear_session()
    model = Sequential()
    model.add(LSTM(300, dropout=0.4, recurrent_dropout=0.4,
                   input_shape=[1, 300], return_sequences=True))
    model.add(LSTM(64, recurrent_dropout=0.4))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='relu'))
    model.compile(loss='mean_squared_error',
                  optimizer='rmsprop', metrics=['mae'])
    model.load_weights('LSTM-score.h5')
    return model


def essay_to_wordlist(essay_v, remove_stopwords):
    """Remove the tagged labels and word tokenize the sentence."""
    essay_v = re.sub("[^a-zA-Z]", " ", essay_v)
    words = essay_v.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return (words)


def getAvgFeatureVecs(essays, model, num_features):
    """Main function to generate the word vectors for word2vec model."""
    counter = 0
    essayFeatureVecs = np.zeros((len(essays), num_features), dtype="float32")
    for essay in essays:
        essayFeatureVecs[counter] = makeFeatureVec(essay, model, num_features)
        counter = counter + 1
    return essayFeatureVecs


def makeFeatureVec(words, model, num_features):
    """Make Feature Vector from the words list of an Essay."""
    featureVec = np.zeros((num_features,), dtype="float32")
    num_words = 0.
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            num_words += 1
            featureVec = np.add(featureVec, model[word])
    featureVec = np.divide(featureVec, num_words)
    return featureVec


def grammar():
    model = KeyedVectors.load_word2vec_format(
        'word2vecmodel.bin', binary=True, limit=10 ** 5)
    model.init_sims(replace=True)
    model.save('word2vecmodel')
    return 'word2vecmodel'


def get_grammar_result(test_answer):

    test_answer = essay_to_wordlist(test_answer, remove_stopwords=True)
    print(os.getcwd())
    # model = Word2Vec.load('word2vecmodel.bin', binary=True)
    model = KeyedVectors.load_word2vec_format(
        'word2vecmodel.bin', binary=True, limit=10 ** 5)
    model.init_sims(replace=True)
    model.save('word2vecmodel')

    test_answer = getAvgFeatureVecs(test_answer, model, num_features)

    test_answer = np.array(test_answer)
    print(test_answer.shape)
    test_answer = np.reshape(
        test_answer, (test_answer.shape[0], 1, test_answer.shape[1]))

    lstm_model = get_model()
    result = lstm_model.predict(test_answer)
    print(result, np.sum(result), len(result), np.nanmean(result))
    # marks=round(np.nanmean(result)/60*25)
    marks = calculate_mean(result)
    print(marks)
    return marks


def get_cohesion_result(paragraph):

    category_dict = {0: 0, 1: 25, 2: 50, 3: 75, 4: 100}

    sentences = sent_tokenize(paragraph)
    marksArray = []

    for sentence in sentences:

        data_tok = nltk.word_tokenize(sentence)

        data_vector = [model.query(word) for word in data_tok]

        sentence_end = np.ones((300,), dtype=np.float32)

        data_vector[29:] = []  # limitting the words in a sentence to 30
        data_vector.append(sentence_end)

        if(len(data_vector) < 30):
            for i in range(30-len(data_vector)):
                # filling the empty words from vector of ones
                data_vector.append(sentence_end)

        data_vector = np.array(data_vector)

        data_vector = data_vector.reshape(1, 30, 300)

        nmodel = load_model()
        results = nmodel.predict(data_vector)

        marks_category = np.argmax(results, axis=1)[0]

        print(results, marks_category)

        marks = category_dict[marks_category]
        marksArray.append(marks)
        print(results)
    return np.mean(np.array(marksArray))


def check_spellings(paragraph):
    miss_words = []
    corrected_words = []
    candidate_words = []

    data_tok = nltk.word_tokenize(paragraph)
    print(paragraph, data_tok)

    spell = SpellChecker()

    # find those words that may be misspelled
    # find those words that may be misspelled
    misspelled = spell.unknown(data_tok)

    for word in misspelled:
        # Get the one `most likely` answer

        miss_words.append(
            [word, spell.correction(word), spell.candidates(word)])

    return str([miss_words])
