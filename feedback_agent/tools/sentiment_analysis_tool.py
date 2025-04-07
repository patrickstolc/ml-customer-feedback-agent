import random
from typing import Annotated, List
import ast
from autogen import ConversableAgent, UserProxyAgent
from feedback_agent.config import LLM_CONFIG

SENTIMENT_VALUES = {"positive", "negative", "neutral"}

def sentiment_analysis(text: Annotated[List[str], "A list of strings"]) -> Annotated[List[int], "A list of integers"]:
    return [
        random.randint(0, 2)
        for _ in range(len(text))
    ]
