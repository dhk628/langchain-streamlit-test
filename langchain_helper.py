import os
# from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

# load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=GOOGLE_API_KEY,
)

def generate_baby_names(gender:str, nationality:str) -> list[str]:
    """
    Generate a list of 5 baby names

    Parameters:
    gender (str): gender of baby
    nationailty (str) : nationailty of baby

    Returns:
    list: list of baby names
    """
    prompt_template = PromptTemplate(
        input_variables=['gender', 'nationality'],
        template="""I want to find a name for a {nationality} {gender} baby. Suggest top 5 popular names for the baby.
                    Return it as a comma separated list."""
    )

    chain =  (
        prompt_template |
        llm
    )

    input_data = {
        'gender': gender,
        'nationality': nationality
    }

    response = chain.invoke(input_data)

    names = response.content.strip().split('\n')[-1].split(',')

    return names

if __name__ == "__main__":
    print(generate_baby_names("girl", "Japanese"))
