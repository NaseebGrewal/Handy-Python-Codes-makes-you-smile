import imaplib
import getpass

# Gmail IMAP configuration
IMAP_SERVER = 'imap.gmail.com'
IMAP_PORT = 993

# Login credentials
EMAIL_ADDRESS = input("Enter your Gmail email address: ")
EMAIL_PASSWORD = getpass.getpass("Enter your Gmail password: ")

def get_mailbox_folders():
    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)

    # Login to the mailbox
    imap.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    # Retrieve the list of mailbox folders
    status, folder_list = imap.list()

    # Print and save the folder names
    folder_names = []
    for folder in folder_list:
        folder_info = folder.decode().split(' "/" ')[1]
        folder_name = folder_info.strip('"')
        folder_names.append(folder_name)
        print(status,folder_name)

    # Disconnect from the mailbox
    imap.logout()
    folder_names2 = []
    for folder in folder_names:
        if folder == 'INBOX':
            folder_names2.append(folder)
        elif folder == '[Gamil]/':
            continue
        else:
            temp = folder.lstrip('[Gmail]/')
            folder_names2.append(temp)
    

    # Save the folder names to a text file
    file_path = 'folder_names.txt'
    with open(file_path, 'w') as file:
        file.writelines('\n'.join(folder_names2))

    print(f"Folder names saved to {file_path}.")

# Call the function to retrieve and print the mailbox folders
get_mailbox_folders()
