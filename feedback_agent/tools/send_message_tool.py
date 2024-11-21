from typing import Annotated


def send_message(message: Annotated[str, "The message to send to the user."]) -> None:
    """
    Send a message to the user.
    """
    print(f"Sending message: {message}")
