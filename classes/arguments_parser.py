import argparse

class arguments_parser():


	def args_parser(self):

	  parser = argparse.ArgumentParser(usage="theLittleGuy.py -u [url] -t [number of threads] -w [wordlist path]")
	  
	  parser.add_argument("-u", "--url", required=True, help="The url to the webserver, the default method if not specified is http and port 80")
	  parser.add_argument("-p", "--port", type=int, help="The port, the default port for http is 80 and for https 443")
	  parser.add_argument("-v", "--verbose", action="store_true", help="Increase the verbosity")
	  parser.add_argument("-t", "--threads", required=True, type=int, help="Number of threads")
	  parser.add_argument("-a", "--user_agent", help="The user-agent, the default user-agent is : Mozilla/5.0")
	  parser.add_argument("-w", "--wordlist", required=True, help="The path to the wordlist")
	  parser.add_argument("-P", "--proxy", help="Use this options if you want to use a proxy")

	  return parser.parse_args()