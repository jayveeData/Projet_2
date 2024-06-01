import streamlit as st
import pandas as pd
import os
from PIL import Image
import requests
from io import BytesIO

# html / css
name =  pd.read_csv("~/Documents/CODE/Projet_2/streamlit_test/final_real2.csv")
name['overview'] = name['overview'].str.replace('()','Aucune description disponible')


background_list = ['https://www.lagazettedescommunes.com/wp-content/uploads/2021/08/cinema-salle-alexander-adobestock-187612077.jpg',
                   'https://i0.wp.com/c.wallhere.com/photos/16/80/cinema_movie_cine_movies_p_blico_premiere_viewer_pel_culas-1045589.jpg!d',
                   'https://cms-assets.webediamovies.pro/cdn-cgi/image/dpr=1,fit=scale-down,gravity=auto,metadata=none,quality=85,width=1920,height=1280/production/232/ccd853ae0d83943d3ffa3ac82ef59431.jpg']

   ### mise en place du background image 
st.markdown("""
    <style>
        .stApp {
            background-image: url('https://i0.wp.com/c.wallhere.com/photos/16/80/cinema_movie_cine_movies_p_blico_premiere_viewer_pel_culas-1045589.jpg!d');
            background-size: cover;
            background-position: center;
        }
    </style>
    """, unsafe_allow_html=True)


html_font = """
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap" rel="stylesheet">
"""
st.markdown(html_font, unsafe_allow_html=True)

# Appliquer la police Bebas Neue au titre
html_title = """
<div style="text-align:center;">
    <h1 style="font-family: 'Bebas Neue', cursive; font-size: 50px;">Recommandations de films francophones</h1>
</div>
"""
st.markdown(html_title, unsafe_allow_html=True)

# affiche bandeau
# col1, col2, col3,col4,col5,col6 = st.columns(6)
# col1.image('https://m.media-amazon.com/images/M/MV5BZWRhNDliMjEtNDFjZC00MmFlLTk0NDItN2YxNTg4OTcxZWUxXkEyXkFqcGdeQXVyMTIzMzQ1ODg4._V1_.jpg')
# col2.image('https://m.media-amazon.com/images/M/MV5BNTE2NDJiZTktMTJkYS00OTRmLWEzNjgtZTE5MmJjNTRlMzBmXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_.jpg')
# col3.image('https://m.media-amazon.com/images/M/MV5BY2YwMjdiOTgtNWU4My00ZmQwLThmZWQtZThiODNlNmY4OGIzXkEyXkFqcGdeQXVyMDYwNjc3OQ@@._V1_.jpg')
# col4.image('https://m.media-amazon.com/images/M/MV5BODg1YjI2OTQtZDdkMy00NDA4LTk4MDQtZWFiMjhiNjI5ZjUxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg')
# col5.image('https://m.media-amazon.com/images/M/MV5BNzhhODdhNjQtMmUwMi00MGI2LTljYWUtYmQzZGMzNjA2ZjhiXkEyXkFqcGdeQXVyMTYwMTAyMTU@._V1_.jpg')
# col6.image('https://m.media-amazon.com/images/M/MV5BNjM4MTFiNzctY2RmOC00YzBkLTgzNTYtZGE4NDdjOWVjNGY5XkEyXkFqcGdeQXVyNzI0MTY5MQ@@._V1_.jpg')


