import streamlit as st
import requests

# 1. Page Configuration
st.set_page_config(page_title="CodePRO LK ChatBot", page_icon="🧠")
st.title("🧠 CodePRO LK AI Assistant")
st.markdown("Ask anything about CodePRO LK and technology education.")

# 2. Initialize Chat History in Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Sidebar for Session Configuration
with st.sidebar:
    st.header("Settings")
    session_id = st.text_input("Session ID", value="101")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# 4. Display Chat Messages from History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Chat Input
if prompt := st.chat_input("What is CodePRO LK?"):
    # Display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 6. Call the FastAPI Backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Replace with your actual FastAPI URL
                api_url = "http://localhost:8000/chat"
                payload = {
                    "input": prompt,
                    "session_id": session_id
                }
                
                response = requests.post(api_url, json=payload)
                
                if response.status_code == 200:
                    answer = response.json().get("answer", "No answer found.")
                    st.markdown(answer)
                    # Add to history
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            
            except requests.exceptions.ConnectionError:
                st.error("Could not connect to the FastAPI server. Make sure app.py is running.")