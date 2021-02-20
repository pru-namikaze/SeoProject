"""
This script runs the SeoProject application using a development server.
"""

from os import environ
from SeoProject import app

import  nltk

if __name__ == '__main__':

    nltk.download("stopwords")
    nltk.download("punkt")
    nltk.download('averaged_perceptron_tagger')
    nltk.download('wordnet')

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
