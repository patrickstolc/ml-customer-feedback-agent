from typing import Annotated, List
import ast
from autogen import ConversableAgent, UserProxyAgent
from feedback_agent.config import LLM_CONFIG

SENTIMENT_VALUES = {"positive", "negative", "neutral"}

def sentiment_analysis(text: Annotated[List[str], "A list of strings"]) -> Annotated[List[int], "A list of integers"]:
    if not isinstance(text, list):
        raise ValueError("Input must be a list. It is currently a " + str(type(text)))
    agent = ConversableAgent(
        name="Sentiment Analysis Agent",
        system_message="""You are a helpful AI assistant.
                      You can analyze the sentiment of a customer feedback.
                      Given a list of feedback texts, you will analyze their sentiment and return a list of integers.
                      Positive sentiment is 2, neutral sentiment is 1, and negative sentiment is 0.
                      Example:
                      Input: ['I love the product!', 'The product is great!', 'I had a great experience with the product.']
                      Output: [2, 2, 2]
                      Don't include any other text in your response.
                      Return 'FINISH' when the task is done.""",
        is_termination_msg=lambda msg: msg.get("content") is not None and "FINISH" in msg["content"],
        llm_config=LLM_CONFIG,
    )    
    user_proxy = UserProxyAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "FINISH" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.initiate_chat(
        recipient=agent,
        max_turns=2,
        message=f'analyze the sentiment of each of the following feedback items, return a list of strings: {", ".join(text)}'
    )

    reply = user_proxy.last_message()

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

    reply_value = reply_value.replace("\nFINISH", "").strip()

    # extract the sentiment list string from the reply
    reply_value = reply_value[reply_value.find("[") : reply_value.find("]") + 1]
    if reply_value[0] == "[" and reply_value[-1] == "]":
        reply_value = ast.literal_eval(reply_value)
        reply_value = [int(value) for value in reply_value]

    return reply_value
