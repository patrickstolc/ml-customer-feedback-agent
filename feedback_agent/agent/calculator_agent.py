from autogen import ConversableAgent
from typing import Annotated, Literal
from feedback_agent.config import LLM_CONFIG

Operator = Literal["+", "-", "*", "/"]

def calculator(a: int, b: int, operator: Annotated[Operator, "operator"]) -> int:
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return int(a / b)
    else:
        raise ValueError("Invalid operator")


def create_calculator_agent() -> ConversableAgent:
    # define the agent
    agent = ConversableAgent(
        name="Calculator Agent",
        system_message="You are a helpful AI assistant. "
                      "You can help with simple calculations. "
                      "Reflect on the order of operations and calculate the result. "
                      "Return 'TERMINATE' when the task is done.",
        llm_config=LLM_CONFIG,
    )

    # add the tools to the agent
    agent.register_for_llm(name="calculator", description="A simple calculator")(calculator)

    return agent

def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )
    user_proxy.register_for_execution(name="calculator")(calculator)
    return user_proxy


def main():
    user_proxy = create_user_proxy()
    calculator_agent = create_calculator_agent()
    chat_result = user_proxy.initiate_chat(calculator_agent, cache=None, message="What is (44232 + 13312 / (232 - 32)) * 5?")
    print(chat_result)

if __name__ == "__main__":
    main()
