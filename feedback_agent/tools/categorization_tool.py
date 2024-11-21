from autogen import AssistantAgent
from feedback_agent.config import LLM_CONFIG

def categorize_feedback(text: str) -> str:
    agent = AssistantAgent(
        name="Feedback Categorization Agent",
        system_message="You are a helpful AI assistant. "
                      "You can categorize customer feedback into themes. "
                      "Given a customer feedback, you can use the categorization tool to categorize the feedback. "
                      "You will provide categorization result in the following format: '[theme]'. "
                      "Example result: 'product'. "
                      "Example of invalid result: 'theme is product'."
                      "Theme can be 'product', 'service', or 'other'. "
                      "Don't include any other text in your response."
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )
    reply = agent.generate_reply(
        messages=[
            {"role": "user", "content": f'categorize the following feedback: {text}'}
        ],
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

    reply_values = reply_value.splitlines()
    if len(reply_values) != 1:
        reply_value = reply_values[0]

    reply_value = reply_value.replace("[", "").replace("]", "").replace(" ", "").strip()

    return reply_value