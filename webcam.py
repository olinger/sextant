import requests
import os, sys
from PIL import Image
from io import BytesIO

class webcam:
	

	def __init__(self,ip, user, password):
		self.adress = ip
		self.user = user
		self.password = password
		self.http = 'http://'
		self.img_url = '/image'
		self.file_type = '.jpg'


	def take_pic(self, directory, name):
		if not os.path.exists(directory):
			os.makedirs(directory)
		print(str(self.http + self.adress + self.img_url + self.file_type))
		r = requests.get(str(self.http + self.adress + self.img_url + self.file_type), auth=(self.user, self.password))

		#check to make sure we are actually getting a valid response
		i = Image.open(BytesIO(r.content))
		img_name = directory + name + self.file_type
		i.save(img_name)		