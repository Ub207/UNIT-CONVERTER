import streamlit as st

# Streamlit UI
st.title("🔄 Unit Converter")
st.write("Convert between different units of length, weight, and temperature.")

# Conversion Categories
category = st.selectbox("Choose a category:", ["Length", "Weight", "Temperature"])

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32

# User Inputs
value = st.number_input("Enter value:", min_value=0.0, step=0.1)

if category == "Length":
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet", "Inches"])
    result = convert_length(value, from_unit, to_unit)

elif category == "Weight":
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds", "Ounces"])
    result = convert_weight(value, from_unit, to_unit)

elif category == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)

# Display Result
if st.button("Convert 🔄"):
    st.success(f"Converted Value: {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("📏 *Simple and easy unit conversion!*")

