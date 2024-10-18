import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Omnium Tradewinds")
st.title("Omnium Tradewinds")

pg = st.navigation([st.Page("pages/accounts.py"), st.Page("pages/items.py")])
pg.run()
