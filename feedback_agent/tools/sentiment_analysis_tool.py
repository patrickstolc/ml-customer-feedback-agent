from typing import Literal, Union
from autogen import AssistantAgent, ConversableAgent
from feedback_agent.config import LLM_CONFIG

def analyze_sentiment(text: str) -> Union[Literal["positive"], Literal["negative"], Literal["neutral"]]:
    agent = AssistantAgent(
        name="Sentiment Analysis Agent",
        system_message="You are a helpful AI assistant. "
                      "You can analyze the sentiment of a customer feedback. "
                      "Given a customer feedback, you can use the sentiment_analysis tool to analyze the sentiment. "
                      "You will provide sentiment analysis result in the following format: '[sentiment]'. "
                      "Example: 'positive'. "
                      "Sentiment can be 'positive', 'negative', or 'neutral'. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )
    reply = agent.generate_reply(
        messages=[
            {"role": "user", "content": f'analyze the sentiment of the following feedback: {text}'}
        ]
    )

    if not reply:
        raise ValueError("No reply found")

    reply_value = ""
    if isinstance(reply, dict):
        reply_content = reply["content"]
        if reply_content:
            reply_value = reply_content
        else:
            raise ValueError("No content found in the reply")
    else:
        reply_value = reply

    reply_value = reply_value.replace("[", "").replace("]", "")

    if reply_value not in ["positive", "negative", "neutral"]:
        raise ValueError(f"Invalid sentiment value: {reply_value}")

    return reply_value