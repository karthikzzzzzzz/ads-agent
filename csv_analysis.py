from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4", temperature=0.3)

def analyze_csv(state):
    # Read the uploaded CSV as text
    with open(state["csv_path"], "r", encoding="utf-8") as file:
        csv_content = file.read()

    # Prompt the LLM for analysis
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a digital marketing analyst. Analyze the ad performance data in the CSV and provide concise insights and suggestions for improvement."),
        ("human", "{csv_text}")
    ])
    chain = prompt | llm

    result = chain.invoke({"csv_text": csv_content})
    state["insights"] = result.content
    return state
