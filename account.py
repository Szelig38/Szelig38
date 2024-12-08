import streamlit as st
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests


def app():
        st.title('Welcome to :violet[JohnleggyDataHub] :sunglasses:')

        choice = st.selectbox('Login/Signup',['Login','Sign Up'])
        if choice=='Login':

            email=st.text_input('Email Address')
            password = st.text_input('Password', type='password')
            
            st.button('Login')

        else:

            email=st.text_input('Email Address')
            password = st.text_input('Password', type='password')
