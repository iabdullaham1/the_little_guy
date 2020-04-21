from  classes import file_buster
from classes import arguments_parser
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

  user_agent = "Mozilla/5.0" if args.user_agent is None else args.user_agent
  port = 0 if args.port is None else args.port

  print(args)

  buster = file_buster.file_buster(args.threads, args.wordlist, args.url, user_agent,port, args.verbose, args.proxy, args.recursive)

  try : 

    buster.main()

  except KeyboardInterrupt :

    buster.save_list_to_resume()