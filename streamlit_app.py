import streamlit as st

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

if __name__ == "__main__":
    main()
