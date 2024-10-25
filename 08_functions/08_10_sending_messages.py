# text_messages = ['Hello, how are you?', 'What are you doing today?', 'Do you want to hangout today?']

text_messages = ['Hello, how are you?', 'What are you doing today?', 'Do you want to hangout today?']
sent_messages = []


def show_messages (messages):
    '''print a series of text messages'''
    for message in messages:
        msg = (f"{message}")
        print(f"send messages : {msg}")

show_messages(text_messages)

def send_messages(messages):
    '''print a series of text messages'''
    while messages:
        msg = text_messages.pop()
        sent_messages.append(msg)

send_messages(text_messages)
print (f"send messages: {text_messages}")
print (f"sent messages : {sent_messages}")

print ("The following messages have been sent.")
for sent_message in sent_messages:
    print (sent_message)