#!/usr/bin/env python# 2017 Christmas Lights Program 
# by Andre Petrov
# credits to Adeept for use of Matrix Keyboard code &
# credits to Adafruit for use of their LCD code
import lcd # importing module for lcd operationimport matrixkeyboard # importing module for keyboard operationimport RPi.GPIO as GPIO # importing module for RPi pins input/outputimport time # importing standard Python time libraryimport sys # importing standard Python system library
GPIO.setmode(GPIO.BCM) # setting input/output mode to BCM formatmykp = matrixkeyboard.keypad() # naming keypad function from module to work in this modulemylcd = lcd.Adafruit_CharLCD(GPIO = GPIO) # naming LCD function from module to work in this module
def xmasleds(): #defining function for LEDs activation (there are 3 LEDs on board)    pins = [26,20,21] #BCM values for last remaining GPIO pins to fit in 3 LEDs on breadboard    for i in range(10): #loop to run LEDs 10 times in sequence         for pin in pins:            GPIO.setup(pin, GPIO.OUT)   # Set LED pins' mode as output            GPIO.output(pin, GPIO.LOW) #  each LED is on             time.sleep(0.2) #short time delay between each LED being on            GPIO.output(pin, GPIO.HIGH) # each LED is offwhile True:  # initialising a loop to accept user's input of a year (4 digits)    year = ''    mylcd.clear() # reseting LCD    mylcd.message("Type 4 digits of\na year in keypad") # prompting user to enter 4 digits
    while len(year) < 4 : # another loop to accept 4 digits        digit = None        while digit == None:            digit = mykp.getKey() #accepting user input on matrix keyboard            time.sleep(0.2) # short delay between inputs        number = str(digit) # building a string of 4 digits         year = year + number # renaming it a 'year'        mylcd.clear() # clearing LCD        mylcd.message(year) # displaying the year in LCD        print year # printing year in terminal
    year = int(year) # year becomes integer from string
    if year == 2017: # matching the integer with '2017'        mylcd.clear() #clearing LCD        mylcd.message("Hooray!!!\nMerry Xmas !!!") # Message displayed on LCD        xmasleds() # running the function in lines 17-24 (LEDs go on in sequence 10 times)        time.sleep(2) #short delay
        
    elif year < 2017: # comparing the integer with '2017', if the integer is less than 2017        diff = 2017 - year # calculating the difference of the integer with '2017'        message = "Come back in\n{} years".format(diff) # message to come back in X years X being the difference with 2017        mylcd.clear() # clearing LCD        mylcd.message(message) # displaying the message        time.sleep(2) #short delay
    elif year > 2017: # comparing the integer with '2017', if the integer is more than 2017        diff = year - 2017 # calculating the difference of the integer with '2017'        message = "Go back in time\n{} years".format(diff)        mylcd.clear() # clearing LCD        mylcd.message(message) # displaying the message        time.sleep(2) #short delay
    mylcd.clear() # clearing LCD    mylcd.message("Press 0 to exit\nor any key") # message allowing to EXIT after each scenario above    digit = None
    while digit == None: # waiting for an input "0" = break out of loop, "anykey" = continue loop        digit = mykp.getKey() # accepting input        time.sleep(0.2) #short delay
    if digit == 0: #break out of loop,        mylcd.clear() # clearing LCD
        mylcd.message("Good Bye !") # displaying the message
        time.sleep(2) #short delay
        mylcd.clear() # clearing LCD
        sys.exit() # calling exit function from sys module to end the program
