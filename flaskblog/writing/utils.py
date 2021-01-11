# Senevirathne S.S. - IT17127042
# 3.0
# 12-05-2020

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

# Size of the vector
num_features = 300

# Word2vec model
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

# Calculate the mean of the grammar result


def calculate_mean(array):
    minval = 11
    maxval = 13
    array = array.reshape(array.shape[0])
    mean_array = array[(array > 5) & (array != np.nan)]
    mean = np.mean(mean_array)*25/60
    # Return the marks out of 25
    return (mean-minval)/(maxval-minval)*25


""" Neural network architecture of cohesion model using RNN-LSTM """


def load_model():
    # Reset keras backend after every prediction
    K.clear_session()

    # Initialized the network
    nmodel = Sequential()

    # Units are number of neurones
    # The first LSTM layer with 96 neurones
    nmodel.add(LSTM(units=96, return_sequences=True, input_shape=(30, 300)))
    # To reduce the overfitting used dropout layers
    # Dropout layer (probability=0.2)
    nmodel.add(Dropout(0.2))
    # The second LSTM layer with 96 neurones
    nmodel.add(LSTM(units=96, return_sequences=True))
    # Dropout layer (probability=0.2)
    nmodel.add(Dropout(0.2))
    # The third LSTM layer with 96 neurones
    nmodel.add(LSTM(units=96, return_sequences=True))
    # Dropout layer (probability=0.2)
    nmodel.add(Dropout(0.2))
    # The fourth LSTM layer with 96 neurones
    nmodel.add(LSTM(units=96, return_sequences=False))
    # Dropout layer (probability=0.2)
    nmodel.add(Dropout(0.2))
    # The final LSTM layer is a dense layer with 5 neurones
    # With softmax activation
    nmodel.add(Dense(units=5, activation='softmax'))

    """ Compile the model
    Categorical crossentropy used as a loss which is a classification problem
    Adaptive moment estimation used as an optimizer
    While training the data, accuracy will be displayed when use the metrics parameter """

    nmodel.compile(loss='categorical_crossentropy',
                   optimizer='adam', metrics=['accuracy'])

    # Load the weights of Cohesion LSTM v2.h5
    # H5 file consist of the weights and architecture
    nmodel.load_weights('Cohesion LSTM V2.h5')

    # Return model
    return nmodel

    """ Neural network architecture of grammar model using RNN-LSTM """


def get_model():
    # Reset keras backend after every prediction
    K.clear_session()

    # Initialized the network
    model = Sequential()

    """ Adding a LSTM layer with 300 cells with a dropout and recurrent probability of 0.4
        Input 300 word vector
        Returning output from each all the neurons """

    model.add(LSTM(300, dropout=0.4, recurrent_dropout=0.4,
                   input_shape=[1, 300], return_sequences=True))
    # The second LSTM layer with 64 neurones
    model.add(LSTM(64, recurrent_dropout=0.4))
    # To reduce the overfitting used dropout layers
    # Dropout layer (probability=0.2)
    model.add(Dropout(0.5))
    # The final LSTM layer with relu activation function
    # Dense layer of 1 neurones
    model.add(Dense(1, activation='relu'))

    """ Compile the model
        Mean squared error used as a loss which is a regression problem
        RMSprop used as an optimizer
        While training the data, mean absolute error will be displayed when use the metrics parameter """

    model.compile(loss='mean_squared_error',
                  optimizer='rmsprop', metrics=['mae'])

    # Load the weights of LSTM-score.h5
    # h5 file consist of the weights and architecture of grammar model
    model.load_weights('LSTM-score.h5')

    # Return model
    return model


def essay_to_wordlist(essay_v, remove_stopwords):
    # Remove the tagged labels and word tokenize the sentence.
    essay_v = re.sub("[^a-zA-Z]", " ", essay_v)
    words = essay_v.lower().split()
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    return (words)


def getAvgFeatureVecs(essays, model, num_features):
    # Main function to generate the word vectors for word2vec model.
    counter = 0
    essayFeatureVecs = np.zeros((len(essays), num_features), dtype="float32")
    for essay in essays:
        essayFeatureVecs[counter] = makeFeatureVec(essay, model, num_features)
        counter = counter + 1
    return essayFeatureVecs


def makeFeatureVec(words, model, num_features):
    # Make Feature Vector from the words list of an Essay.
    featureVec = np.zeros((num_features,), dtype="float32")
    num_words = 0.
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            num_words += 1
            featureVec = np.add(featureVec, model[word])
    featureVec = np.divide(featureVec, num_words)
    return featureVec

# Load the word2vec model


