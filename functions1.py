#============================ FUNCTIONS OF THIS PROGRAM ARE KEPT IN TWO DIFFERENT FILES FOR READABILITY ===========================
#============================================ THIS FILE CONTAINS FIRST 16 FUNCTIONS ===============================================
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
import keyboard
import webbrowser as web
import time
import mouse

# --------INPUT_COMMAND FUNCTION---------
# Working: It converts voice speech into text
def inputCommand():

    r = sr.Recognizer()

    # from the speech_Recognition module we will use the Microphone module for listening the command
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # It is used to cancel the noise
        print('\nI am Listening...')
        
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.7  # Used to set the space between words wile talking
        audio = r.listen(source, phrase_time_limit=5)
        
        
        # Now we will be using the try and catch method so that if sound is recognized it is good else we will have exception handling
        try:
            print("Recognizing")
            
            # for Listening the command in indian english we can also use 'hi-In' for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')  # using google api for recognizing Indian english language
            print("You said: ", Query)
            
        except Exception as e:
            print(e)
            print("Sorry, please repeat it again.")
            return "None"
        
        return Query


# --------SPEAK FUNCTION---------
# Working: It converts text into voice speech
def speak(text):

    engine = pyttsx3.init()  # initiatinh module pyttx3 and creating an object named 'engine'
    engine.setProperty("rate", 185)  # to set the speaking rate
    engine.setProperty('volume', 1)  # to set the volume
   
    voices = engine.getProperty('voices') # getter method(gets the current value of engine property)

    engine.setProperty('voice', voices[0].id)  # setter method .[0]=male voice and [1]=female voice in set Property.

    engine.say(text)   # Method for the speaking of the the assistant

    engine.runAndWait()  # Blocks while processing all the currently queued commands


# --------PASSWORD FUNCTION---------
# Working: it askes for password before starting the application
def password():
    print("This application is password protected.\nPlease enter the password.")
    speak("This application is password protected\nPlease enter the password")
    
    for x in range(0,5):
    
        password = "1234"
        input_pass = str(input("Enter the password: "))

        if password == input_pass:
            clear = lambda: os.system('cls')  # It is used to clear the command prompt
            clear()  # calling the function named 'clear'

            
            print('Loading your personal assistant J.A.R.V.I.S......')
            speak("Loading your personal assistant Jarvis......")

            greet()

            day_of_the_week = Day()
            temp_in_celcius = your_location_weather()
            print("The day is " + day_of_the_week  + " and temperature is " +   str(temp_in_celcius) + " degree celsius.")
            speak("The day is " + day_of_the_week  + " and temperature is " +   str(temp_in_celcius) + " degree celsius.")

            print('How was the day boss ?')
            speak('How was the day boss')
            
            import jarvis
            break
        else:
            print("Access Denied")
            speak("Access Denied")
  

# --------GREET FUNCTION---------
# Working: It greets the user
def greet():
    hour=datetime.datetime.now().hour  # hour=object, datetime()= module, datetime()=class, now()=method, hour= property of method now()
    if hour>=0 and hour<12:  # condition: 12 am <= hour < 12pm
        print("Welcome back boss ! Good morning.")
        speak("Welcome back boss, Good morning.")
    
    elif hour>=12 and hour<18: #condition: 12pm <= hour < 6pm
        print("Welcome back boss ! Good afternoon.")
        speak("Welcome back boss, Good afternoon.")
    
    else:   # condition: 6pm <= hour < 12am
        print("Welcome back boss ! Good evening.")
        speak("Welcome back boss, Good evening.")
                  
            
