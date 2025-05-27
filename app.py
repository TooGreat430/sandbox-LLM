import streamlit as st
from functions import initialize_model, get_answer

# Inisialisasi session chat
if "chat" not in st.session_state:
    st.session_state["chat"] = initialize_model().start_chat()
    st.session_state["chat_history_list"] = []

st.set_page_config(page_title="Marvel Comic Search", layout="wide")

# Header
st.title("Marvel Comic Con 2025")
st.markdown("Welcome, true believer! Dive into the Marvel Universe and discover epic comics, legendary heroes, and unforgettable stories 🦸‍♂️🦸‍♀️")

# Divider
st.divider()

# Chat history display
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi! I’m your Marvel Comic assistant. What can I help you find today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input from user
if prompt := st.chat_input("Type your Marvel comic question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Searching the Marvel universe..."):
        try:
            response_message, comic_list, chat_df = get_answer(prompt)

            if comic_list:
                # Simpan ke message log
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response_message
                })
                with st.chat_message("assistant"):
                    st.markdown(response_message)
                    for comic in comic_list:
                        st.markdown("#### 📘 Comic Info")
                        st.markdown(f"• **Series**: {comic.get('series_name', 'N/A')}")
                        st.markdown(f"• **Issue Title**: {comic.get('issue_title', 'N/A')}")
                        st.markdown(f"• **Release Date**: {comic.get('release_date', 'N/A')}")
                        st.markdown(f"• **Writer**: {comic.get('writer', 'N/A')}")
                        st.markdown(f"• **Price**: {comic.get('price', 'N/A')}")
                        st.divider()
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response_message
                })
                with st.chat_message("assistant"):
                    st.markdown(response_message)

        except Exception as e:
            st.error(f"Error occurred: {e}")
