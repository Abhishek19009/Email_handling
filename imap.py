/* 
Short script for deleting old emails using IMAP protocol
Be careful selected emails will be deleted permanently
If encountered an error, mail me:- abhishek19@iiserb.ac.in 
*/


import imaplib

# Please update imap_user and imap_pass

imap_host = 'imap.gmail.com'
imap_user = 'Your email address here'
imap_pass = 'Your password here'


# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host, 993)

## login to server
imap.login(imap_user, imap_pass)

imap.select("INBOX")

status, message_list = imap.search(None, 'ALL')

messages = message_list[0].split(b' ')

# Specify serial number of email from where you want deletion to start

starting_index = input("Enter starting index for deletion: ")

print("SNo\tStatus")
for message in messages:
	
	if int(message) >= int(starting_index):
		try:
			imap.store(message, "+FLAGS", "\\Deleted")
			print(f"{int(message)}\tDeleted")
		except:
			print(f"{int(message)}\tFailed")

print("\nMails deleted successfully!!!")
imap.close()

imap.logout()
