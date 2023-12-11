import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True, key = lambda x: x[1])[1:6] 
    recommended_movies=[]
    poster=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        poster.append(movies.iloc[i[0]].poster_path)
        
    return recommended_movies, poster
        # print(i[0])

similarity= pickle.load(open('similarity.pkl', 'rb'))    
movies_dict= pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Please choose any particular movie then system will recommend?',
                    movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # for i in range(5):
    #         if i == 0 or i == 2:  # Putting items in the first row and skipping the second row
    #             with col1:
    #                 st.text(names[i])
    #                 st.image(posters[i])
    #         elif i == 1 or i == 3:  # Skipping items in the first row and putting them in the second row
    #             with col2:
    #                 st.text(names[i])
    #                 st.image(posters[i])
    #         elif i == 4:
    #             with col3:
    #                 st.text(names[i])
    #                 st.image(posters[i])
    
    for i in range(5):
        if i == 0 or i == 2:  # Putting items in the first row and skipping the second row
            with col1:
                st.markdown(f"**{names[i]}**")
                st.image(posters[i], width=125)
        elif i == 1 or i == 3:  # Skipping items in the first row and putting them in the second row
            with col2:
                st.markdown(f"**{names[i]}**")
                st.image(posters[i], width=125)
        elif i == 4:
            with col3:
                st.markdown(f"**{names[i]}**")
                st.image(posters[i], width=125)
                    
                    
                    