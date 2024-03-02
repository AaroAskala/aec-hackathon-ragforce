import streamlit as st

def switch_page(page_name: str):
    """
    Switch page programmatically in a multipage app

    Args:
        page_name (str): Target page name
    """
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages

    def standardize_name(name: str) -> str:
        return name.lower().replace("_", " ")

    page_name = standardize_name(page_name)

    pages = get_pages("streamlit_app.py")  # OR whatever your main page is called

    for page_hash, config in pages.items():
        if standardize_name(config["page_name"]) == page_name:
            raise RerunException(
                RerunData(
                    page_script_hash=page_hash,
                    page_name=page_name,
                )
            )

    page_names = [standardize_name(config["page_name"]) for config in pages.values()]

    raise ValueError(f"Could not find page {page_name}. Must be one of {page_names}")



#css for Start window
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

buttonstextMargins = st.markdown("""
        <style>
            .st-emotion-cache-1y4p8pa {
                margin: 0px;
                padding: 0px 0px 0px 0px;
                max-width: 100rem;

            }
        </style>
        """, unsafe_allow_html=True)

textStyleMainWindow = """
    <style>
    .st-emotion-cache-10trblm {
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 65px;
        color: #e6e6e6;
        margin: 0px;
        padding: 0px;
    }
    </style>"""


st.write("#")
st.title("Select the wanted use case")

st.markdown(textStyleMainWindow, unsafe_allow_html=True)


st.write("#")
st.write("#")
st.write("#")


col1, col2, col3 = st.columns(3)

m = st.markdown("""
    <style>
    .st-emotion-cache-1r6slb0{
        display: flex;
        justify-content: space-around;
        align-items: center;

    }
    
    .st-emotion-cache-ocqkz7{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 110px 30px 0px 30px;
        gap: 0px;
        
    }
    
    div.stButton > button:first-child {
        width:250px;
        height:120px;
        border-width:1px;
        border-color: #e6e6e6;
        boarder-radius: 55px;
        background-color: #003856;
        transition: background-color 0.5s;
        box-shadow: 30px 20px 40px -9px rgba(17,17,17,0.51);
    }
    
    .st-emotion-cache-10fz3ls p {
        font-size:21px;
        text-shadow: 9px 5px 7px rgba(17,17,17,0.70);
        color: #e6e6e6;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #35b98b; 
    }
    </style>""", unsafe_allow_html=True)


def goToPage(page_name):
    st.query_params(page=page_name)


with col1:
    if st.button("Buildings", key="buildings", type="primary"):
        switch_page("Bot")
with col2:
    if st.button("Infrastructure",key="Infrastructure", type="primary"):
        switch_page("Bot")
with col3:
    if st.button("Digital Solutions",key="Digital Solutions", type="primary"):
        switch_page("Bot")
