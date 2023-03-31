#! /usr/bin/python3.6
from imapclient import IMAPClient 
import pprint
import pyzmail
import sys

#from imapclient import IMAPClient
imapObj=IMAPClient('imap.gmail.com',ssl=True)
imapObj.login('budagavichaitu@gmail.com',sys.argv[1])
inbox=imapObj.select_folder('INBOX')
#UID=imapObj.search(['SINCE 24-oct-2019'])
#print(inbox[b'EXISTS'])
mailids=["info@lucifro.com","info@buddy4study.com","<store-news@amazon.in","ramit.sethi@iwillteachyoutoberich.com"]
try:
	for mailid in mailids:
		UIDS=imapObj.search(['FROM',mailid])
		for UID in UIDS:
			rawMessage=imapObj.fetch(UID,['BODY[]',])
			message=pyzmail.PyzMessage.factory(rawMessage[UID][b'BODY[]'])
			#imapObj.delete_messages([UID])
			#imapObj.expunge()
			print('Deleted mails with subjects',end='')
			pprint.pprint(message.get_subject())
			#pprint.pprint('raw Items:',rawMessages.items())
			#print(UIDS)
			imapObj.move( [UID],  '[Gmail]/Trash')
			#pprint.pprint(imapObj.list_folders())

finally:
	imapObj.logout()
	print('Suucessfully Deleted')