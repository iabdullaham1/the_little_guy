#!/usr/bin/python3
import requests
import _thread
import time
import sys
from datetime import timedelta

class file_buster():

	

	def __init__(self, number_of_threads, list_path, url, user_agent, port, verbose, proxy):
		
		self.found_paths = []
		self.number_of_threads = number_of_threads
		self.threads_count = number_of_threads
		self.start_time = time.monotonic()
		self.user_agent = user_agent
		self.detection_file = ""
		self.counter = 0
		self.list_length = 0
		self.list_progress = 0
		self.verbose = verbose
		self.url = self.format_url(url)
		self.port = port if port != 0 else self.calculate_port()
		self.proxies = None if proxy is None else {"http": proxy,"https": proxy}
		self.lists = self.load_list(list_path, number_of_threads)


		
	def load_list(self, path, number_of_threads):
		
		print("loading dictionary ...")
		list = []
		
		for i in range(number_of_threads):
		
			list.append([])
		
		with open(path) as file:

			for index,line in enumerate(file):
				
				self.list_length = self.list_length + 1
				list[index % number_of_threads].append(line)

		print("dictionary loaded.\n")
		return list


	def threads_factory(self):

		for index,list in enumerate(self.lists):
			
			try:
		
				_thread.start_new_thread( self.bust_list, (index,) )
		
			except Exception as e:
		
				print(e)

		while self.threads_count != 0:
			pass

		self.load_results()


	def bust_list(self,tnumber):
		
		for index in range(len(self.lists[tnumber])):
			
			if self.counter == 50 :

				self.blocker_detector()
				self.counter = 0

			self.send_request(self.lists[tnumber][0])
			self.lists[tnumber].pop(0)			
			self.list_progress = self.list_progress + 1

		self.threads_count = self.threads_count - 1


	def send_request(self,line):
		
		try:
			
			path = f"{self.url}/{line}"
			request = requests.get(path[:-1], allow_redirects=True, headers={'User-Agent': self.user_agent}, proxies=self.proxies)
			
			if request.status_code != 404 :
				
				print(f"{path[:-1]} : {request.status_code} \n")
				self.found_paths.append((path[:-1],request.status_code))
				
				if self.detection_file == "" and line[:-1] != "" :

					self.detection_file = line[:-1]
					print(f"[-] the detection_file is : {self.detection_file} \n")
			
			elif self.verbose :
				print(f"{path[:-1]} : {request.status_code} \n")

		except Exception as e:
		
			print(e)


	def format_url(self,url):
		
		formated_url = f"{url}" if len(url.split("http")) >= 2 else f"http://{url}"
		formated_url = formated_url if formated_url[len(formated_url) - 1] != "/" else f"{formated_url[:-1]}"
		return formated_url


	def save_list_to_resume(self):
		
		try :

			path = f"theLittleGuy_{time.time()}.list"
			with open(path,"w") as file :
			
				for list in self.lists :
			
					for line in list:
			
						file.write(line)
			
			print(f"[-] I have created a new list named : {path} in case you wanted to continue later\n")

		except Exception as e :

			print(e)


	def blocker_detector(self):
		
		if self.detection_file != "" :
			try :
		
				request = requests.get(f"{self.url}/{self.detection_file}", allow_redirects=True, headers={'User-Agent': self.user_agent})
			
				if request.status_code != 200 :
				
					print("Error: either there is an issue with the server or the server is trying to block us !")
					exit(1)
		
			except Exception as e :
				print(e)


	def load_results(self):

		path = f"theLittleGuy-results-{time.time()}"
		
		try :
		
			with open(path, "w") as file :

				for line in self.found_paths :

					file.write(f"{line[0]} : {line[1]} \n")

			print(f"[-] The script needed {timedelta(seconds= time.monotonic() - self.start_time)} to finish\n")
			print(f"[-] The results were saved in the file : {path} \n")
		
		except Exception as e :

			print(e)

	def calculate_port(self) :

		if len(self.url.split("https://")) > 1 :
			return 443
		else :
			return 80

