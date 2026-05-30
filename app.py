import pickle
import streamlit as st
import numpy as np

## Loads the trained KNN model
model = pickle.load(open('artifacts/model.pkl', 'rb'))
## Loads list of all book names for the dropdown
books_name = pickle.load(open('artifacts/book_name.pkl', 'rb'))
## Loads dataframe with book titles and image URLs
final_rating = pickle.load(open('artifacts/final_ratings.pkl', 'rb'))
## Loads pivot table (books × users ratings matrix)
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fetch_poster(suggestion):
    books_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        books_name.append(book_pivot.index[book_id])

    for name in books_name[0]:
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for id in ids_index:
        url = final_rating.iloc[id]['img_url']
        poster_url.append(url)

    return poster_url 


def recommend_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)

    for i in suggestion:
        books = book_pivot.index[i]
        for j in books:
            book_list.append(j)

    return book_list, poster_url



## Streamlit UI

## Shows title at top of webpage
st.header("Book Recommender Sytem")

## Creates a dropdown with all book names
selected_books = st.selectbox(
    'Type or Select a Book', 
    books_name
)

## When user clicks the button, run recommendations
if st.button('Show Recommendation'):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])



