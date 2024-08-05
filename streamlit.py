import streamlit as st
from groq import Groq


user_input = st.chat_input('start typing')

if not user_input: 
    st.title('Hello there 👋')


model_choice = st.sidebar.selectbox('Choose Model', 
('LLaMA3 8b', 'LLaMA3 70b', 'Mixtral 8x7b', 'Gemma 7b'
'gemma2 9b it', "llama-3.1-8b-instant"
))

model_map = {
    'LLaMA3 8b': 'llama3-8b-8192',
    'LLaMA3 70b': 'llama3-70b-8192',
    'Mixtral 8x7b': 'mixtral-8x7b-32768',
    'Gemma 7b': 'gemma-7b-it',
    "gemma2 9b":"gemma2-9b-it",
    "llama-3.1-8b-instant":'llama-3.1-8b-instant'
}

model = model_map.get(model_choice, 'llama-3.1-8b-instant')

def get_chat_completion(user_input, model):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input or 'introduce your model',
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

response = get_chat_completion(user_input, model)
st.write(response)