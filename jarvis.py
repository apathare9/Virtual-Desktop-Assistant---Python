import pyttsx3 
import speech_recognition as sr 
import webbrowser   
import wikipedia  
import os  
import pyjokes 
import requests  
import datetime 
import wolframalpha  
import smtplib  
import winshell 
from twilio.rest import Client 
from pywikihow import search_wikihow  
import wikipedia as googleScrap 
import pywhatkit as kit  
import speedtest  
import psutil
import socket
import functions1
import functions2
import webbrowser as web
import time
import keyboard

#================================================= WHILE LOOP TO CALL ALL THE FUNCTIONS =================================================
while(True):
        
    query = functions1.inputCommand().lower()  # calling inputCommand() function and ensuring all the text are in lower-case by using lower() function

    if "day" in query:  # ------TELLS DAY
        day_of_the_week = functions1.Day()   # calling the function 'Day()' and storing the value in 'day_of_the_week' variable
        print("The day is " + day_of_the_week  + ".")
        functions1.speak("The day is " + day_of_the_week  + ".")
        continue


    elif "date" in query: # ------TELLS DATE
        date = str(datetime.date.today())   # calling the function 'datetime()' and storing the value in 'date' object
        print(date)
        functions1.speak("Date is " + date)


    elif "time" in query:  # ------TELLS TIME
        time = datetime.datetime.now().strftime("%H:%M:%S") #time=object, datetime()= module, datetime()=class, now() & steftime=method. Its specifying the format of time i.e., hour, minute, seconds
        print("The time is: " + time)
        functions1.speak("The time is " + time)
        continue


    elif 'news' in query:  # ------TELLS NEWS
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        functions1.speak('Opening news from the Times of India website ! Enjoy Reading !')
            
    
    elif 'joke' in query:  # ------TELLS JOKES
        functions1.speak(pyjokes.get_joke())  # It will call pyjokes module
        continue


    elif 'music' in query or "song" in query or "songs" in query:  # ------PLAY SONGS FROM SPECIFIC FOLDER
        functions1.music()


    elif "open" in query:  # ------OPENING ANY WEBSITE OR DESKTOP APPLICATION
        functions1.Open_Apps_and_websites(query)
    

    elif "weather" in query:     # ------TELLS WHEATHER
        functions1.weather() 


    elif "where is" in query:  # ------FINDS LOCATION
        query = query.replace("where is", "")  # replacing the words 'where is' with space. Its basically done to remove 'where is' words from the sentence
        location = query  # transferring the name of the place from query to location variable
        functions1.speak("You asked for the location of" + location)
        webbrowser.open("https://www.google.nl/maps/place/" + location + "")
        
    
    elif "write a note" in query:  # ------WRITING NOTES
        functions1.note()


    elif "show note" in query or "show the note" in query or "show me the note" in query:  # ------SHOWING NOTES
        functions1.speak("Showing Notes")
        file = open("jarvis_writes.txt", "r")  # it open the text file in read(r) mode
        print(file.read())   # it will print all the text from the file
        functions1.speak(file.read(20))   # it will functions1.speak first 20 lines from the file
    
    
    elif 'ask' in query:  # ------ASKING QUESTIONS FROM WOLFRAMALPHA API
        functions1.ask()


    elif "calculate" in query:   # ------ASKING MATHS QUESTIONS FROM WOLFRAMALPHA API
        functions1.calculation(query)        
               

    elif "message" in query:   # ------SENDS TEXT MESSAGE TO REGISTERED PHONE NUMBER
        functions1.message()

  
    elif "whatsapp" in query:   # ------SENDS WHATSAPP MESSAGE TO ANYONE 
        functions1.whatsapp_msg()
    
    
    elif "mail" in query:  # ------SENDS MAIL
        functions1.mail()


    elif 'search' in query:  # ------SEARCH INFORMATION FROM GOOGLE
        functions2.search(query)


    elif 'from wikipedia' in query:  # ------SEARCH INFORMATION FROM WIKIPEDIA
        functions2.from_wikipedia(query)
    

    elif "play" in query or " YouTube" in query:  # ---- PLAY VIDEOS OR SONGS FROM YOUTUBE
        functions2.videos_from_youtube(query)
 
   
    elif "how to" in query:    # ------TELLS STEPS FOR ANY RECIPIE OR TO DO ANY TASK
        functions2.how_to(query)


    elif 'empty recycle bin' in query or 'empty bin' in query:   # ------EMPTY RECYCLE BIN
        winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
        functions2.speak("Recycle Bin is emptyed")


    elif "battery" in query:   # ------TELLS BATTERY STATUS OF THE LAPTOP
        functions2.battery()    

    
    elif "c drive" in query:  # ------TELLS C DRIVE SPACE 
        functions2.c_drive()
        
        
    elif "d drive" in query:  # ------TELLS D DRIVE SPACE 
        functions2.d_drive()
    
    
    elif "RAM" in query or "ram" in query: # ------TELLS RAM STATUS
        functions2.RAM()
    
    
    elif "boot time" in query:   # ------TELLS BOOT TIME
        print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))


    elif "ip address" in query or "IP address" in query:   # ------TELLS IP ADDRESS
        hostname=socket.gethostname()   
        IPAddr=socket.gethostbyname(hostname)   
        print("Your Computer Name is:"+hostname + "\nYour Computer IP Address is:" + IPAddr)  
  
    
    elif 'speed' in query:   # ------TELLS INTERNET SPEED 
        functions2.SpeedTest(query)
    
    
    elif "current location" in query or "where am i" in query or "where i am" in query:  # ------TELLS CURRENT LOCATION OF USER
        functions2.my_location()
    
    
    elif "details" in query:  # ------TELLS CURRENT LOCATION DETAILS 
        functions2.location_details()


