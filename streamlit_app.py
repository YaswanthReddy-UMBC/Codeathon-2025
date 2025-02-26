%%writefile app.py
# --- Importing Libraries ------ (These are used to simplify the code.)
import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np

incident_types = ['Physical Abuse', 'Neglect', 'Emotional Abuse', 'War Oprhaned Kids','Bullying', 'Child Trafficking', 'Sexual Abuse','Child labour', 'Other']
st.title("Speak Up For Kids")
st.subheader('Child Violence Reporting Application.')

# --- The below code is to Show the Map ---
st.subheader("Incident Map")

st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',initial_view_state=pdk.ViewState(latitude=37.7749,
        longitude=-122.4194,zoom=11,pitch=50,),))

# --- Report an Incident ---

st.subheader("Report an Incident") #-- This line is a subheading that shows to report an incident
with st.form("incident_report"):
    report_type = st.selectbox("Incident Type", incident_types) #-- This gives the user options to select the incident types
    report_age = st.number_input("Victim's Age", min_value=0, max_value=18, value=0) #-- This one gives the user to select the victim's age
    report_gender = st.selectbox("Victim's Gender", ["Male", "Female", "Other"]) #-- This one gives the user to select the victim's gender
    report_address = st.text_input("Victim's Address") #-- This one gives the user to enter the victim's address
    report_location = st.text_input("Location of the Incident") #-- This one gives the user to enter the location of the incident
    report_description = st.text_area("Description of the Incident") #-- This one gives the user to enter the description of the incident
    report_date = st.date_input("Date of the Incident") #-- This one gives the user to enter the date of the incident
    report_time = st.time_input("Time of the Incident") #-- This one gives the user to enter the time of the incident
    report_phone = st.text_input("Contact Information") #-- This one gives the user to enter the contact information
    submitted = st.form_submit_button("Submit Report") #--This one is to submit the report. 

    if submitted:
        st.success("Incident reported.")

st.markdown("---")
st.markdown(
    "<small>Disclaimer: This application should be connected to database for the authorities to see the report`.</small>",
    unsafe_allow_html=True,
)
