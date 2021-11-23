from machine import Pin,Timer
from utime import sleep
import push_button
import micropython

micropython.alloc_emergency_exception_buf(100)
# Button
pButton=27

# Timer
pushButton_timer=Timer(0)

def myFunc1():
    print('I am a single click')
    
def myFunc2():
    print('I am a long click')

def myFunc3():
    print('I am a double click')

button=Pin(pButton, Pin.IN, Pin.PULL_UP)

pButton=push_button.push_button(button,myFunc1,myFunc2,myFunc3)

pushButton_timer.init(period=10, mode=Timer.PERIODIC, callback= pButton.check_button)

while True:
    sleep(1)