import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Function to refresh and ensure 'data' folder exists
def refresh():
    if not os.path.exists('data'):
        os.makedirs('data')  # Create the 'data' folder if it doesn't exist
    data = os.listdir(r"/home/greninja07/Downloads/NCERT_HELPER/ncert_helper_main/ui/data")
    return data

with st.sidebar:
    st.title("Upload Files to Add")
    
    # Ensure the 'data' folder exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    uploaded_file = st.file_uploader("Choose a file", accept_multiple_files=False)
    data = refresh()
    
    if uploaded_file is not None:
        with open(os.path.join('data', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getvalue())
        st.success(f"File '{uploaded_file.name}' uploaded successfully.")
    
    st.button('Refresh', on_click=refresh)
    
    st.title("Available Files")
    for filename in data:
        st.write(filename)

# Load environment variables
load_dotenv()
api_host = os.environ.get("PATHWAY_HOST", "0.0.0.0")
api_port = int(os.environ.get("PATHWAY_PORT", 8000))

# Streamlit UI elements
st.title("NCERT_HELP_PROVIDER")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Describe your task to get related weather conditions"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    url = f"http://{api_host}:{api_port}/v1/pw_ai_answer"
    data = {"prompt": prompt}
    headers = {
        "Accept": "/",
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        response = response.json()
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error(
            f"Failed to send data to the API. Status code: {response.status_code},\
                  Response: {response.text}"
        )