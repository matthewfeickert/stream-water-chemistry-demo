import streamlit as st
import pandas as pd


def app():
    st.write("# Stream Water Chemistry Datasheet")

    edu_code = st.selectbox("EDU Code", ["KR_122084", "Other"])

    site_name = st.selectbox("Site Name", ["ISWS 405", "Other"])

    event_date = st.date_input("Date")

    observers = st.text_input("Observers")

    st.write("## Water Quality Meter")

    water_temperature = st.number_input(
        "Temperature (Celsius)",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        help="Temperature in Celsius",
    )

    dissolved_oxygen_density = st.number_input(
        "Dissovled Oxygen (mg/L)",
        min_value=0.0,
        max_value=10.0,
        step=0.1,
    )

    dissolved_oxygen_saturation = st.number_input(
        "Dissovled Oxygen (% Sat.)",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
    )

    conductivity = st.number_input(
        "Conductivity (μS/cm)",
        min_value=0,
        max_value=1000,
        step=1,
    )

    ph = st.number_input(
        "pH",
        min_value=0.0,
        max_value=100.0,
        step=0.01,
    )

    st.write("## Colorimeter")

    nitrate = st.number_input(
        "Nitrate (mg/L)",
        min_value=0.0,
        max_value=10.0,
        step=0.1,
        help="Hach TNT Nitrate-Nitrogen NO3-",
    )

    ammonia = st.number_input(
        "Ammonia (mg/L)",
        min_value=0.0,
        max_value=10.0,
        step=0.01,
    )

    react_phosphate = st.number_input(
        "React. Phosphate (mg/L)",
        min_value=0.0,
        max_value=10.0,
        step=0.01,
    )

    turbidity = st.number_input(
        "Turbidity (FAU)",
        min_value=0,
        max_value=100,
        step=1,
    )

    st.write("## Transparency Tube")

    visual_water_clarity = st.number_input(
        "Visual Water Clarity (cm)",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
    )

    data = {
        "PU_Gap_Code": [edu_code],
        "Reach_Name": [site_name],
        "Event_Date": [event_date],
        "SWC_Date": [event_date],
        "Water_Temperature": [water_temperature],
        "DO": [dissolved_oxygen_density],
        "DO_Saturation": [dissolved_oxygen_saturation],
        "Conductivity": [conductivity],
        "pH": [ph],
        "Nitrate": [nitrate],
        "Ammonia": [ammonia],
        "Orthophosphate": [react_phosphate],
        "Turbidity": [turbidity],
        "Visual_Water_Clarity": [visual_water_clarity],
    }

    df = pd.DataFrame(data)

    @st.cache
    def convert_df(df):
        return df.to_csv(index=False).encode("utf-8")

    st.download_button(
        f"Download {edu_code} Stream Water Chemistry Datasheet",
        convert_df(df),
        f"{edu_code}_stream_water_chemistry_datasheet.csv",
        "text/csv",
    )
