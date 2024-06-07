"""
Chatbot for the Mistral.

You need a valid Mistral API key to run this script.
"""

import os

from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

API_KEY = os.environ.get('MISTRAL_API_KEY')
MODEL = 'mistral-large-2402'  # 'mistral-large-latest'
SEP = 8 * '-'

assert API_KEY, "Mistral API key is required"

client = MistralClient(api_key=API_KEY)

chat_history = []


def user_input(msg: str) -> ChatMessage:
    return ChatMessage(role='user', content=msg)


while True:
    user_msg = user_input(input('user: '))

    chat_history.append(user_msg)

    response = client.chat(model=MODEL, messages=chat_history, temperature=.9, top_p=.3)

    response_msg = response.choices[0].message

    print(SEP)
    print(f'{response_msg.role}:', response_msg.content)
    print(SEP)

    chat_history.append(response_msg)
