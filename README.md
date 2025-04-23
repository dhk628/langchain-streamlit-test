# Test Repository for LangChain and Streamlit

This is a repository to just test out the functionality of LangChain and Streamlit, and the code is mostly based on [this article](https://swethag04.medium.com/build-your-first-llm-powered-web-app-7af32b22bf94) with some changes to reflect changes in the LangChain API. As in the article, we will be creating a Streamlit app to get the top 5 baby names of a given gender and nationality.

## Setup

We will be using Gemini, so we first need to run the following to install the required packages:
```
pip install google-generativeai langchain streamlit
```
The Google Gemini API key is stored in the file `.env` in the root directory as `GOOGLE_API_KEY=[MY_KEY]`.

## LangChain

The file `langchain.py` contains the code to use the LLM within LangChain to generate the baby names. First, we load our Gemini API key using
```
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
```
We then load the model via 
```
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
)
```
The code uses Gemini 2.0 Flash, but this ca, of course, be replaced with any other Gemini model.

Inside the `generate_baby_names` function, we create the prompt template, then create an instance of the `RunnableSequence` class using
```
chain =  (
    prompt_template |
    llm
)
```
We can then get a response by simply calling `chain.invoke(input_data)`, where `input_data` is a dictionary containing the input gender and nationality.

## Streamlit

We create the Streamlit app in `main.py`. The user can choose the gender using `streamlit.pills` and can input the nationality using `streamlit.text_input`. On pressing the "Submit" button, the code calls the `generate_baby_names` function from `langchain_helper.py` and then displays the response.

## Using the app

The app can be accessed at https://localhost:8501 by running
```
streamlit run main.py
```