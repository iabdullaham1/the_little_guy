#!/usr/bin/python3
from  classes import file_buster
from classes import arguments_parser
from classes import header_analyzer
from classes import prepare

img = """                                                  
                       &@@@/                      
                     @@@@@@@@&                    
                    @@@@@@@@@@. ------------------                  
                    %@@@@@@@@@ |  The Little Guy  |      
                     %@@@@@@@  |  By Iabdullaham  |     
                        .,      ------------------                  
             %@@@@@@@@@@*                         
         (@&        @@@@@@@@,                ,,,  
       .@*         @@@@@@@@@@@              .,,,. 
       @,          @@@@@@@@@@@/@@          (@*    
      (@          *@@@@@@@@@@@    (@@@@@@@%       
     ,,,,,        #@@@@@@@@@@@                    
                  %@@@@@@@@@@%                    
                  *@@@@@@@@@@                     
                   @@@@@@@@@/                     
                    #@@@@@@@@@@&%(*,@             
                     @@            ,@             
                  .@&              *@             
                &@*                /@             
            .@@/                   .*,,,,,,       
   .,,,#@@@.                        .,,,,         
  ,,,,,                                           
  .,,    
  "
"""



if __name__ == "__main__" :

  print(img)

  parser = arguments_parser.arguments_parser()
  args = parser.args_parser()

  prepare = prepare.prepare()

  user_agent = prepare.prepare_user_agent(args.user_agent)
  url  = prepare.prepare_url(args.url) 
  port = prepare.prepare_port(args.port,url)

  if args.header_analyzer or args.full :

    try :
      
      analyzer = header_analyzer.header_analyzer(url, user_agent, port, args.proxy)
      analyzer.main()

    except Exception as e :
      
      print(e)

  if args.buster or args.full : 

    buster = file_buster.file_buster(args.threads, args.wordlist, url, user_agent,port, args.verbose, args.proxy, args.recursive)

    try : 

      buster.main()

    except KeyboardInterrupt :

      buster.save_list_to_resume()