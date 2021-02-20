"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from SeoProject import app

from SeoProject import stop_words
from SeoProject import lemmatizing_word
from SeoProject import search_data_dictionary
from SeoProject import GS
from SeoProject import PageRerank_Algo
from SeoProject import SERP_2_HTML_convert

@app.route('/')
@app.route('/home')
def home():

    #Proj Code:
    #user_query = request.values["user_query"]
    user_query = "going cheer jaipur today 's cricket match news tommrow"
    print("Log: User Query Recived")

    stop_words_removed_user_query = stop_words.stop_words(user_query)
    print("Log: Stop Words Removed")

    lemmatized_user_query = lemmatizing_word.lemmatizing_word(stop_words_removed_user_query)
    print("Log: Query Lemmatized")

    data_dictionary_search_result = search_data_dictionary.init_for_search(str(lemmatized_user_query))
    print("Log: Data Dictionary Module Done")

    crawler_SEPRP = GS.prep_for_inbound(data_dictionary_search_result, str(lemmatized_user_query))
    print("Log: Crawler Done")
    
    Rerank_SERP = PageRerank_Algo.init_for_rerank(crawler_SEPRP, user_query)
    print("Log: Re-rank Done")
    
    Rerank_SERP_str = SERP_2_HTML_convert.convert(Rerank_SERP)
    
    print("Rerank_SERP_str: " + Rerank_SERP_str)

    #Renders the home page.
    return render_template('index.html',
        title='Home Page',
        year=datetime.now().year,)

@app.route('/contact')
def contact():
    #Renders the contact page.
    return render_template('contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.')

@app.route('/about')
def about():
    #Renders the about page.
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.')
