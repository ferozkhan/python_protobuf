from datetime import datetime
from itertools import islice

from app.protos.message_pb2 import Chat


def generate_dummy_messages():
    i = 0
    while True:
        yield {
            "text": f"blah {i}",
            "datetime": str(datetime.now())
        }
        i += 1


def buffer_message(message_buf, _message):
    print('buffering messages')
    message_buf.text = _message.get("text")
    message_buf.datetime = _message.get("datetime")


def get_messages():
    messages = islice(generate_dummy_messages(), 10)
    for _message in messages:
        message_buf = chat.message.add()
        buffer_message(message_buf, _message)


def read_messages():
    for message in chat.message:
        print(message)


if __name__ == "__main__":
    chat = Chat()
    get_messages()
    read_messages()
