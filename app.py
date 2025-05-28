import streamlit as st
from functions import initialize_model, get_answer


st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 42% !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Inisialisasi session chat
if "chat" not in st.session_state:
    st.session_state["chat"] = initialize_model().start_chat()

st.set_page_config(page_title="Marvel Comic Search", layout="wide")

# Header
st.title("Marvel Comic Con 2025")
st.markdown("Welcome, true believer! Dive into the Marvel Universe and discover epic comics, legendary heroes, and unforgettable stories 🦸‍♂️🦸‍♀️")
st.success(
    "Search Your Marvel Comic Here!",
    icon="✨",
)

# Divider
st.divider()

# Chat history display
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hello Marvel Fans! Welcome To Comic Con! What can I help you find today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if isinstance(msg["content"], dict):
            st.write(msg["content"]["message"])
            for product in msg["content"]["comic_message"]:
                st.markdown(f"• **Series**: {comic.get('series_name', 'N/A')}")
                st.markdown(f"• **Issue Title**: {comic.get('issue_title', 'N/A')}")
                st.markdown(f"• **Release Date**: {comic.get('release_date', 'N/A')}")
                st.markdown(f"• **publisher**: {comic.get('writer', 'N/A')}")
                st.markdown(f"• **Price**: {comic.get('price', 'N/A')}")
        else:
            st.write(msg["content"])
        st.markdown(msg["content"])

# Chat input from user
if prompt := st.chat_input("Type your Marvel comic question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Searching the Marvel universe..."):
        try:
            st.session_state['chat'], response_message, comic_list = get_answer(st.session_state['chat'], prompt)

            if comic_list:
                # Simpan ke message log
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response_message
                })
                with st.chat_message("assistant"):
                    st.write(response_message)
                    for comic in comic_list:
                        st.markdown("#### 📘 Comic Info")
                        st.markdown(f"• **Series**: {comic.get('series_name', 'N/A')}")
                        st.markdown(f"• **Issue Title**: {comic.get('issue_title', 'N/A')}")
                        st.markdown(f"• **Release Date**: {comic.get('release_date', 'N/A')}")
                        st.markdown(f"• **publisher**: {comic.get('writer', 'N/A')}")
                        st.markdown(f"• **Price**: {comic.get('price', 'N/A')}")
                        st.divider()
            else:
                st.session_state.messages.append({
                    "role": "assistant",
                    "comic_message": response_message
                })
                st.chat_message("assistant").write(response_message)
                    

        except Exception as e:
            st.error(f"Error occurred: {e}")
