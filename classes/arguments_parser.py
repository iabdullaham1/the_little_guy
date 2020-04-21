import argparse
import sys

class arguments_parser():


	def args_parser(self):

	  parser = argparse.ArgumentParser(usage="theLittleGuy.py -u [url] -t [number of threads] -w [wordlist path]")

	  parser.add_argument("-u", "--url", required=True, help="The url to the webserver, the default method if not specified is http and port 80")
	  parser.add_argument("-p", "--port", type=int, help="The port, the default port for http is 80 and for https 443")
	  parser.add_argument("-v", "--verbose", action="store_true", help="Increase the verbosity")
	  parser.add_argument("-a", "--user_agent", help="The user-agent, the default user-agent is : Mozilla/5.0")
	  parser.add_argument("-P", "--proxy", help="Use this options if you want to use a proxy")
	  parser.add_argument("-r", "--recursive", action="store_true", help="activate the recursive functionality")
	  parser.add_argument("-H", "--header_analyzer", action="store_true", help="run the header analyzer script")
	  parser.add_argument("-f", "--full", action="store_true", help="run all scripts")
	  parser.add_argument("-b", "--buster", action="store_true", help="run the file buster script")	
	  
	  options, remaining = parser.parse_known_args()
	  if options.buster or options.full :
	  	parser.add_argument("-t", "--threads", required=True, type=int, help="Number of threads")
	  	parser.add_argument("-w", "--wordlist", required=True, help="The path to the wordlist")
	  return parser.parse_args()