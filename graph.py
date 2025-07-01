from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from csv_analysis import analyze_csv
from vector_search import vector_search
from rewriter import rewrite_ad_text
from langgraph.checkpoint.memory import InMemorySaver

graph = StateGraph()
checkpointer = InMemorySaver()

graph.add_node("AnalyzeCSV", RunnableLambda(analyze_csv))
graph.add_node("SearchBlogs", RunnableLambda(vector_search))
graph.add_node("RewriteAd", RunnableLambda(rewrite_ad_text))
graph.add_node("FeedbackMemory", RunnableLambda(feedback_memory))
graph.add_node("Evaluate", RunnableLambda(evaluate_output))

graph.set_entry_point("AnalyzeCSV")
graph.add_edge("AnalyzeCSV", "SearchBlogs")
graph.add_edge("SearchBlogs", "RewriteAd")
graph.add_edge("RewriteAd", "FeedbackMemory")
graph.add_edge("FeedbackMemory", "Evaluate")
graph.add_edge("Evaluate", END)

final_graph = graph.compile(checkpointer=checkpointer)