html_code = """
<div class="image-slider">
  <div class="slider">
    <!-- Ajoutez autant d'images que vous voulez dans la balise "slider" -->
    <img src="https://m.media-amazon.com/images/M/MV5BZWRhNDliMjEtNDFjZC00MmFlLTk0NDItN2YxNTg4OTcxZWUxXkEyXkFqcGdeQXVyMTIzMzQ1ODg4._V1_.jpg" alt="Image 1">
    <img src="https://m.media-amazon.com/images/M/MV5BNTE2NDJiZTktMTJkYS00OTRmLWEzNjgtZTE5MmJjNTRlMzBmXkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_.jpg" alt="Image 2">
    <img src="https://m.media-amazon.com/images/M/MV5BY2YwMjdiOTgtNWU4My00ZmQwLThmZWQtZThiODNlNmY4OGIzXkEyXkFqcGdeQXVyMDYwNjc3OQ@@._V1_.jpg" alt="Image 3">
    <img src="https://m.media-amazon.com/images/M/MV5BODg1YjI2OTQtZDdkMy00NDA4LTk4MDQtZWFiMjhiNjI5ZjUxXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_.jpg" alt="Image 4">
    <img src="https://m.media-amazon.com/images/M/MV5BNzhhODdhNjQtMmUwMi00MGI2LTljYWUtYmQzZGMzNjA2ZjhiXkEyXkFqcGdeQXVyMTYwMTAyMTU@._V1_.jpg" alt="Image 5">
    <img src="https://m.media-amazon.com/images/M/MV5BNjM4MTFiNzctY2RmOC00YzBkLTgzNTYtZGE4NDdjOWVjNGY5XkEyXkFqcGdeQXVyNzI0MTY5MQ@@._V1_.jpg" alt="Image 6">
    <img src="https://m.media-amazon.com/images/M/MV5BYzM5YmQzNmEtMTYwZS00NzA3LWE4MmUtOTdmNTE3YzBkYmNiXkEyXkFqcGdeQXVyODgzNDIwODA@._V1_.jpg" alt="Image 7">
    <img src="https://m.media-amazon.com/images/M/MV5BMTcyMDMzMzEwMV5BMl5BanBnXkFtZTcwMTE2OTc3MQ@@._V1_.jpg" alt="Image 8">
    <img src="https://m.media-amazon.com/images/M/MV5BM2U4YmU4NWYtYzZkOC00MTY5LThjMzMtZDQ3ZTMzMTM0ODg2XkEyXkFqcGdeQXVyODIyOTEyMzY@._V1_.jpg" alt="Image 9">
    <img src="https://m.media-amazon.com/images/M/MV5BMjAyODI1NDM4OV5BMl5BanBnXkFtZTgwMTM5NzU0MTI@._V1_.jpg" alt="Image 10">
    <img src="https://m.media-amazon.com/images/M/MV5BZDllNzczOTUtMTJjMy00ZjA3LTk2ODgtNDZhZWVkMzI1YWE2XkEyXkFqcGdeQXVyODgzNDIwODA@._V1_.jpg" alt="Image 11">
    <img src="https://m.media-amazon.com/images/M/MV5BMTY5NjEwODgwOV5BMl5BanBnXkFtZTgwMTcwMzAxMzE@._V1_.jpg" alt="Image 12">
    <img src="https://m.media-amazon.com/images/M/MV5BNTQ5NTk0NDkyNl5BMl5BanBnXkFtZTcwMTY5Mzk5Ng@@._V1_.jpg" alt="Image 13">
    <img src="https://m.media-amazon.com/images/M/MV5BN2UxZGU2NmQtOGVlNC00Y2NmLWI5NzQtNzE2NWE1YTQ0MDY4XkEyXkFqcGdeQXVyNTY0OTgzMzU@._V1_.jpg" alt="Image 14">
    <img src="https://m.media-amazon.com/images/M/MV5BOTIyOGFhM2MtOTQ2Mi00NjA1LWJjMDAtOGZjY2NhY2UwN2I0XkEyXkFqcGdeQXVyNjE4ODA3NTY@._V1_.jpg" alt="Image 15">
    <img src="https://m.media-amazon.com/images/M/MV5BNmFiZTdjZjktY2IxNi00YTBlLTgzYTMtZWY5MjQ4YjI3MDZjXkEyXkFqcGdeQXVyNjc5NTg2MzE@._V1_.jpg" alt="Image 16">
    <img src="" alt="Image 17">
    <img src="" alt="Image 18">
    <img src="" alt="Image 19">
    <img src="" alt="Image 20">

  </div>
</div>

<style>
/* Ajoutez le code CSS suivant dans la balise "style" */
.image-slider {
  width: 100%;
  height: 200px;
  overflow: hidden;
  position: relative;
}

.slider {
  width: calc(200px * 16); /* Largeur totale du bandeau (nombre d'images * largeur d'une image) */
  height: 200px;
  display: flex;
  animation: slide 20s infinite linear; /* Durée de l'animation et vitesse de défilement */
}

.slider img {
  width: 300px; /* Largeur d'une image */
  height: 200px; /* Hauteur d'une image */
  object-fit: contain; /* Permet de remplir toute la largeur et la hauteur de l'image sans déformation */
}

@keyframes slide {
  0% {
    transform: translateX(0); /* Position initiale du bandeau */
  }
  100% {
    transform: translateX(calc(-200px * 8)); /* Position finale du bandeau (décalage de 5 images vers la gauche) */
  }
}
</style>

"""

