#============================ FUNCTIONS OF THIS PROGRAM ARE KEPT IN TWO DIFFERENT FILES FOR READABILITY ===========================
#============================================== THIS FILE CONTAINS NEXT 13 FUNCTIONS ==============================================

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


# --------SEARCH FUNCTION---------
# Working: Searches any information from Google
def search(query):
    query = query.replace("search","")
    query = query.replace("what is","")
    speak("Here is what I have found from google ")
    try:
        kit.search(query)
        result = googleScrap.summary(query,2)
        print(result)
    except:
        speak("Audible data not found")


# --------SEARCH FROM WIKIPEDIA FUNCTION---------
# Working: Searches any information from Wikipedia
def from_wikipedia(query):      
    speak("Checking the wikipedia ")
    query = query.replace("wikipedia", "")  # replacing the word wikipedia with space. Its basically done to remove wikipedia word from the sentence	
    result = wikipedia.summary(query, sentences=2) # result=object, wikipedia=module, summary=function of module wikipedia. Passing the query to wikipedia module & functions.speak 2 sentences from that.
    speak("According to wikipedia")
    print(result)
    speak(result)


# --------VIDEOS FROM YOUTUBE FUNCTION---------
# Working: Plays any Youtube video
def videos_from_youtube(query):
    query = query = query.replace("play","")
    query = query = query.replace("song","")
    name = query.replace("YouTube","")
    print("Playing" + name )
    speak("Playing" + name )
    kit.playonyt(name)


# --------HOW TO FUNCTION---------
# Working: Tells recipe or steps to do any task
def how_to(query):
    max_results = 1
    how_to = search_wikihow(query, max_results)
    assert len(how_to) == 1
    print(how_to[0].summary)
    speak("Here is " + query)


# --------BATTERY FUNCTION---------
# Working: It tells the battery status of the laptop
def battery():
    battery = psutil.sensors_battery() 
    percentage = battery.percent  #fetching battery percentage
    sec_left = battery.secsleft   # fetching how many seconds left before battery drains out
    power = battery.power_plugged # fetching information whether charger is connected or not
    min_left = sec_left/60    # converting seconds left before battery drains out into minutes. NOTE: the value is in float
    min_left = int(min_left)  # converting float into integer to remove decimal points
    power = str(power)        # converting datatype of 'power' varibale which was in bool to string

    def p():
        true = "True"
        if true in power:  # if charger is connected that means its true then show the following sentence
            return("the battery is " + str(percentage) + "% " + "and charger is connected.")  
        else:  # if charger is not connected that means its false then show the following sentence
            return("the battery is " + str(percentage) + "%, " +  str(min_left) + " minutes left before it drains out and charger is not connected.")

    a = p()  #taking the output of funtion p in variable 
    print(a)
    speak(a)


# --------C DRIVE FUNCTION---------
# Working: It tells total, used and available space of C drive in Giga Bytes   
def c_drive():
    c_drive = list(psutil.disk_usage('C:/')) 
    total = c_drive[0]
    total = total // 10**9
    used = c_drive[1]
    used = used // 10**9
    free = c_drive[2]
    free = free // 10**9
    percent = c_drive[3]
    
    print("C drive storage status:")
    print(">> Total space: ",total,"GB")
    print(">> Used space: ",used, "GB")
    print(">> Free Space: ",free, "GB")
    print(">> Used space percentage: ",percent,"%")
    speak("Here are C drive storage status")


# --------D DRIVE FUNCTION---------
# Working: It tells total, used and available space of C drive in Giga Bytes  
def d_drive():

    d_drive = list(psutil.disk_usage('D:/'))
    total = d_drive[0]
    total = total // 10**12
    used = d_drive[1]
    used = used // 10**9
    free = d_drive[2]
    free = free // 10**9
    percent = d_drive[3]

    print("D drive storage status:")
    print(">> Total space: ",total,"TB")
    print(">> Used space: ",used, "GB")
    print(">> Free Space: ",free, "GB")
    print(">> Used space percentage: ",percent,"%")
    speak("Here are D drive storage status")


# --------RAM FUNCTION---------
# Working: It tells total, used and available space of RAM in Giga Bytes and used memory in percentage
def RAM():
    total_ram = psutil.virtual_memory()[0]
    total_ram = total_ram // 10**9
    available_ram = psutil.virtual_memory()[1]
    available_ram = available_ram // 10**9
    used_ram = psutil.virtual_memory()[3]
    used_ram = used_ram // 10**9
    
    print('>> Total RAM:', total_ram,"GB")
    print('>> Used RAM:', used_ram,"GB")
    print('>> Available RAM:', available_ram,"GB")
    print('>> RAM memory used:', psutil.virtual_memory()[2],"%")
    speak("Here are the RAM status")


# --------INTERNET SPEED TEST FUNCTION---------
# Working: tells both uploadinng and downloading speed
def SpeedTest(query):
    import speedtest
    speed = speedtest.Speedtest()
    
    if 'uploading' in query:
        print("Checking uploading speed.....")
        speak("Checking uploading speed.....")
        uploading = speed.upload()
        correctUpload = int(uploading/800000)
        print("Uploading speed is " + str(correctUpload) + " mbp/s")
        speak("Uploading speed is " + str(correctUpload) + " m b p s")
    
    elif 'downloading' in query:
        print("Checking downloading speed.....")
        speak("Checking downloading speed.....")
        downloading = speed.download()
        correctDown = int(downloading/800000)
        print("Downloading speed is " + str(correctDown) + " mbp/s")
        speak("Downloading speed is " + str(correctDown) + " mbps")
    
    else:
        print("Checking internet speed.....")
        speak("Checking internet speed.....")
        uploading = speed.upload()
        correctUpload = int(uploading/800000)
        downloading = speed.download()
        correctDown = int(downloading/800000)
        print("Uploading speed is " + str(correctUpload) + " mbp/s and Downloading speed is "  + str(correctDown) + " mbp/s")
        speak("Uploading speed is " + str(correctUpload) + " m b p s and Downloading speed is " + str(correctDown) + " m b p s")
    

# --------MY LOCATION FUNCTION---------
# Working: Tells your current city and country name
def my_location():
    ip_address = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_address + '.json'
    geo_q = requests.get(url)      
    geo_d = geo_q.json()
    city = geo_d['city']
    country = geo_d['country']
    print("Your are currently at " + city + ", " + country)
    speak("Your are currently at, " + city + "," + country)


# --------LOCATION DETAILS FUNCTION---------
# Working: Tells your current location details
def location_details():
    ip_address = requests.get('https://api.ipify.org').text        
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_address + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json()
    
    city = geo_d['city']
    state = geo_d['region']
    country = geo_d['country']
    longitude = geo_d['longitude']
    latitude = geo_d['latitude']
    country_code = geo_d['country_code']
    continent = geo_d['continent_code']
    timezone = geo_d['timezone']
    
    print ('>> City: ' + city)
    print ('>> State: ' + state)
    print ('>> Country: ' + country)
    print ('>> Logitude: ' + longitude)
    print ('>> Latitude: ' + latitude)
    print ('>> Country code: ' + country_code)
    print ('>> Continent code: ' + continent)
    print ('>> Time Zone: ' + timezone)
    speak("Here are the location details boss")