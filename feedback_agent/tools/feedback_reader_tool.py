from typing import List, TypedDict, Literal

class Feedback(TypedDict):
    id: str
    text: str
    source: Literal["email", "chat", "survey"]

feedback_store: List[Feedback] = [
    {
        "id": "1",
        "text": "I love the product!",
        "source": "email"
    },
    {
        "id": "2",
        "text": "The product is great!",
        "source": "chat"
    },
    {
        "id": "3",
        "text": "I had a great experience with the product.",
        "source": "survey"
    },
    {
        "id": "4",
        "text": "I had a bad experience with the product.",
        "source": "survey"
    },
    {
        "id": "5",
        "text": "I had a great experience with the product.",
        "source": "survey"
    }
]

def query_feedback() -> List[Feedback]:
    return feedback_store
