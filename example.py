# https://towardsdatascience.com/creating-multipage-applications-using-streamlit-efficiently-b58a58134030
import streamlit as st

# Custom imports
from multipage import MultiPage
from pages import water_chemistry, jab_effort

# Create an instance of the app
app = MultiPage()

# Title of the main page
st.title("Example")

# Add all your applications (pages) here
app.add_page("Stream Water Chemistry Datasheet", water_chemistry.app)
app.add_page("20-Jab Effort Datasheet", jab_effort.app)

# The main app
app.run()
