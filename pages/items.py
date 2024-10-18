import altair as alt
import pandas as pd
import streamlit as st


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/items.csv")
    return df

df = load_data()

st.dataframe(
    df,
    use_container_width=True,
)