import pandas as pd
import streamlit as st


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():
    df = pd.read_csv("data/customers.csv")

    # add financial summary data to this but dummy to start
    
    df['Total Units'] = df["Number of Stores"]
    df['Non-Promo Units'] = df["Number of Stores"]
    df['Promo Units'] = df["Number of Stores"]
    df['Base Units'] = df["Number of Stores"]
    df['Incremental Units'] = df["Number of Stores"]
    return df

df = load_data()

c = st.container()

c.subheader("Total Financial Summary")

c.dataframe(
    df,
    use_container_width=True,
)