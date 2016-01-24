import webiopi
import datetime

GPIO = webiopi.GPIO

LIGHT18 = 18 # GPIO pin using BCM numbering

HOUR_ON_18  = 8  # Turn Light ON at 08:00
MINUTE_ON_18 = 25
HOUR_OFF_18 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_18 = 25

LIGHT23 = 23 # GPIO pin using BCM numbering
HOUR_ON_23  = 8  # Turn Light ON at 08:00
MINUTE_ON_23 =
HOUR_OFF_23 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_23 =

LIGHT24 = 24 # GPIO pin using BCM numbering
HOUR_ON_24  = 8  # Turn Light ON at 08:00
MINUTE_ON_24 =
HOUR_OFF_24 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_24 =

LIGHT25 = 25 # GPIO pin using BCM numbering
HOUR_ON_25  = 8  # Turn Light ON at 08:00
MINUTE_ON_25=
HOUR_OFF_25 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_25=

LIGHT8 = 8 # GPIO pin using BCM numbering
HOUR_ON_8  = 8  # Turn Light ON at 08:00
MINUTE_ON_8 =
HOUR_OFF_8 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_8 =

LIGHT7 = 7 # GPIO pin using BCM numbering
HOUR_ON_7  = 8  # Turn Light ON at 08:00
MINUTE_ON_7 = 
HOUR_OFF_7 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_7 =

LIGHT20 = 20 # GPIO pin using BCM numbering
HOUR_ON_20  = 8  # Turn Light ON at 08:00
MINUTE_ON_20 =
HOUR_OFF_20 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_20 =

LIGHT21 = 21 # GPIO pin using BCM numbering
HOUR_ON_21  = 8  # Turn Light ON at 08:00
MINUTE_ON_21 =
HOUR_OFF_21 = 18 # Turn Light OFF at 18:00
MINUTE_OFF_21 =

# setup function is automatically called at WebIOPi startup
def setup():
    # set the GPIO used by the light to output
    GPIO.setFunction(LIGHT18, GPIO.OUT)
    GPIO.setFunction(LIGHT23, GPIO.OUT)
    GPIO.setFunction(LIGHT24, GPIO.OUT)
    GPIO.setFunction(LIGHT25, GPIO.OUT)
    GPIO.setFunction(LIGHT8, GPIO.OUT)
    GPIO.setFunction(LIGHT7, GPIO.OUT)
    GPIO.setFunction(LIGHT20, GPIO.OUT)
    GPIO.setFunction(LIGHT21, GPIO.OUT)

    # retrieve current datetime
    now = datetime.datetime.now()

    # test if we are between ON time and tun the light ON
    if ((now.hour >= HOUR_ON_18) and (now.hour < HOUR_OFF_18)):
        GPIO.digitalWrite(LIGHT18, GPIO.HIGH)

    if ((now.hour >= HOUR_ON_23) and (now.hour < HOUR_OFF_23)):
        GPIO.digitalWrite(LIGHT23, GPIO.HIGH)
	
    if ((now.hour >= HOUR_ON_24) and (now.hour < HOUR_OFF_24)):
        GPIO.digitalWrite(LIGHT24, GPIO.HIGH)

    if ((now.hour >= HOUR_ON_25) and (now.hour < HOUR_OFF_25)):
        GPIO.digitalWrite(LIGHT25, GPIO.HIGH)

    if ((now.hour >= HOUR_ON_8) and (now.hour < HOUR_OFF_8)):
        GPIO.digitalWrite(LIGHT8, GPIO.HIGH)

    if ((now.hour >= HOUR_ON_7) and (now.hour < HOUR_OFF_7)):
        GPIO.digitalWrite(LIGHT7, GPIO.HIGH)
	
    if ((now.hour >= HOUR_ON_20) and (now.hour < HOUR_OFF_20)):
        GPIO.digitalWrite(LIGHT20, GPIO.HIGH)

    if ((now.hour >= HOUR_ON_21) and (now.hour < HOUR_OFF_21)):
        GPIO.digitalWrite(LIGHT21, GPIO.HIGH)

# loop function is repeatedly called by WebIOPi 
def loop():
    # retrieve current datetime
    now = datetime.datetime.now()

    # toggle light ON all days at the correct time
    if ((now.hour == HOUR_ON_18) and (now.minute == MINUTE_ON_18)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT18) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT18, GPIO.LOW)

    if ((now.hour == HOUR_ON_23) and (now.minute == MINUTE_ON_23)): #and (now.second == 0)):
    	if (GPIO.digitalRead(LIGHT23) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT23, GPIO.LOW)

    if ((now.hour == HOUR_ON_24) and (now.minute == MINUTE_ON_24)): # and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT24) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT24, GPIO.LOW)

    if ((now.hour == HOUR_ON_25) and (now.minute == MINUTE_ON_25) #and (now.second == 0)):
    	if (GPIO.digitalRead(LIGHT25) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT25, GPIO.LOW)

    if ((now.hour == HOUR_ON_8) and (now.minute == MINUTE_ON_8)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT8) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT8, GPIO.LOW)

    if ((now.hour == HOUR_ON_7) and (now.minute == MINUTE_ON_7)): #and (now.second == 0)):
    	if (GPIO.digitalRead(LIGHT7) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT7, GPIO.LOW)

    if ((now.hour == HOUR_ON_20) and (now.minute == MINUTE_ON_20)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT20) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT20, GPIO.LOW)

    if ((now.hour == HOUR_ON_21) and (now.minute == MINUTE_ON_21)): #and (now.second == 0)):
    	if (GPIO.digitalRead(LIGHT21) == GPIO.HIGH):
            GPIO.digitalWrite(LIGHT21, GPIO.LOW)
    
	####################### toggle light OFF ##################
    if ((now.hour == HOUR_OFF_18) and (now.minute == MINUTE_OFF_18): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT18) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT18, GPIO.HIGH)

    if ((now.hour == HOUR_OFF_23) and (now.minute == MINUTE_OFF_23)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT23) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT23, GPIO.HIGH)
	
    if ((now.hour == HOUR_OFF_24) and (now.minute == MINUTE_OFF_24)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT24) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT24, GPIO.HIGH)

    if ((now.hour == HOUR_OFF_25) and (now.minute == MINUTE_OFF_25)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT25) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT25, GPIO.HIGH)
	
    if ((now.hour == HOUR_OFF_8) and (now.minute == MINUTE_OFF_8)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT8) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT8, GPIO.HIGH)

    if ((now.hour == HOUR_OFF_7) and (now.minute == MINUTE_OFF_7)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT7) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT7, GPIO.HIGH)
	
    if ((now.hour == HOUR_OFF_20) and (now.minute == MINUTE_OFF_20)): and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT20) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT20, GPIO.HIGH)

    if ((now.hour == HOUR_OFF_21) and (now.minute == MINUTE_OFF_21)): #and (now.second == 0)):
        if (GPIO.digitalRead(LIGHT21) == GPIO.LOW):
            GPIO.digitalWrite(LIGHT21, GPIO.HIGH)

    # gives CPU some time before looping again
    webiopi.sleep(1)

# destroy function is called at WebIOPi shutdown
def destroy():
    GPIO.digitalWrite(LIGHT18, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT23, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT24, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT25, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT8, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT7, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT20, GPIO.HIGH)
    GPIO.digitalWrite(LIGHT21, GPIO.HIGH)

