from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0.4)

def rewrite_ad_text(state):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Rewrite the ad copy in a {tone} tone, optimized for {platform}."),
        ("human", "{text}")
    ])
    chain = prompt | llm
    result = chain.invoke({
        "tone": state["tone"],
        "platform": state["platform"],
        "text": state["original_ad"]
    })
    state["rewritten_ad"] = result.content
    return state
