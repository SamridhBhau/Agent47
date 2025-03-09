import streamlit as st

if __name__=="__main__":
    selected = st.selectbox("Select between Text and Audio", ["Text", "Audio"])
    
    if selected == "Text":
        st.text_input("Ask anything")
    elif selected == "Audio":
        audio_input = st.audio_input("Audio");

    st.file_uploader("Select image to upload", type=["jpeg", "png"])

     
