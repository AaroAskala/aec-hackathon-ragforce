import time
import streamlit as st

# Basic setup
st.set_page_config(page_title="AugEng", page_icon=":flash:")

# Load
progress_text = "Opening search. Please wait."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(0.09)
my_bar.empty()

# Chat messaging window
with st.chat_message(name="AI"):
    st.write("Answer is written here")

question = st.chat_input(placeholder="Ask questions to find the text you need!", key=str, max_chars=500, disabled=False)

# Sidebar and Selected focus area
with st.sidebar:
    st.image(
        "https://www.sitowise.com/sites/default/files/styles/image_with_text_576x370_1x/public/2020-11/Sitowise_Haalarimerkit_Smart%20satama.png?itok=xMQFn05C",
        width=100)
    st.title("RAGforce :rocket:")
    st.subheader("Augmented search for engineers")
    st.divider()

add_selectbox = st.sidebar.selectbox(
    "Select Business Area",
    ("Infrastructure", "Buildings", "Digital Solutions")
)