# --------DAY FUNCTION---------
# Working: It tells the day of the week
def Day():
    
    day = datetime.datetime.today().weekday()  # day = object, datetime()= module, datetime()=class, today()=method, weekday()=method
                                               # weekday() is a method which contains int from 0 to 6 indicating days in a week. 0 = monday....6 = sunday

    # created a dictionary where the index is from 0 -6 contains days in a week
    Day_dict = {0: 'Monday', 
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    if day in Day_dict.keys():  # if the result of day object (which is a int, range 0-6) matches with index numbers of dictionary then move ahead 
        day_of_the_week = Day_dict[day]  #retrieve the data of that index number eg., index no.=2 & data=Wednesday
        return(day_of_the_week)


# --------MUSIC FUNCTION---------
# Working: Plays songs from your music directory (specify your music directory path in 'music_dir' variable )
def music():
    print("Enjoy your songs!")
    speak("Enjoy your songs!")
    music_dir = "C:\\Users\\karpi\\OneDrive\\Desktop\\Music"

    songs = os.listdir(music_dir)  # songs = object, os=module, listdir=function. It lists all the songs
    print(songs)  # printing the list of all songs 
    random = os.startfile(os.path.join(music_dir, songs[0])) #it will play the first song (whose index is 0) from the list

     
# --------OPEN WEBSITES & APPS FUNCTION---------
# Working: Opens websites and launches desktop applications 
def Open_Apps_and_websites(query):
        
        if "google" in query:  # ------OPEN GOOGLE
            speak("Opening Google ")
            webbrowser.open("www.google.com")  #webbrowser module is used to launch and remotely control Web browsers.
            pass

        elif "youtube" in query:  # ------OPEN YOUTUBE
            speak("Opening Youtube ")
            webbrowser.open("https://www.youtube.com")
            pass

        elif "facebook" in query: # ------OPEN FACEBOOK
            speak("opening facebook")
            webbrowser.open("www.facebook.com")
            pass
        
        elif "geeks for geeks" in query: # ------OPEN GEEKS FOR GEEKS
            speak("opening geeks for geeks")
            webbrowser.open("https://www.geeksforgeeks.org/")
            pass
        
        elif 'powerpoint presentation' in query or "ppt" in query or "powerpoint" in query:  # ------OPEN POWER POINT PRESENTATION
            speak("opening Power Point presentation")
            ppt_path = r"C:\Users\karpi\OneDrive\Desktop\PowerPoint 2016.lnk"  #path of power point application. Here 'r'=raw, means it will take the string as it is
            os.startfile(ppt_path)  # the os module will start the application

        elif 'Excel' in query: # ------OPEN MICROSOFT EXCEL
            speak("opening Microsoft Excel")
            excel_path = r"C:\Users\karpi\OneDrive\Desktop\Excel 2016.lnk"
            os.startfile(excel_path)
            
        elif 'word' in query or "microsoft word" in query:  # ------OPEN MICROSOFT WORD
            speak("opening Microsoft Word") 
            power = r"C:\Users\karpi\OneDrive\Desktop\Word 2016.lnk "  #path of power point application. Here 'r'=raw, means it will take the string as it is
            os.startfile(power)   # the os module will start the application

        elif 'telegram' in query:  # ------OPEN TELEGRAM
            speak("opening Telegram")
            power = r"C:\Users\karpi\OneDrive\Desktop\Telegram.exe "  #path of telegram application. Here 'r'=raw, means it will take the string as it is
            os.startfile(power)  # the os module will start the application

        elif 'chrome' in query:  # ------OPEN GOOGLE CHROME
            speak("opening Google Chrome")
            power = r"C:\Users\karpi\OneDrive\Desktop\Chrome.lnk "    #path of chrome browser. Here 'r'=raw, means it will take the string as it is
            os.startfile(power)   # the os module will start the application


# --------WEATHER FUNCTION---------
# Working: Tells weather
def weather():
    api_key = "fd1d66c49b7e37b81a0e4912dba3a399"   

    base_url = "http://api.openweathermap.org/data/2.5/weather?"  # base_url variable to store url

    # Give city name
    speak(" Which place wheather you want to know ? ")
    print("Which place wheather you want to know ? ")
    city_name = inputCommand()
     
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name  # Its basically the the complete url which will be sent to the weather website
        
    response = requests.get(complete_url) # get function of requests module returns the response object

    x = response.json() # json method of response object convert json format data into python format data

    if x["cod"] != "404": # Now x contains list of nested dictionaries Check the value of "cod" key is equal not to "404", means city is found otherwise, city is not found

        y = x["main"]  # store the value of "main" key in variable y

        temp_in_kelvin = y["temp"] # store the value corresponding to the "temp" key of y

        current_pressure = y["pressure"] # store the value corresponding to the "pressure" key of y

        current_humidiy = y["humidity"] # store the value corresponding to the "humidity" key of y

        z = x["weather"] # store the value of "weather" key in variable z

        weather_description = z[0]["description"] # store the value corresponding to the "description" key at the 0th index of z


        temp_in_kelvin = y["temp"] # store the value corresponding to the "temp" key of y. Currently the temp is in Kelvin
    
        temp_in_celcius =  temp_in_kelvin - 273.15 #Coverting Kelvin to Celcius
        
        temp_in_celcius = int(temp_in_celcius)


        # print following values
        print("Temperature is " + str(temp_in_celcius) + " degree celcius, atmospheric pressure is " + str(current_pressure) +
               ", humidity is " + str(current_humidiy) + r"% and there is " + str(weather_description) + ".")
        
        speak("Temperature is " + str(temp_in_celcius) + " degree celcius, atmospheric pressure is " + str(current_pressure) +
               ", humidity is " + str(current_humidiy) + "percent and there is " + str(weather_description))
    else:
        print(" City Not Found ")


# --------YOUR LOCATION WEATHER FUNCTION---------
# Working: Tells weather of your location (put the name of your city/town in 'city_name' variable)
def your_location_weather():
    api_key = "fd1d66c49b7e37b81a0e4912dba3a399"   # app id

    base_url = "http://api.openweathermap.org/data/2.5/weather?"  # base_url variable to store url

    city_name = 'vasai'  

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name  # Its basically the the complete url which will be sent to the weather website

    response = requests.get(complete_url) # get function of requests module returns the response object

    x = response.json() # json method of response object convert json format data into python format data


    if x["cod"] != "404": # Now x contains list of nested dictionaries Check the value of "cod" key is equal not to "404", means city is found otherwise, city is not found

        y = x["main"]  # store the value of "main" key in variable y
    
        temp_in_kelvin = y["temp"] # store the value corresponding to the "temp" key of y. Currently the temp is in Kelvin
    
        temp_in_celcius =  temp_in_kelvin - 273.15 #Coverting Kelvin to Celcius
        
        temp_in_celcius = int(temp_in_celcius)

        return(temp_in_celcius) #returning the value of 'temp_in_celcius' variable

    else:
        print(" City Not Found ")

         
# --------NOTE FUNCTION---------
# Working: Writes a note
def note():
    print("Boss, what should I write ?")
    speak("Boss, What should i write ?")
    note_content = inputCommand()    
    file = open('notes.txt', 'w')  # Here it creates a text file named 'jarvis_writes.txt' & it opens the txt file in write(w) mode

    print("Boss, Should I include the time ?")
    speak("Boss, Should I include the time ?")
    choice = inputCommand()
   
    if 'yes' in choice or 'sure' in choice:
        time=datetime.datetime.now().strftime("%H:%M:%S")  # format of time in Hour, Minute and Seconds
        file.write(time)  #writing the time in the text file.
        file.write(" :- ")
        file.write(note_content)  #writing the sentences said by the user in the text file.
    else:
        file.write(note_content)
        speak("ok boss")
        file.close()

    print("Should I show you the note ? ")
    speak("Should I show you the note ? ")
    query = inputCommand()
   
    if 'yes' in query:
        speak("Showing Notes")
        file = open("jarvis_writes.txt", "r")  # it open the text file in read(r) mode
        print(file.read())  # it will print all the text from the file
        speak(file.read(2))  # it will functions1.speak first 20 lines from the file
    else:
        speak("ok boss")


# --------ASK FUNCTION---------
# Working: It answers to any question using WolfRamALpha API
def ask():
    print("I can answer any of your queries, go ahead and ask me.")
    speak("I can answer any of your queries,  go ahead and ask me.")
    question= inputCommand()         

    app_id = 'your api id'        
    client = wolframalpha.Client('your api id')   #           
    result = client.query(question)  # Stores the response from wolf ram alpha            
    answer = next(result.results).text  # Includes only text from the response
    print(answer)
    speak(answer)


# --------CALCULATION FUNCTION---------
# Working: Calculates any mathematical questions using WolfRamAlpha API
def calculation(query):                    
    app_id = "your api id"  # app id
    client = wolframalpha.Client("your api id")

    query = query.replace("calculate", "")
    res = client.query(query)

    answer = next(res.results).text  # the result is stored in answer variable
    print("The answer is " + answer)
    speak("The answer is " + answer)


# --------TEXT MESSAGE FUNCTION---------
# Working: Sends text message to registered mobile number
def message():           
    account_sid = 'your account sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token)
    print("What message should I send ?")
    speak("What message should I send ?")
    message = client.messages.create(body=inputCommand(),from_='phone no. given by twilio',to='your registered phone no.')
    print(message.body)
    print(message.date_created)
    speak("Message has been send.")


# --------WHATSAPP MESSAGE FUNCTION---------
# Working: Sends whatsapp message to any mobile number
def whatsapp_msg():
    speak("whome should i send boss ?")
    number = '+91' + str(input("Phone number: "))
    
    speak("what should i send boss ?")
    message = input("Enter the message: ")
    
    open_chat = "https://web.whatsapp.com/send?phone=" + number + "&text=" + message
    web.open(open_chat)
    time.sleep(8)
    keyboard.press('enter')
    print("Message has been sent!")
    speak("Message has been sent")


# --------SEND EMAIL FUNCTION---------
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('email id', 'password')
    server.sendmail('email id', to, content)
    server.close()
  

# --------MAIL FUNCTION---------
# Working: to take reciever email id and email content from the user
def mail():
    try:
        print("Whome should i send ?")
        speak("Whome should i send ?")
        to = input("Type the email address: ")
        print("What should I write?")
        speak("What should I write?")
        content = inputCommand()
        sendEmail(to, content)
        print("Email has been sent !")
        speak("Email has been sent !")
    except Exception as e:
        print(e)
        print("I am not able to send this email :( ")
        speak("I am not able to send this email")