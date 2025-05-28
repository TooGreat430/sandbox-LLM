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
                st.write("#### 📘 Comic Info")
                st.write(f"• **Title**: {comic['title']}")
                st.write(f"• **Characters**: {comic['characters']}")
                st.write(f"• **Release Date**: {comic['year']}")
                st.write(f"• **Publisher**: {comic['publisher']}")
                st.write(f"• **Description**: {comic['issue_description']}")
                st.write(f"• **Price**: {comic['Price']}")
        else:
            st.write(msg["content"])

# Chat input from user
if prompt := st.chat_input("Type your Marvel comic question here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Searching the Marvel universe..."):
        st.session_state['chat'], response_message, comic_list = get_answer(st.session_state['chat'], prompt)
        if len(comic_list) == 0:
            st.session_state.messages.append({
                "role": "assistant",
                "content": response_message
            })
            st.chat_message("assistant").write(response_message)
        else:
            st.session_state.messages.append({
                "role": "assistant",
                "content": {
                    "message": response_message,
                    "comic_message": comic_list
                }
            })
            with st.chat_message("assistant"):
                st.write(response_message)
                for comic in comic_list:
                    st.write("#### 📘 Comic Info")
                    st.write(f"• **Title**: {comic['title']}")
                    st.write(f"• **Characters**: {comic['characters']}")
                    st.write(f"• **Release Date**: {comic['year']}")
                    st.write(f"• **Publisher**: {comic['publisher']}")
                    st.write(f"• **Description**: {comic['issue_description']}")
                    st.write(f"• **Price**: {comic['Price']}")
                
                    
