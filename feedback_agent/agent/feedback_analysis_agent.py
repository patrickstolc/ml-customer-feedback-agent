import argparse
from autogen import ConversableAgent
from feedback_agent.tools.feedback_reader_tool import query_feedback
from feedback_agent.tools.sentiment_analysis_tool import analyze_sentiment
from feedback_agent.tools.categorization_tool import categorize_feedback
from feedback_agent.tools.keyword_extraction_tool import extract_keywords
from feedback_agent.config import LLM_CONFIG

PROMPT_SENTIMENT_ANALYSIS = """
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
"""

PROMPT_KEYWORD_EXTRACTION = """
1. Read feedback from the feedback store, using the feedback_reader tool.
2. For each feedback item, extract the keywords using the keyword_extraction tool.
3. Create a JSON object that contains the feedback id and the extracted keywords.
Example:
[
    {"id": "1", "keywords": ["good", "service", "recommend"]},
    {"id": "2", "keywords": ["bad", "experience", "not recommended"]},
    {"id": "3", "keywords": ["neutral", "ok", "average"]}
]
4. Return the JSON object.
"""

PROMPT_CATEGORIZATION = """
1. Read feedback from the feedback store, using the feedback_reader tool.
2. For each feedback item, categorize the feedback into themes using the categorization tool.
3. Create a JSON object that contains the feedback id and the categorized theme.
Example:
[
    {"id": "1", "theme": "product"},
    {"id": "2", "theme": "service"},
    {"id": "3", "theme": "other"}
]
4. Return the JSON object.
"""

PROMPT_CATEGORIZE_AND_EXTRACT_KEYWORDS = """
1. Read feedback from the feedback store, using the feedback_reader tool.
2. For each feedback item, categorize the feedback into themes using the categorization tool.
3. For each feedback item, extract the keywords using the keyword_extraction tool.
4. Create a JSON object that contains the feedback id, the categorized theme, and the extracted keywords.
Example:
[
    {"id": "1", "theme": "product", "keywords": ["good", "recommend"]},
    {"id": "2", "theme": "service", "keywords": ["bad", "not recommended"]},
    {"id": "3", "theme": "other", "keywords": ["neutral", "ok", "average"]}
]
5. Return the JSON object.
"""

def create_feedback_analysis_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Feedback Analysis Agent",
        system_message="You are a helpful AI assistant. "
                      "You can perform sentiment analysis on customer feedback. "
                      "You can read customer feedback using the feedback_reader tool. It will return a list of feedback, that consists of id, text, and source. "
                      "Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. "
                      "You can also categorize the feedback into themes using the categorization tool. "
                      "You can also extract keywords from the feedback using the keyword_extraction tool. "
                      "Don't include any other text in your response. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    agent.register_for_llm(name="feedback_reader", description="Read customer feedback")(query_feedback)
    agent.register_for_llm(name="sentiment_analysis", description="Analyze the sentiment of a customer feedback")(analyze_sentiment)
    agent.register_for_llm(name="categorization", description="Categorize feedback into themes")(categorize_feedback)
    agent.register_for_llm(name="keyword_extraction", description="Extract keywords from a customer feedback")(extract_keywords)

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
    user_proxy.register_for_execution(name="categorization")(categorize_feedback)
    user_proxy.register_for_execution(name="keyword_extraction")(extract_keywords)
    return user_proxy


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["sentiment_analysis", "keyword_extraction", "categorization", "categorize_and_extract_keywords"], required=True, default="sentiment_analysis")
    args = parser.parse_args()

    prompt = None
    if args.mode == "sentiment_analysis":
        prompt = PROMPT_SENTIMENT_ANALYSIS
    elif args.mode == "keyword_extraction":
        prompt = PROMPT_KEYWORD_EXTRACTION
    elif args.mode == "categorization":
        prompt = PROMPT_CATEGORIZATION
    elif args.mode == "categorize_and_extract_keywords":
        prompt = PROMPT_CATEGORIZE_AND_EXTRACT_KEYWORDS

    user_proxy = create_user_proxy()
    feedback_analysis_agent = create_feedback_analysis_agent()
    user_proxy.initiate_chat(
        feedback_analysis_agent, 
        message=prompt
    )

if __name__ == "__main__":
    main()
