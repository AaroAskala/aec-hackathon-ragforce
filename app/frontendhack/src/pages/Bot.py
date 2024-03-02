import time
import streamlit as st

#Basic setup
st.set_page_config(page_title="AugEng", page_icon=":flash:")

# Sidebar and Selected focus area
with st.sidebar:
    st.title("RAGforce :rocket:")
    st.subheader("Augmented search for engineers")
    st.divider()
    add_selectbox = st.sidebar.selectbox(
    "Select Business Area",
    ("Infrastructure", "Buildings", "Digital Solutions")    
)
    on = st.toggle('CO2 calculation methods')
    st.toggle('Legislation')
    st.toggle('Design guidelines')
    st.toggle('Technical specification')
    st.toggle('QA guidelines')

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your question"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"], 
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        with st.spinner('Searching for answers...   '):    
            time.sleep(2)
        response = st.write_stream(stream)  
    st.session_state.messages.append({"role": "assistant", "content": response})
          