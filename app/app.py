import streamlit as st
import pandas as pd
import joblib


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Industrial Pump Maintenance Prediction",
    page_icon="⚙️",
    layout="centered"
)


# ============================================================
# LOAD MODEL
# ============================================================

import os
import joblib

# Get the folder containing app.py
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up, then into models
MODEL_PATH = os.path.join(
    APP_DIR,
    "..",
    "models",
    "decision_tree_model.pkl"
)

MODEL_PATH = os.path.abspath(MODEL_PATH)

model = joblib.load(MODEL_PATH)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("⚙️ Industrial Pump Maintenance Prediction")

st.write(
    """
    Enter the operating conditions of an industrial pump to
    predict whether maintenance is required according to the
    trained machine learning model.
    """
)


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("Pump Operating Conditions")

temperature = st.number_input(
    "Temperature",
    min_value=50.0,
    max_value=150.0,
    value=100.0
)

vibration = st.number_input(
    "Vibration",
    min_value=0.1,
    max_value=5.0,
    value=2.5
)

pressure = st.number_input(
    "Pressure",
    min_value=100.0,
    max_value=300.0,
    value=200.0
)

flow_rate = st.number_input(
    "Flow Rate",
    min_value=0.5,
    max_value=20.0,
    value=10.0
)

rpm = st.number_input(
    "RPM",
    min_value=1000.0,
    max_value=3000.0,
    value=2000.0
)

operational_hours = st.number_input(
    "Operational Hours",
    min_value=100.0,
    max_value=10000.0,
    value=5000.0
)


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("Predict Maintenance Requirement"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "Temperature": [temperature],
        "Vibration": [vibration],
        "Pressure": [pressure],
        "Flow_Rate": [flow_rate],
        "RPM": [rpm],
        "Operational_Hours": [operational_hours]
    })


    # ========================================================
    # PREDICTION
    # ========================================================

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    probability_maintenance = probability[1]


    # ========================================================
    # DISPLAY RESULT
    # ========================================================

    st.subheader("Prediction")

    if prediction == 1:

        st.warning(
            "⚠️ Maintenance Required"
        )

        st.write(
            f"Estimated probability of maintenance: "
            f"**{probability_maintenance:.2%}**"
        )

    else:

        st.success(
            "✅ No Maintenance Required"
        )

        st.write(
            f"Estimated probability of maintenance: "
            f"**{probability_maintenance:.2%}**"
        )


    # ========================================================
    # SHOW INPUTS
    # ========================================================

    st.subheader("Input Values")

    st.dataframe(
        input_data,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Educational prototype — Industrial Pump Maintenance Prediction"
)