import imaplib

imap_host = 'imap.gmail.com'
imap_user = 'abhishek19@iiserb.ac.in'
imap_pass = 'Deathnote@13'


# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host, 993)

## login to server
imap.login(imap_user, imap_pass)

imap.select("INBOX")

status, message_list = imap.search(None, 'ALL')

messages = message_list[0].split(b' ')

print("SNo\tStatus")
for message in messages:
	
	if int(message) >= 2000:
		try:
			imap.store(message, "+FLAGS", "\\Deleted")
			print(f"{int(message)}\tDeleted")
		except:
			print(f"{int(message)}\tFailed")

imap.close()

imap.logout()