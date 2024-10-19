import pandas as pd
import streamlit as st

st.set_page_config(page_title="Omnium Tradewinds")
st.title("Omnium Tradewinds")

# left side navbar
pg = st.navigation([
  st.Page("pages/financial_summary.py", title="Financial Summary"), 
  st.Page("pages/accounts.py", title="Accounts"), 
  st.Page("pages/items.py", title="Items")
])
pg.run()
