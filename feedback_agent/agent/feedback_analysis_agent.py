from autogen import ConversableAgent
from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.categorization_tool import categorize_feedback
from feedback_agent.tools.keyword_extraction_tool import extract_keywords


LLM_CONFIG = {
    "model": "llama3.1:8b",
    "client_host": "127.0.0.1:11434",
    "api_type": "ollama",
    "num_predict": -1,
    "repeat_penalty": 1.1,
    "seed": 42,
    "stream": False,
    "temperature": 1,
    "top_k": 50,
    "top_p": 0.8,
    "native_tool_calls": False,
    "cache_seed": None
}

def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="You are a helpful AI assistant. "
                      "You can perform sentiment analysis on customer feedback. "
                      "You can read customer feedback using the feedback_reader tool. It will return a list of feedback, that consists of id, text, and source. "
                      "Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. "
                      #"You can also categorize the feedback into themes using the categorization tool. "
                      # "You can also extract keywords from the feedback using the keyword_extraction tool. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
    agent.register_for_llm(name="sentiment_analysis", description="Analyze the sentiment of a customer feedback")(analyze_sentiment)
    # agent.register_for_llm(name="categorization", description="Categorize feedback into themes")(categorize_feedback)
    # agent.register_for_llm(name="keyword_extraction", description="Extract keywords from a customer feedback")(extract_keywords)

    return agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="feedback_reader")(query_feedback)
    user_proxy.register_for_execution(name="sentiment_analysis")(analyze_sentiment)
    # user_proxy.register_for_execution(name="categorization")(categorize_feedback)
    # user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
    return user_proxy


def main():
    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()
    user_proxy.initiate_chat(
        feedback_analysis_agent, 
        message="""
                1. Read feedback from the feedback store, using the feedback_reader tool.
                2. For each feedback item, analyze the sentiment using the sentiment_analysis tool.
                3. Create a JSON object that contains the feedback id and the analyzed sentiment.
                Example:
                [
                    {"id": "1", "sentiment": "positive"},
                    {"id": "2", "sentiment": "negative"},
                    {"id": "3", "sentiment": "neutral"}
                ]
                4. Return the JSON object.
                """,
                cache=None
    )

if __name__ == "__main__":
    main()
