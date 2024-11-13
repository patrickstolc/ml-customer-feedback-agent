import ast
from autogen import AssistantAgent, UserProxyAgent, ChatResult, register_function
from autogen.coding import LocalCommandLineCodeExecutor
from feedback_agent.tools.feedback_reader_tool import feedback_reader
from feedback_agent.tools.sentiment_analysis_tool import sentiment_analysis
from feedback_agent.tools.calculate_average_tool import calculate_average
from feedback_agent.config import LLM_CONFIG

ReAct_prompt = """
Answer the following questions as best you can. You have access to the tools provided.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do and what tool to use
Action: the action to take is ALWAYS one of the provided tools
Action Input: the input to the action
Observation: the result of the action. Only observe tools' outputs.
... (this thought/action/action input/observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question and should be a result of the provided tools and nothing else

Begin!
Question: {input}
"""


def react_prompt_message(sender, recipient, context):
    """
    Return the ReAct prompt message interpolated with the input question.
    """
    return ReAct_prompt.format(input=context["question"])


def create_feedback_analysis_agent() -> AssistantAgent:
    """
    Return a new feedback analysis agent.
    """
    agent = AssistantAgent(
        name="Assistant",
        system_message="""
        Only use tools. Don't try to reason. Reply TERMINATE when the task is done.
        """,
        llm_config=LLM_CONFIG
    )

    return agent

def create_user_proxy(code_executor: LocalCommandLineCodeExecutor):
    """
    Return a new user proxy agent.
    """
    user_proxy = UserProxyAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().lower().endswith("terminate"),
        human_input_mode="NEVER",
        max_consecutive_auto_reply=10,
        code_execution_config={
            "executor": code_executor
        },
    )
    return user_proxy


def create_local_code_executor():
    """
    Return a new local code executor.
    """
    return LocalCommandLineCodeExecutor(
        timeout=100,
    )


def setup_agents():
    """
    Setup the agents.
    """
    # Create the code executor, user proxy, and feedback analysis agent
    code_executor = create_local_code_executor()
    user_proxy = create_user_proxy(code_executor)
    feedback_analysis_agent = create_feedback_analysis_agent()

    # Add the feedback reader tool to the feedback analysis agent and user proxy agent
    register_function(
        feedback_reader, 
        caller=feedback_analysis_agent, 
        executor=user_proxy, 
        name="feedback_reader", 
        description="Read customer feedback, optionally filtered by start_date and end_date as YYYY-MM-DD formatted strings."
    )

    # Add the sentiment analysis tool to the feedback analysis agent and user proxy agent
    register_function(
        sentiment_analysis, 
        caller=feedback_analysis_agent, 
        executor=user_proxy, 
        name="sentiment_analysis", 
        description="Returns sentiment of a customer feedback given a list of feedback strings."
    )

    # Add the calculate average tool to the feedback analysis agent and user proxy agent
    register_function(
        calculate_average, 
        caller=feedback_analysis_agent, 
        executor=user_proxy, 
        name="calculate_average", 
        description="Calculate the average given a list of numbers."
    )

    # Return the user proxy and feedback analysis agent
    return user_proxy, feedback_analysis_agent


def get_tool_calls(chat_result: ChatResult):
    """
    Return the tool calls from the chat result.
    """
    tool_call_history = []

    for message in chat_result.chat_history:
        if "tool_calls" in message.keys():
            tool_calls = map(lambda x: { "name": x["function"]["name"], "arguments": ast.literal_eval(x["function"]["arguments"]) }, message["tool_calls"])
            tool_call_history.extend(list(tool_calls))

    return tool_call_history


def find_final_answer(chat_result: ChatResult):
    """
    Return the final answer from the chat result.
    """

    # Get the chat history
    messages = chat_result.chat_history
    final_answer = None

    # Iterate over the chat history in reverse order
    for message in reversed(messages):
        # Check if the message contains the final answer
        if "final answer:" in message.get("content", "").lower():
            # Get the final answer block    
            final_answer_block = message.get("content", "")

            # Split the final answer block into lines
            answer_block_lines = final_answer_block.split("\n")

            # Get the final answer
            final_answer = answer_block_lines[-1].split("Final Answer:")[1].strip()
            break

    # Return the final answer
    return final_answer


def main():
    # Setup the agents
    user_proxy, feedback_analysis_agent = setup_agents()

    # Define the task
    task = "What is the average feedback sentiment in Q1 2024?"

    # Initiate the chat
    user_proxy.initiate_chat(
        feedback_analysis_agent,
        message=react_prompt_message,
        question=task
    )


if __name__ == "__main__":
    main()
