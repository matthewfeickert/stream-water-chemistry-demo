import streamlit as st
import pandas as pd


def app():
    st.write("# 20-Jab Effort Datasheet")

    edu_code = st.selectbox("EDU Code", ["KR_122084", "Other"])

    site_name = st.selectbox("Site Name", ["ISWS 405", "Other"])

    stream_name = st.selectbox("Stream Name", ["East Fork Shoal Creek", "Other"])

    event_date = st.date_input("Date")

    collectors = st.text_input("Collectors")

    data = {
        "Jab Number": [None],
        "Habitat Type": [None],
        "Flow": [None],
        "Substrate": [None],
    }

    df = pd.DataFrame(columns=list(data.keys()))
    # df = pd.DataFrame(data)

    for idx in range(1, 21):
        with st.form(f"form_{idx}"):
            habitat_type = st.selectbox("Habitat Type", ["Ri", "Ru", "P", "G"])
            flow = st.selectbox("Flow", ["Fast", "Slow"])
            substrate = st.selectbox(
                "Substrate", ["F", "C", "PD", "AqV", "STV", "TR", "DJ"]
            )

            # Every form must have a submit button.
            submitted = st.form_submit_button("Submit")
            if submitted:
                inputs = {
                    "Jab Number": [idx],
                    "Habitat Type": [habitat_type],
                    "Flow": [flow],
                    "Substrate": [substrate],
                }
                df_inputs = pd.DataFrame(inputs)
                # st.write("slider", slider_val, "checkbox", checkbox_val)
                df = df.concat(df_inputs, ignore_index=True)
                st.dataframe(df)

    # st.dataframe(df)