st.markdown(html_code, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["par film", "par réalisateur"])

with tab1:
    
    
    # with st.form(key='film_form'):
    #     # user_input = st.text_input('Entrez un film :').lower()
    #     user_input = st.selectbox('Entrez un film :', options=name['originalTitle'], format_func=lambda x: x.lower()).lower()
    #     submitted = st.form_submit_button('Rechercher')

    with st.form(key='film_form'):
    # Utilisez st.text_input pour saisir du texte
        user_input_text = st.text_input('Entrez un film :')

        # Créez une liste de suggestions en fonction de l'entrée de l'utilisateur
        if user_input_text:
            suggestions = [movie for movie in name['originalTitle'] if movie.lower().startswith(user_input_text.lower())]
        else:
            suggestions = []

        # Utilisez st.selectbox pour afficher les suggestions
        user_input = st.selectbox('', options=suggestions, format_func=lambda x: x.lower())

        # Soumettez le formulaire
        submitted = st.form_submit_button('Rechercher')



    if submitted:
        #                                                   // MACHINE LEARNING //
        ###########################################################################################################################################

        pwd = os.getcwd()
        filepath_bis = pwd +'/algo_cleaned_final.csv'
        filepath = pwd + '/algo-cast5.csv'
        filepath_2 =pwd + '/links_to_images.csv'

        df = pd.read_csv(filepath)
        dfs= pd.read_csv(filepath_bis)
        images = pd.read_csv(filepath_2)

        merged = df.merge(images, left_on = 'ID_extract',right_on='index',how='left')
        data= merged.drop(columns=['Unnamed: 0_x','Unnamed: 0_y','genre1','genre2','genre3','overview'])

        data.rename(columns = {'genre1_fr':'genre1','genre2_fr':'genre2','genre3_fr':'genre3','overview_fr':'overview'},inplace=True)

        data['genre2'] = data['genre2'].str.replace('Ô','')
        data['genre3'] = data['genre3'].str.replace('Ô','')
        


        data['ID'] = data['ID'].str.replace('aucune source',"https://previews.123rf.com/images/pe3check/pe3check1710/pe3check171000054/88673746-aucune-image-disponible-signe-ic%C3%B4ne-internet-pour-indiquer-l-absence-d-image-jusqu-%C3%A0-ce-que-celle.jpg")
        
        data['ID'].iloc[2023] = data['ID'].iloc[2023].replace('https://m.media-amazon.com/images/M/MV5BMTM1MjgxNTA2MF5BMl5BanBnXkFtZTcwMzY5ODIyMw@@._V1_.jpg','https://fr.web.img2.acsta.net/r_1280_720/medias/nmedia/18/67/97/92/19050069.jpg')
        data['ID'].iloc[1766] = data['ID'].iloc[1766].replace('https://m.media-amazon.com/images/M/MV5BZWM3ZTc0ZjktZmVjMy00ZDI2LWFkYzQtYWNkYmVhNzlkMDBkXkEyXkFqcGdeQXVyNjMxMTE2Mjg@._V1_.jpg',"https://m.media-amazon.com/images/I/81zjpUbgi9L._AC_UF1000,1000_QL80_.jpg")
        data['ID'].iloc[1014] = data['ID'].iloc[1014].replace('https://m.media-amazon.com/images/M/MV5BMTQzOTA0NDE1OF5BMl5BanBnXkFtZTcwMDI3NzY3MQ@@._V1_.jpg','https://hubmarketlive.blob.core.windows.net/media/e647a4e6-4dea-4f48-84bb-9bb2bc444318.jpg')

        data_vision = data[['originalTitle',
                            'startYear',
                            'runtimeMinutes',
                            'averageRating_x',
                            'Top_Box_office_$',
                            'genre1',
                            'genre2',
                            'genre3',
                            'popularity',
                            'isFamilyfact',
                            'ID',
                            'overview']]
        
        #### ML

        df_new = data[['startYear','runtimeMinutes','averageRating_x', 'Top_Box_office_$','genre1',
                'genre2', 'genre3', 'popularity','isFamilyfact',]]

        dummies = pd.get_dummies(df_new[['genre1','genre2','genre2']])
        dummies = dummies.astype(int)


        new_data = pd.concat([df_new,dummies],axis = 1)

        new_data = new_data.drop(columns=['genre1','genre2','genre3'])

        # standard scaler

        from sklearn.preprocessing import StandardScaler

        scaler = StandardScaler().fit(new_data)
        standardized = scaler.transform(new_data)

        std = pd.DataFrame(standardized)

        std.columns = new_data.columns

        from sklearn.neighbors import NearestNeighbors

        k = 6
        modelKNN = NearestNeighbors(n_neighbors=k).fit(std)

        film_title = user_input.lower()

        #                               // GESTION D'ERREUR POUR LE FAIT QU'IL N'Y A PAS DE FILM DE SPECIFIE AU DEBUT //
        ###########################################################################################################################################

        if film_title in data['originalTitle'].str.lower().values:
            film_index = data[data['originalTitle'].str.lower()==film_title].index[0]


        ###########################################################################################################################################

            film_features = std.iloc[film_index]

            # modelKNN.fit(std)

            # Trouver les indices des voisins les plus proches du film "Intouchables"
            neighbors_indices = modelKNN.kneighbors([film_features], return_distance=False)

            # Afficher les indices des voisins les plus proches
            print("Indices des voisins les plus proches :", neighbors_indices)


            ls = []
            for i in neighbors_indices[0][1:]:
                nv = data_vision.iloc[i]
                ls.append(nv)
            predict = pd.DataFrame(ls)
            
            predict['genre2'] = predict['genre2'].replace('O', ' ')
            predict['genre3'] = predict['genre3'].replace('O', ' ')
            predict['overview'] = predict['overview'].str.replace('()','Aucune description disponible')

       # image import 
            image_url_1 = predict['ID'].iloc[0]
            image_url_2 = predict['ID'].iloc[1]
            image_url_3 = predict['ID'].iloc[2]
            image_url_4 = predict['ID'].iloc[3]
                # Téléchargez l'image à partir de l'URL
            response_1 = requests.get(image_url_1)
            response_2 = requests.get(image_url_2)
            response_3 = requests.get(image_url_3)
            response_4 = requests.get(image_url_4)
                # Convertissez le contenu de la réponse en image
            image1 = Image.open(BytesIO(response_1.content))
            image2 = Image.open(BytesIO(response_2.content))
            image3 = Image.open(BytesIO(response_3.content))
            image4 = Image.open(BytesIO(response_4.content))


            size = (300, 400)
            image1.thumbnail(size)

            size = (300, 400)
            image2.thumbnail(size)

            size = (300, 400)
            image3.thumbnail(size)

            size = (300, 400)
            image4.thumbnail(size)

            annee1 = predict['startYear'].iloc[0]
            duree1 = str(predict['runtimeMinutes'].iloc[0])+'min'

            st.write(f"Vous avez aimé {film_title}? Ces films pourrait vous intérresser :")

            # affichage des images
            film1,film2 = st.columns(2)
            
            ########################## FILM 1  ##########################
            film1.markdown('---')
            film1.image(image1, caption= predict['originalTitle'].iloc[0])
            film1.markdown(f"<span style='color: yellow;'>{predict['genre1'].iloc[0]}</span> {predict['genre2'].iloc[1]} {predict['genre3'].iloc[2]}",unsafe_allow_html=True)
            film1.write(predict['overview'].iloc[0])
            film1.write(predict['startYear'].iloc[0])
            film1.write(str(predict['runtimeMinutes'].iloc[0])+'min')
            film1.markdown('---')

            
            ########################## FILM 2  ##########################
            film2.markdown('---')
            film2.image(image2, caption= predict['originalTitle'].iloc[1])
            film2.markdown(f"<span style='color: yellow;'>{predict['genre1'].iloc[0]}</span> {predict['genre2'].iloc[1]} {predict['genre3'].iloc[2]} ",unsafe_allow_html=True)
            film2.write(predict['overview'].iloc[1])
            film2.write(predict['startYear'].iloc[1])
            film2.write(str(predict['runtimeMinutes'].iloc[1])+'min')
            film2.markdown('---')

            
            film3,film4 = st.columns(2)
            ########################## FILM 3  ##########################
            film3.markdown('---')
            film3.image(image3, caption= predict['originalTitle'].iloc[2])
            film3.markdown(f"<span style='color: yellow;'>{predict['genre1'].iloc[0]}</span> {predict['genre2'].iloc[1]} {predict['genre3'].iloc[2]}",unsafe_allow_html=True)
            film3.write(predict['overview'].iloc[2])
            film3.write(predict['startYear'].iloc[2])
            film3.write(str(predict['runtimeMinutes'].iloc[2])+'min')
            film3.markdown('---')
            ########################## FILM 4  ##########################
            film4.markdown('---')
            film4.image(image4,caption= predict['originalTitle'].iloc[3])
            film4.markdown(f"<span style='color: yellow;'>{predict['genre1'].iloc[0]}</span> {predict['genre2'].iloc[1]} {predict['genre3'].iloc[2]}",unsafe_allow_html=True)
            film4.write(predict['overview'].iloc[3])
            film4.write(predict['startYear'].iloc[3])
            film4.write(str(predict['runtimeMinutes'].iloc[3])+'min')
            film4.markdown('---')


        else:
            st.write("Veuillez entrez un autre film,")



