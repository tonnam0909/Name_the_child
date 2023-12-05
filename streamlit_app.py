import streamlit as st
import openai  # Make sure to install the 'openai' library using: pip install openai

# Function to generate a name using OpenAI API
def generate_name(gender, characteristic, first_letter, language, api_key):
    # Set OpenAI API key
    openai.api_key = api_key

    # Call OpenAI API to generate a name based on the provided parameters
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the appropriate engine
        prompt=f"Generate a {gender.lower()} name that is {characteristic.lower()} and starts with {first_letter.lower()} in {language.lower()}",
        max_tokens=50  # Adjust as needed
    )

    generated_name = response.choices[0].text.strip()
    return generated_name

# Streamlit app
def main():
    st.title("Name Generator App")

    # User input
    gender = st.selectbox("Select gender", ["Male", "Female"])
    characteristic = st.text_input("Enter a characteristic (e.g., Brave, Intelligent)")
    first_letter = st.text_input("Enter the first letter of the name")
    language = st.selectbox("Select language", ["English", "Italian", "Spanish"])

    # Slider for API key
    api_key = st.text_input("Enter your OpenAI API key", type="password")
    
    # Generate and display the name
    if st.button("Generate Name"):
        generated_name = generate_name(gender, characteristic, first_letter, language, api_key)
        st.success(f"The generated name is: {generated_name}")

if __name__ == "__main__":
    main()
