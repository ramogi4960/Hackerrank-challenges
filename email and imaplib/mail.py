import imaplib
import email

gmail_imap = "imap.gmail.com"
email_address = input("Enter email address: ")
password = input("Enter email password: ")
imap = imaplib.IMAP4_SSL(gmail_imap)
imap.login(email_address, password)

imap.select("Inbox")
_, message_nums = imap.search(None, "ALL")

for message_num in message_nums[0].split()[3:6]:
    _, data = imap.fetch(message_num, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    print(f"Message number: {message_num}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")
    print("Content:")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())
