class prepare():

	def __init__(self) :
		pass


	def prepare_url(self, url) : 

		formated_url = f"{url}" if len(url.split("http")) >= 2 else f"http://{url}"
		formated_url = formated_url if formated_url[len(formated_url) - 1] != "/" else f"{formated_url[:-1]}"
		
		return formated_url

	def prepare_port(self, port, url) :

		if port is not None :

			return port

		else :

			if len(url.split("https://")) > 1 :
			
				return 443
		
			else :
		
				return 80

	def prepare_user_agent(self,user_agent) :

		if user_agent is not None :

			return user_agent

		else :

			return "Mozilla/5.0"