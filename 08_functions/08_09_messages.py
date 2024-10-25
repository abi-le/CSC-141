#pass the list to a function called show_messages
def show_messages (messages):
    '''print a series of text messages'''
    for message in messages:
        msg = (f"{message}")
        print(msg)

text_messages = ['Hello, how are you?', 'What are you doing today?', 'Do you want to hangout today?']
show_messages(text_messages)