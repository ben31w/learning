def show_messages(texts):
    """Prints a list of text messages."""
    for text in texts:
        print(text)

def send_messages(unsent_texts, sent_texts):
    """
    'Sends' text messages by printing them and moving them
    to a list called sent_texts.
    """
    while unsent_texts:
        text = unsent_texts.pop()
        print(text)
        sent_texts.append(text)

texts = ['hi', 'lol', 'lmao']
sent_texts = []

# 'Archive' the texts (keep them in 'texts' list) by calling 
# send_messages() with a splice.
send_messages(texts[:], sent_texts)

print(texts)
print(sent_texts)