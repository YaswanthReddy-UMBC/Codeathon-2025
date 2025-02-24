import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

incident_types = ['Physical Abuse', 'Neglect', 'Emotional Abuse']
st.title("Child Protection Incident Map")

# --- Show the Map ---
st.subheader("Incident Map")

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=37.7749,
        longitude=-122.4194,
        zoom=11,
        pitch=50,),))

# --- Report an Incident (Simplified) ---

st.subheader("Report an Incident")
with st.form("incident_report"):
    report_type = st.selectbox("Incident Type", incident_types)
    report_age = st.number_input("Victim's Age", min_value=0, max_value=18, value=0)
    submitted = st.form_submit_button("Submit Report")

    if submitted:
        st.success("Incident reported.")

st.markdown("---")
st.markdown(
    "<small>Disclaimer: This is a simplified example.</small>",
    unsafe_allow_html=True,
)
