import time
import streamlit as st

# Basic setup
st.set_page_config(page_title="AugEng", page_icon=":flash:")


st.header("RAGforce :rocket:")
st.subheader("Augmented search for engineers")
st.divider()

st.markdown("""
    <style>
    .st-emotion-cache-1y4p8pa h2,
    .st-emotion-cache-1y4p8pa h3{
        color: #e6e6e6;
    }
    
    .st-emotion-cache-1y4p8pa{
        padding: 30px 0px 0px 50px;
        max-width: 1500px;
        
    }
    .st-emotion-cache-1y4p8pa{
        max-width: 1500px;
    }
    .st-bb, .st-co{
        background-color:#003856;
        color: #e6e6e6;
    }
    .st-emotion-cache-sy3zga{
        color: #e6e6e6;
    }
    </style>""", unsafe_allow_html=True)

# Sidebar and Selected focus area
with st.sidebar:
    add_selectbox = st.sidebar.selectbox(
        "Select Business Area",
        ("Infrastructure", "Buildings", "Digital Solutions")
    )
    on = st.toggle('CO2 calculation methods')
    st.toggle('Legislation')
    st.toggle('Design guidelines')
    st.toggle('Technical specification')
    st.toggle('QA guidelines')

#client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#if prompt := st.chat_input("Ask your question"):
 #   st.session_state.messages.append({"role": "user", "content": prompt})
  #  with st.chat_message("user"):
   #     st.markdown(prompt)

    #with st.chat_message("assistant"):
        #stream = client.chat.completions.create(
            #model=st.session_state["openai_model"],
            #messages=[
                #{"role": m["role"], "content": m["content"]}
                #for m in st.session_state.messages
           # ],
            #stream=True,
      #  )
       # with st.spinner('Searching for answers...   '):
        #    time.sleep(2)
       # response = st.write_stream(stream)
   # st.session_state.messages.append({"role": "assistant", "content": response})


mainWindow = st.markdown("""
        <style>
               .main {
                    background-color: #003856;
                }
        </style>
        """, unsafe_allow_html=True)

header = st.markdown("""
        <style>
               .st-emotion-cache-18ni7ap {
                    background-color: #003856;
                    color: #e6e6e6;
                }
        </style>
        """, unsafe_allow_html=True)


sideBar = st.markdown("""
        <style>
            .st-emotion-cache-vk3wp9{
                min-width:300px;
                max-width:300px;
                transition:0ms;
        }
            .st-emotion-cache-6qob1r {
                background-color: #83c9f0;
                width:300px;
            }
        </style>
        """, unsafe_allow_html=True)


mainWindowMargins = st.markdown("""
        <style>
            .st-emotion-cache-uf99v8 {
                margin: 0px;
                padding: 0px;
            }
        </style>
        """, unsafe_allow_html=True)

