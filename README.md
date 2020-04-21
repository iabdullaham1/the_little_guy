# theLittleGuy

![N](https://i.ibb.co/dGBG51g/Screenshot-2020-04-16-21-24-05.png)

# What is theLittleGuy ?

The little guy is a kind of a big project which will have a lot of functionalities in  the future. However, right now it has only two modules (dictionary attacking the webserver to get the available paths, and analyzing the headers).



# The Headers Analyzer Features : 

1- The ability to pass the connection through a proxy.

2- changing the user-agent.

3- The ability to add new headers to check if they are present easily.

4- The ability to add new headers to check if they are missing (the script will show that the header is missing and print the value if the header is set)


# The Dicionary Attack Features :

1- Multi threading.

2- Error detection (it can detect if there is something wrong for example if the webserver have blocked you).

3- Pause and continue later (when you press CTRL+C the script will create a new list which contains the untested words in the list in case you wanted to continue later!).

4- Connecting to an HTTP proxy.

5- Changing the user-agent.

6- Verbose mode.

7- Creating a file at the end of execution which contains the results.

8- Recursive attack



# Pre-requirements :

1- python3.

2- requests library (I think it is shipped with the latest versions of python but I added it just in case).



# usage :
![N](https://i.ibb.co/rwZRfdY/2.png)

# Ading New Headers to check :

### 1 - Adding an informative header to check if present : 

This feature allows you to check if a certain header is present (for example the `Server` header) and if it is present the script will print it's value. You can add new headers to check if they are present by adding them to the file `resources/check_if_available_headers.lst` and when you run the script it will check them.

### 2 - Adding Important Headers to check and report if missing :

This feature allows you to check if some headers are missing , and if so it will report it to you, however if the header is set the script will print it's value in case there is a misconfiguration that you can test. You can add new headers to the list by adding them to the file `resources/check_if_not_available_headers.lst` .

