import requests

class header_analyzer():

	def __init__(self, url, user_agent, port, proxy) :

		self.url = url
		self.headers = self.get_headers()
		self.port = port 
		self.proxy = None if proxy is None else {"http": proxy,"https": proxy}
		self.user_agent = user_agent


	def get_headers(self) :

		request = requests.get(self.url)
		headers = request.headers

		return headers


	def xss_protection(self) :

			if self.in_headers("X-XSS-Protection") :

				if self.headers['X-XSS-Protection'] == "0" :
					
					print(f"X-XSS-Protection : {self.headers['X-XSS-Protection']} - disabled")
				
				else :

					self.print_header("X-XSS-Protection")
			
			else :

				print("[-] X-XSS-Protection is not present")
		

	def automated_check(self):
		
		check_informative = self.check_informative_header
		self.read_headers("resources/check_if_available_headers.lst", check_informative)

		check_important = self.check_important_header
		self.read_headers("resources/check_if_not_available_headers.lst", check_important)		

	def read_headers(self, headers_path, checking_function) :

		with open(headers_path) as file :

			for header in file : 

				header = header[:-1]
				
				if header != "" :
				
					checking_function(header)			


	def check_important_header(self, header) :

		if not self.in_headers(header) :

			print(f"[-] The {header} header is not present")

		else :

			self.print_header(header)


	def check_informative_header(self, header) :
		

		if self.in_headers(header) :

			self.print_header(header)


	def print_header(self, header) : 

		print(f"{header} : {self.headers[header]}")

	
	def in_headers(self, header) :

		if header in self.headers :
		
			return True

		else :

			return False


	def main(self) :

		self.xss_protection()
		self.automated_check()
