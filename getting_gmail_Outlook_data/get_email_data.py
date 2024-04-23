import imaplib
import email
import csv

# Gmail IMAP configuration
IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993

# Connect to the IMAP server
imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

# Login credentials
EMAIL_ADDRESS = input("Enter your Gmail email address: ")
EMAIL_PASSWORD = input("Enter your Gmail Gmail password: ")
# EMAIL_PASSWORD = getpass.getpass("Enter your Gmail password: ",stream=None)


# Login to the mailbox
imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

# Select the mailbox you want to extract emails from (e.g., INBOX)
imap.select("INBOX")

# meparker3.14159265359@gmail.com
# oqlrxnczqegxllsf
# [b'(\\HasNoChildren) "/" "INBOX"', b'(\\HasChildren \\Noselect) "/" "[Gmail]"', b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"', b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Bin"', b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"', b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"', b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"', b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"', b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"']
# Search for the first 50 emails in the selected mailbox
status, email_ids = imap.search(None, "ALL")  # 'search from @usergmail
email_ids = email_ids[0].split()[:50]

# Create a dataset to store the extracted emails
dataset = []

# Iterate over each email
for email_id in email_ids:
    # Fetch the email
    status, email_data = imap.fetch(email_id, "(RFC822)")
    raw_email = email_data[0][1]

    # Parse the raw email data
    parsed_email = email.message_from_bytes(raw_email)

    # Extract relevant email attributes
    sender = parsed_email["From"]
    subject = parsed_email["Subject"]
    date = parsed_email["Date"]
    body = ""

    if parsed_email.is_multipart():
        for part in parsed_email.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode("utf-8")
                break
    else:
        body = parsed_email.get_payload(decode=True).decode("utf-8")

    # Append the extracted attributes to the dataset
    dataset.append([sender, date, subject, body])

# Disconnect from the mailbox
imap.logout()

# Save the dataset to a CSV file
csv_file = "email_dataset.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Sender", "Date", "Subject", "Body"])  # Header row
    writer.writerows(dataset)

print(f"Dataset saved to {csv_file}.")
