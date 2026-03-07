import streamlit as st
import requests
st.set_page_config(page_title="VoltSpectra AI", page_icon="⚡")

st.title("\t  Volt Spectra")

st.write("Circuit parameters for analysis :")

voltage = st.number_input("Voltage")
expected_voltage = st.number_input("Expected Voltage")
current = st.number_input("Current")
temperature = st.number_input("Temperature")
ripple = st.number_input("Ripple")

if st.button("Analyze Circuit"):

    data = {
        "voltage": voltage,
        "expected_voltage": expected_voltage,
        "current": current,
        "temperature": temperature,
        "ripple": ripple
    }

    response = requests.post(
        "http://localhost:9000/analyze-circuit",
        json=data
    )

    st.write("### Result")
    result = response.json()

st.subheader("Circuit Analysis Result")

status = result.get("status")
message = result.get("message")

if status == "Healthy":
    st.success(f"Status: {status}")
else:
    st.warning(f"Status: {status}")

st.write(message)