with tab2:


    # with st.form(key='director_form'):
    #     user_input = st.text_input('Entrez un film :').lower()
    #     submitted = st.form_submit_button('Rechercher')

    with st.form(key='director_form'):
    # Utilisez st.text_input pour saisir du texte
        user_input_text = st.text_input('Entrez un film :')

        # Créez une liste de suggestions en fonction de l'entrée de l'utilisateur
        if user_input_text:
            suggestions = name[name['originalTitle'].str.lower().str.strip().str.contains(user_input_text.lower())]['originalTitle'].tolist()
        else:
            suggestions = []

        # Utilisez st.selectbox pour afficher les suggestions
        user_input = st.selectbox('', options=suggestions, format_func=lambda x: x)

        # Soumettez le formulaire
        submitted = st.form_submit_button('Rechercher')

        if submitted:
            data = pd.read_csv("~/Documents/CODE/streamlit_test/final_real2.csv")

            data['genre2'] = data['genre2'].fillna('')
            data['genre3'] = data['genre3'].fillna('')

            chosen_film = user_input.lower().strip()

            film_data = data[data["originalTitle"].str.lower().str.strip() == chosen_film]

            if film_data.empty:
                st.write("Aucun film trouvé dans la base de données.")
            else:
                dir = film_data['director'].iloc[0]

                if pd.isna(dir) or dir == 'no info':
                    st.write("Aucune information sur le réalisateur de ce film")
                else:
                    film_by_dir = data[data['director'] == dir].sort_values(by='popularity', ascending=False)

                    # Exclure le film choisi et afficher les 5 films les plus populaires du réalisateur
                    top_film = film_by_dir[film_by_dir['originalTitle'].str.lower().str.strip() != chosen_film].iloc[:5]


            

                    if top_film.empty:
                        st.write(f"Nous sommes désolés, mais nous n'avons actuellement aucun autre film de {dir} dans notre base de données. Nous sommes toujours à la recherche de nouveaux films à ajouter, alors revenez bientôt !")

                    else:
                        image_urls = top_film['ID'].iloc[:len(top_film)]
                        responses = [requests.get(url) for url in image_urls]
                        images = [Image.open(BytesIO(response.content)) for response in responses]
                        
                        st.write(f"Vous avez aimé le film '{chosen_film}' ? Il est réalisé par {dir}. Découvrez d'autres films de ce réalisateur ci-dessous !")

                    
                            
                        cols = st.columns(2)

                        # Afficher les deux premiers films dans la première ligne
                       

                        for i, col in enumerate(cols):
                            with col:
                                if i < len(top_film):
                                    col.markdown("<div style='border: 2px solid black; padding: 10px;'>", unsafe_allow_html=True)
                                    col.image(images[i], caption=top_film['originalTitle'].iloc[i])
                                    col.markdown(f"<span style='color: yellow;'>{top_film['genre1'].iloc[i]}</span> {top_film['genre2'].iloc[i]} {top_film['genre3'].iloc[i]}", unsafe_allow_html=True)
                                    col.write(top_film['overview'].iloc[i])
                                    col.write(top_film['startYear'].iloc[i])
                                    col.write(str(top_film['runtimeMinutes'].iloc[i]) + 'min')
                                    col.markdown("</div>", unsafe_allow_html=True)

                        # Afficher les deux derniers films dans la deuxième ligne (s'il y en a)
                        if len(top_film) > 2:
                            cols = st.columns(2)
                            for i, col in enumerate(cols):
                                with col:
                                    if i + 2 < len(top_film):
                                        col.markdown("<div style='border: 2px solid black; padding: 10px;'>", unsafe_allow_html=True)
                                        col.image(images[i + 2], caption=top_film['originalTitle'].iloc[i + 2])
                                        col.markdown(f"<span style='color: yellow;'>{top_film['genre1'].iloc[i + 2]}</span> {top_film['genre2'].iloc[i + 2]} {top_film['genre3'].iloc[i + 2]}", unsafe_allow_html=True)
                                        col.write(top_film['overview'].iloc[i + 2])
                                        col.write(top_film['startYear'].iloc[i + 2])
                                        col.write(str(top_film['runtimeMinutes'].iloc[i + 2]) + 'min')
                                        col.markdown("</div>", unsafe_allow_html=True)

                            # Afficher le troisième film dans la deuxième ligne (s'il y en a trois)
                            if len(top_film) == 3:
                                cols = st.columns(1)
                                with cols:
                                    col.markdown("<div style='border: 2px solid black; padding: 10px;'>", unsafe_allow_html=True)
                                    col.image(images[2], caption=top_film['originalTitle'].iloc[2])
                                    col.markdown(f"<span style='color: yellow;'>{top_film['genre1'].iloc[2]}</span> {top_film['genre2'].iloc[2]} {top_film['genre3'].iloc[2]}", unsafe_allow_html=True)
                                    col.write(top_film['overview'].iloc[2])






                # ajouter texte s'il n'y a pas de directeur ( nom du directeur non disponible dans la base de données )                                             :ok 
                # ajouter texte s'il il n'y a pas d'autre film du même directeur dans notre databse ( aucune autre film du même directeur dans la base de données ) :ok
                # ajouter texte pour onglet réalisateur (voici d'autre film du même réalisateur)                                                                    :ok
                # ajouter autocompletion / suggestion tab 2                                                                                                         :ok
                # gerer le synopsis vide                                                                                                                            :ok
                # changer affiche de Chouchou

