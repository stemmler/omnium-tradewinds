import altair as alt
import pandas as pd
import streamlit as st


# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).
@st.cache_data
def load_data():

    # TODO: want to load this data and all the calculatios more globally
    # and just access from these pages.
    df_accounts = pd.read_csv("data/customers.csv")

    # TODO: trying to get this to be clickable. still WIP
    # def make_clickable(url, name):
    #   return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(url,name)

    # # df['Customer'] = df.apply(lambda x: make_clickable(x['url'], x['name']), axis=1)
    # df_accounts['Customer'] = df_accounts.apply(lambda x: make_clickable("www.google.com", x['Customer']), axis=1)
    # df_accounts.apply(df["Customer"], '<a href="google.com">Test</a>')
    df_distribution = pd.read_csv("data/distribution.csv")
    df_pricing = pd.read_csv("data/pricing.csv")
    df_promotion = pd.read_csv("data/promotion.csv")
    return df_accounts, df_distribution, df_pricing, df_promotion

df_accounts, df_distribution, df_pricing, df_promotion = load_data()

c = st.container()

# top nav bar, but needs some fixing!
summary, distribution, base_price, promotions = c.tabs([
  "Account Summary", 
  "Distribution", 
  "Base Price", 
  "Promotions"
])

with summary:
  st.subheader("List of Accounts")
  st.dataframe(
    df_accounts,
    use_container_width=True,
  )

with distribution:
  st.dataframe(
      df_distribution,
      use_container_width=True,
  )

with base_price:
  st.dataframe(
      df_pricing,
      use_container_width=True,
  )

with promotions:
  st.dataframe(
      df_promotion,
      use_container_width=True,
  )