def show_messages(messgaes):
    """打印列表中每条文本消息"""
    for message in messgaes:
        print(message)

def send_messages_f(messages,send_messages):
    while messages:
        messgae = messages.pop()
        print(f"print {messgae}")
        send_messages.append(messgae)

messages = [
    "aaaaa",
    "bbbbb",
    "ccccc",
    "ddddd",
    "eeeee",
]

send_messages = []
send_messages_f(messages,send_messages)
show_messages(messages)
show_messages(send_messages)