#======================================================= COMMONLY ASKED QUESTIONS ======================================================

    elif "hello" in query or "hey" in query:
        print("Hello boss, how was the day ?") 
        functions1.speak("Hello boss, how was the day ?") 
    
    elif "your name" in query or "who are you" in query:
        print("I am J.A.R.V.I.S. Your personal Assistant")
        functions1.speak("I am Jarvis. Your personal Assistant")

    elif "version" in query:
            print("My version is 1.O")
            functions1.speak("My version is 1.O")

    elif "what can you do" in query:  
        print("I can do many things like:\n 1.  Tell day, date, time and news\n 2.  Tell jokes.\n 3.  Play songs.\n 4.  Open websites.\n"
                " 5.  Launch desktop applications.\n 6.  Tell wheather of any place.\n 7.  Find location.\n 8.  Write a note.\n"
                " 9.  Answer any GK questions.\n 10. Answer any mathematical questions.\n 11. Send a text message.\n 12. Send whatsapp message.\n"
                " 13. Send a mail.\n 14. Search anything from Google.\n 15. Search anything from Wikipedia.\n 16. Play videos from YouTube.\n"
                " 17. Tell recipie.\n 18. Empty recycle bin.\n 19. Tell batteryinternal drive & RAM status.\n 20. Tell boot time.\n"
                " 21. Tell IP address.\n 22. Tell internet speed (both uploading and downloading speed).\n 23. Tell your current location details.\n")
        
        functions1.speak("I can do many things, some of them are lsited below")

    elif "great" in query or "good" in query or "nice" in query: 
        print("Well, tell me what should I do for you ?")
        functions1.speak("Well, tell me what should I do for you ?")

    elif "bad" in query or "worst" in query or "not good" in query: 
        print("Well, tell me what should I do to lift your mood ?")
        functions1.speak("Well, tell me what should I do to lift your mood ?")
    
    elif "who i am" in query or "who am i" in query:
        print("If you are talking then definately your human. Hahahaha")
        functions1.speak("If you are talking then definately your human. Hahahaha")

    elif 'thank' in query or 'thanks' in query:
        print("Any time boss :)")
        functions1.speak("Any time boss")
    
    elif "sorry" in query:
        print("Please don't be sorry.")
        functions1.speak("please don't be sorry")

    elif "funny" in query:  
        print("Happy to see you smiling :)")
        functions1.speak("Happy to see you smiling")

    elif "jarvis" in query:
        print("Yes boss, I am online....")
        functions1.speak("Yes boss, I am online.")

    elif "who made you" in query or "who created you" in query:
        print("I was created by Arpita Kar.")
        functions1.speak("I was created by Arpita Kar")
        
    elif "bye" in query or "stop" in query or "ok bye" in query or "goodbye" in query or "exit" in query:  # this will exit and terminate the program
        print("Good bye ! Hope to see you soon ;)")
        functions1.speak("Good bye ! Hope to see you soon !")
        break