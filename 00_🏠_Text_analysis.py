import streamlit as st
from PIL import Image
import urllib
import pandas as pd
import dhlab as dh
import streamlit as st

st.set_page_config(page_title="Beatrice og Hamsun", page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items=None)

st.session_state.update(st.session_state)


#st.session_state.update(st.session_state)




#### CODE FOR WELCOME SCREEN


@st.cache_data()
def corpus(file):
    c = pd.read_excel(file)
    c['url'] = c.urn.apply(lambda x: f"https://www.nb.no/items/{x}")
    return c

litt_korpus = corpus("Hamsun_samlede.xlsx")
#st.write(litt_korpus.columns)
st.session_state['korpus'] = litt_korpus
st.session_state['dhlabid'] = [int(x) for x in litt_korpus.dhlabid]

st.title("Oversikt over korpuset - klikk på lenkene for å gå til bokhylla")
st.write("Velg en oppgave fra sidemenyen, finn konkordanser eller bygg en kollokasjon")
st.write("Sjekk ut https://dh.nb.no mer om DH-lab og tekstanalyse")

st.dataframe(
    litt_korpus[['url','title', 'authors','year']],
    column_config={
            "url": st.column_config.LinkColumn("URL")
    },
    hide_index=True
)

    
        