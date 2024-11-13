from datetime import datetime
from typing import Annotated, TypedDict, Literal, Optional

class Feedback(TypedDict):
    id: str
    date: str
    text: str
    source: Literal["email", "chat", "survey"]

feedback_store: list[Feedback] = [
    {
        "id": "1",
        "date": "2024-01-01",
        "text": "I love the product!",
        "source": "email",
    },
    {
        "id": "2",
        "date": "2024-01-01",
        "text": "The product is very good!",
        "source": "chat"
    },
    {
        "id": "3",
        "date": "2024-01-01",
        "text": "I had a great experience with the product.",
        "source": "survey"
    },
    {
        "id": "4",
        "date": "2024-01-01",
        "text": "I had a bad experience with the product.",
        "source": "survey"
    },
    {
        "id": "5",
        "date": "2024-01-01",
        "text": "I had a great experience with the product.",
        "source": "survey"
    }
]

def feedback_reader(start_date: Annotated[Optional[str], "YYYY-MM-DD"] = None, end_date: Annotated[Optional[str], "YYYY-MM-DD"] = None) -> Annotated[list[Feedback], "A list of feedback items"]:
    if start_date is None or end_date is None:
        return feedback_store
    
    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(end_date, "%Y-%m-%d")
    
    return list(
        filter(
            lambda feedback: start_datetime <= datetime.strptime(feedback["date"], "%Y-%m-%d") <= end_datetime,
            feedback_store
        )
    )
