import streamlit as st
import pickle

new_books_sample = pickle.load(open('books_sample_df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Book Recommender System')

selected_book = st.selectbox('Select a book', new_books_sample['Title'].values)

import requests

def fetch_cover(book_name):
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q={}'.format(book_name))
    data = response.json()
    return data
def recommend(book,similarity):
    index_pos = new_books_sample[new_books_sample['Title'] == book].index[0]
    book_list = sorted(list(enumerate(similarity[index_pos])), key=lambda x: x[1], reverse=True)[1:6]

    return book_list
if st.button('Recommend'):
    book_list = recommend(selected_book,similarity)

    # for item in book_list:
    #     book_name = new_books_sample.iloc[item[0]]['Title']
    #     st.header(book_name)
    #     data = fetch_cover(book_name)
    #     st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        book_name = new_books_sample.iloc[book_list[0][0]]['Title']
        st.text(book_name)
        data = fetch_cover(book_name)
        try:
            st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
        except:
            st.image('https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png')

    with col2:
        book_name = new_books_sample.iloc[book_list[1][0]]['Title']
        st.text(book_name)
        data = fetch_cover(book_name)
        try:
            st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
        except:
            st.image('https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png')

    with col3:
        book_name = new_books_sample.iloc[book_list[2][0]]['Title']
        st.text(book_name)
        data = fetch_cover(book_name)
        try:
            st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
        except:
            st.image('https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png')

    with col4:
        book_name = new_books_sample.iloc[book_list[3][0]]['Title']
        st.text(book_name)
        data = fetch_cover(book_name)
        try:
            st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
        except:
            st.image('https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png')

    with col5:
        book_name = new_books_sample.iloc[book_list[4][0]]['Title']
        st.text(book_name)
        data = fetch_cover(book_name)
        try:

            st.image(data['items'][0]['volumeInfo']['imageLinks']['thumbnail'])
        except:
            st.image('https://user-images.githubusercontent.com/24848110/33519396-7e56363c-d79d-11e7-969b-09782f5ccbab.png')