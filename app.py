
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

##  To get response from LLAma 2 model

def getLLamaresponse(topic,no_words,role):

    ### LLama2 model
    llm=CTransformers(model='TheBloke/openchat-3.5-0106-GGUF',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ### Template of the prompt

    template="""Act as  {role} tell me about {topic} within {no_words} words."""
    
    prompt=PromptTemplate(input_variables=["role","topic",'no_words'],
                          template=template)
    
    ## Getting the response from the LLama 2 model
    response=llm(prompt.format(role=role,topic=topic,no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="OpenChat",
                    page_icon='🕘',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Open Chat 🕘")

input_text=st.text_input("Ask me anything")

## creating more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('asking for ',
                            ('Student','Agency','Business owner'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(role,no_words,topic))