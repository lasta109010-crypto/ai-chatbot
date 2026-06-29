import streamlit as st
from openai import OpenAI

client = OpenAI()

# your title
st.set_page_config(
    page_title = "AI Chat Bot" , 
    layout = "centered"

)

st.title("AI Chat Bot")

# create the notebook/the brain

if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Ask AnyThing")

#display old messages


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


#save user messages 
if prompt:
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)
#as open ai response
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=st.session_state.messages
    )
#save and display
    assistant_reply = response.output_text

    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_reply}
    )

    with st.chat_message("assistant"):
        st.write(assistant_reply)




