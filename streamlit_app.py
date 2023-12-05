import streamlit as st
import openai
# Uncomment the following lines to enable the API key input form
# Initialize
st.cache_data.clear()

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

openai.api_key = st.session_state.openai_api_key

if "text_error" not in st.session_state:
    st.session_state.text_error = None

if "text" not in st.session_state:
    st.session_state.text = None

if "n_requests" not in st.session_state:
    st.session_state.n_requests = 0

with st.sidebar:
    api_key_form = st.form(key="api_key_form")
    openai_api_key = api_key_form.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    api_key_form_submitted = api_key_form.form_submit_button("Submit")

    if api_key_form_submitted:
        st.session_state.openai_api_key = openai_api_key
        openai.api_key = st.session_state.openai_api_key
        st.success("Your OpenAI API key was saved successfully!")

# Function to generate a fictional name
def generate_name(gender, characteristic, first_letter, language):
    # Replace this with the actual OpenAI API call once available
    # For now, a fictional name is generated based on the provided parameters
    name = f"{first_letter.upper()}{characteristic.capitalize()}"

    return name

# Streamlit app
def main():
    st.title("Name Generator App")

    # User input
    gender = st.selectbox("Select gender", ["Male", "Female"])
    characteristic = st.text_input("Enter a characteristic (e.g., Brave, Intelligent)")
    first_letter = st.text_input("Enter the first letter of the name")
    language = st.selectbox("Select language", ["English", "Italian", "Spanish"])

    # Generate and display the name
    if st.button("Generate Name"):
        generated_name = generate_name(gender, characteristic, first_letter, language)
        st.success(f"The generated name is: {generated_name}")