def grammar():
    model = KeyedVectors.load_word2vec_format(
        'word2vecmodel.bin', binary=True, limit=10 ** 5)
    model.init_sims(replace=True)
    model.save('word2vecmodel')
    return 'word2vecmodel'

    """ Provide the grammar result """


def get_grammar_result(test_answer):
    os.chdir('/Users/Bevan/Desktop/New folder (3)/flask/flaskblog/static/')
    # Call the essay_to_wordlist
    test_answer = essay_to_wordlist(test_answer, remove_stopwords=True)
    print(os.getcwd())
    # model = Word2Vec.load('word2vecmodel.bin', binary=True)
    # Load the word2vec model

    model = KeyedVectors.load_word2vec_format(
        'word2vecmodel.bin', binary=True, limit=10 ** 5)
    model.init_sims(replace=True)
    model.save('word2vecmodel')

    # Call the getAvgFeatureVecs
    test_answer = getAvgFeatureVecs(test_answer, model, num_features)

    # Converted the tokenized array into numpy array before applying the neural network
    test_answer = np.array(test_answer)

    # print(test_answer.shape)

    # Coverting the test answer into 3 dimensional array before applying to the neural network
    test_answer = np.reshape(
        test_answer, (test_answer.shape[0], 1, test_answer.shape[1]))

    # Get the model
    lstm_model = get_model()
    print(test_answer)
    # Get the prediction
    result = lstm_model.predict(test_answer)

    # print(result, np.sum(result), len(result), np.nanmean(result))
    # marks=round(np.nanmean(result)/60*25)

    # Calculate the mean
    marks = calculate_mean(result)

    # print(marks)

    # Return marks
    return marks

    """ Provide the cohesion result """


def get_cohesion_result(paragraph):
    """ Five categories of cohesion marks
        0 coesion words = 0 mark
        1 cohesion words = 25 marks
        2 cohesion words = 50 marks
        3 cohesion words = 75 marks
        4 cohesion words = 100 marks """

    category_dict = {0: 0, 1: 25, 2: 50, 3: 75, 4: 100}

    # Tokenized the paragraph
    sentences = sent_tokenize(paragraph)
    # Append to the array
    marksArray = []

    for sentence in sentences:

        # Tokernized sentences into the words
        data_tok = nltk.word_tokenize(sentence)

        # Vectorized
        data_vector = [model.query(word) for word in data_tok]

        # The size of each sentence vector should be limited to 30
        # Each vector represent the 300 numeric values
        sentence_end = np.ones((300,), dtype=np.float32)

        # Limit words to 30 in a sentence
        data_vector[29:] = []
        data_vector.append(sentence_end)

        if(len(data_vector) < 30):
            for i in range(30-len(data_vector)):
                # filling the empty words from vector of ones
                data_vector.append(sentence_end)

        # Converted the vectorized array into numpy array before applying the neural network
        data_vector = np.array(data_vector)

        # Coverte to the 3 dimensional array before applying to the neural network
        # 30 = number of words
        # 300 = size of the each word of the vector
        data_vector = data_vector.reshape(1, 30, 300)

        # Load the model
        nmodel = load_model()
        # Predict the result
        results = nmodel.predict(data_vector)

        # Check the maximum argument of the marks
        marks_category = np.argmax(results, axis=1)[0]

        # Print the result and the marks category
        print(results, marks_category)

        marks = category_dict[marks_category]

        # Append to marksArray
        marksArray.append(marks)

        # print(results)
    return np.mean(np.array(marksArray))*25/100

    """ Define spelling approch using pyspellchecker """


def check_spellings(paragraph):
    # Mispelled word
    miss_words = []
    # Correct word
    corrected_words = []
    # Similar words
    candidate_words = []

    # Tokernized the paragraph
    data_tok = nltk.word_tokenize(paragraph)
    print(paragraph, data_tok)

    # Create the object
    spell = SpellChecker()

    # Pass the tokernized paragraph to the spell object
    misspelled = spell.unknown(data_tok)

    # Inside the mispelled object consist of mispelled word, correct word and the similar words
    words = []
    corrections = []
    candidates = []

    # Get the mispelled words
    for word in misspelled:

        # Append mispelled words
        words.append(word)
        # Append correct words
        corrections.append(spell.correction(word))
        # Append all similar words
        candidateStr = ""
        for candidate in spell.candidates(word):
            candidateStr = candidateStr+" "+candidate
        candidates.append(candidateStr)
    print("---------------------------------------------")
    print(words, corrections, candidates)
    print("---------------------------------------------")

    myStr = ""

    # Get the whole words into same line
    for i in range(len(words)):
        myStr = myStr+"Misplled Word-" + \
            words[i]+", Correction-"+corrections[i] + \
            ", Candidate Words-"+candidates[i]+'\n'
    print(myStr)
    return myStr
