# This is the corpus on which the original RAG model was based on. The text bits have been generated with the help of Chat GPT.
corpus_of_documents = [

    "Python is Interpreted: Python is an interpreted language, meaning that the code is executed line by line by an interpreter, rather than compiled into machine code.",
    "Python is High-level: Python is a high-level programming language, which means it abstracts away the complexities of the machine language, making it easier to write and understand code.",
    "Python is Dynamically Typed: Python is dynamically typed, which means that you don't need to declare the type of a variable when you create one. The interpreter automatically assigns the appropriate type to the variable based on its value.",
    "Python is Object-Oriented: Python supports object-oriented programming (OOP) principles, allowing you to create classes and objects, encapsulate data, and implement inheritance and polymorphism.",
    "Python has a Large Standard Library: Python comes with a large standard library that provides support for many common programming tasks, such as file I/O, networking, and web development, right out of the box.",
    "Python is used for Web Development: Python is widely used for web development, with popular frameworks like Django and Flask that make it easy to build web applications.",
    "Python is used for Data Analysis and Machine Learning: Python has become the de facto language for data analysis and machine learning, with libraries like NumPy, pandas, and scikit-learn that make it easy to work with large datasets and build machine learning models.",
    "Python is used for Automation: Python is often used for automation tasks, such as scripting repetitive tasks, building bots, or controlling hardware devices.",
    "Python is Cross-platform: Python is a cross-platform language, meaning that it runs on all major operating systems, including Windows, macOS, and Linux.",
    "Python is Open Source: Python is open source and has a large and active community of developers who contribute to its development and maintenance."
    "Start with the Basics: Begin by learning the basics: variables, data types, and control structures like loops and conditionals.",
    "Practice Regularly: Practice coding regularly to reinforce your skills and build confidence.",
    "Use Python Documentation: Refer to the official Python documentation and online resources for help and examples.",
    "Leverage Libraries: Take advantage of Python's extensive library ecosystem to simplify your coding tasks.",
    "Readability Matters: Write clean and readable code by following Python's style guide (PEP 8) and using meaningful variable names.",
    "Debugging Tools: Learn to use debugging tools like print() statements and Python's built-in debugger (pdb) to identify and fix errors in your code.",
    "Version Control: Use version control systems like Git to manage your code and collaborate with others effectively.",
    "Stay Organized: Organize your code into functions and modules to improve reusability and maintainability.",
    "Test Your Code: Write unit tests to verify that your code behaves as expected and catches bugs early.",
    "Keep Learning: Python is vast and constantly evolving, so keep learning new concepts, libraries, and best practices."
    
    ]

# These two functions are from the original tiny RAG model that takes the corpus and user input, splits them into pieces and compares them with each other. The latter function does the comparison and returns the one with most similarities.
def jaccard_similarity(query, document):
    query = query.lower().split(" ")
    document = document.lower().split(" ")
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = jaccard_similarity(user_input, doc)
        similarities.append(similarity)
    return corpus[similarities.index(max(similarities))]

# These imports are related to the connection between Streamlit and Ollama. 
import streamlit as st
from langchain_community.llms import Ollama
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks import StreamlitCallbackHandler
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler

# The name of the chatbot.
st.title("Pyt-Bot")

# The checkbox to use the internet for the search.
search_internet = st.checkbox("Check internet?", value=False, key="internet")
# The text box used to get the user input that is then passed on to the language model.
user_input = st.text_input("Ask your question here and click enter:", value="", key="prompt")

relevant_document = return_response(user_input, corpus_of_documents)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# If the user input is not empty, start the process.
if user_input!="":
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # If the internet box is not ticked, use ollama to get the response.
    response = ""
    if not search_internet:
        llm = Ollama(model="llama2:latest") # 👈 stef default
        response = llm.predict(user_input)
        
    else:
        llm = Ollama(
            model="llama2:latest", 
            callback_manager=CallbackManager([FinalStreamingStdOutCallbackHandler()])
        )
        agent = initialize_agent(
            load_tools(["ddg-search"])
            ,llm 
            ,agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
            ,verbose=True
            ,handle_parsing_errors=True
        )
        response = agent.run(user_input, callbacks=[StreamlitCallbackHandler(st.container())])
        # BUG 2023Nov05 can spiral Q&A: https://github.com/langchain-ai/langchain/issues/12892
        # to get out, refresh browser page
    
    # Provide the answer with the bot role and response from the language model or the internet as response.
    st.session_state.messages.append({"role": "bot", "content": response})
    
    st.markdown(response)