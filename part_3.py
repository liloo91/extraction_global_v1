#import module
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

#donnée de l'authentification
donneesDeCpte = {"usernames":
                {"utilisateur" :
                    {"name" : "utilisateur",
                    "password" : "utilisateurMDP",
                    "role" : "utilisateur"},
                 "root":
                    {"name" : "root",
                    "password" : "rootMDP",
                    "role": "administrateur"}
                    }
                }
authenticator = Authenticate(donneesDeCpte)
authenticator.login()

#page accueil si ok connexion
def accueil():
    with st.sidebar:
        authenticator.logout("Déconnexion") #bouton déconnexion via Authenticate
        st.write("Bienvenue à toi")
        selection = option_menu(menu_title=None,
                                options=["Accueil", "Photos"])
    if selection == "Accueil":
        st.title("Bienvenue sur dans ton univers connecté")
        st.image("https://media.tenor.com/fzcZe2pe6iAAAAAM/good.gif")
    elif selection == "Photos":
        st.title("Bienvenue sur l'album photo de ton animal")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://media.istockphoto.com/id/1293763250/fr/photo/chaton-mignon-l%C3%A9chant-la-table-en-verre-avec-lespace-de-copie.jpg?s=612x612&w=0&k=20&c=mWo6TYYuAEd8kvsBf61kVkj6_KoXmuAN6Fl5Bc2owRA=")
        with col2:
            st.image("https://m.media-amazon.com/images/I/61cKIWLVTkL.jpg")
        with col3:    
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdiMMNYm7SHbZ1I5HFFVy24P-ZqaM7bJDiFA&s")

#page d'authentification
if st.session_state["authentication_status"]:
    accueil()
elif st.session_state["authentication_status"] is False:
    st.error("Les infos sont erronées")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être rempli")