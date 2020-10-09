import logging
from datetime import datetime
from itertools import islice

from app.protos.message_pb2 import Chat

log = logging.getLogger()


def generate_dummy_messages():
    i = 0
    while True:
        yield {
            "text": f"blah {i}",
            "datetime": str(datetime.now())
        }
        i += 1


def buffer_message(message_buf, _message):
    log.info('buffering message')
    message_buf.text = _message.get("text")
    message_buf.datetime = _message.get("datetime")


def get_messages(number_of_messages=10):
    messages = islice(generate_dummy_messages(), number_of_messages)
    [buffer_message(chat.message.add(), _message) for _message in messages]


def read_messages():
    for message in chat.message:
        print(message)


if __name__ == "__main__":
    chat = Chat()
    get_messages(number_of_messages=20)
    read_messages()
