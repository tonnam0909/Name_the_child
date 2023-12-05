import streamlit as st
import openai
import pandas as pd
st.cache_data.clear()

if "openai_api_key" not in st.session_state:
    st.session_state.openai_api_key = ""

#openai.api_key = st.session_state.openai_api_key

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

#user_api_key = st.sidebar.text_input("OpenAI API key", type="password")
#client = openai.OpenAI(api_key=user_api_key)

def generate_name_recommendation(gender, characteristics, first_letter, language):
    # Customize the prompt based on your requirements
    prompt = f"Give me five {gender} names that means {characteristics} that starts with {first_letter} in {language} and tell me the origin of each name."

    # Call OpenAI API for recommendation
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        top_p=0.7,
        max_tokens=450,
        messages=[
            {"role": "system", "content": "You are a name recommendation bot. You will help users find the most suitable name for the user from the information given by the user."},
            {"role": "user", "content": f"You will help users find the best names that is the most suitable from the given information:{prompt}."},
        ]
    )
    
    return response.choices[0].message.content

st.markdown("<div style='text-align: center;'><h2 style='font-size: 2rem;'>NAME YOUR CHILD!!!</h2></div>", unsafe_allow_html=True)

# Uncomment the following lines to enable the API key input form


# User input
gender = st.selectbox("Select gender", ["Male", "Female"])
characteristics = st.text_input("Enter characteristics (e.g., Brave, Intelligent)")
first_letter = st.text_input("Enter the first letter of the name")
language = st.selectbox("Select language", ["English", "Italian", "Spanish"])

# Generate recommendation
if st.button("Generate Name"):
    if gender and characteristics and first_letter and language:
        recommendation = generate_name_recommendation(
            gender, characteristics, first_letter, language
        )
        st.success(f"Recommended Name: {recommendation}")
    else:
        st.warning("Please fill in all fields.")