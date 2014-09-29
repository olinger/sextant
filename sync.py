import dropbox
import os, sys

class sync:

	def __init__(self):
		f = open("creds.txt", 'r')
		self.token = f.readlines()[0]
		print("TOKEN ", self.token)
		self.client = dropbox.client.DropboxClient(self.token)
		print('linked account: ', self.client.account_info())

	def uploadfile(self, filename, delete):
		f = open(filename, 'rb')
		response = self.client.put_file(filename, f)
		if (delete):
			os.remove(filename)
