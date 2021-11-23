from utime import ticks_ms,ticks_diff#,sleep
from machine import Timer#,Pin

class push_button():
    def __init__(self,button,function_single_click=None,function_long_click=None,function_double_click=None):
        '''Object to assigne callback functions to certain button events

        button Pin
        function_single_click callback function for a single click
        function_long_click callback function for a long click
        function_double_click callback function for a double click'''
        
        self.button=button
        self.state=self.button.value()
        
        # set callback functions
        self.single_click_fnc=function_single_click
        self.long_click_fnc=function_long_click
        self.double_click_fnc=function_double_click
        
        # set default click time
        self.single_click=50
        self.long_click=1000
        self.double_click=400
        
        self.button_down=False
        self.button_up=True 
        self.counter=0
        self.counter_fst_click=0
        self.sng_click_timer=Timer(3)
        
    def set_click_times(self,single_click_ms,double_click_ms,long_click_ms):
        self.single_click=single_click_ms
        self.double_click=double_click_ms
        self.long_click=long_click_ms
    
    def check_button(self,p):
        if self.button.value()!= self.state and not(self.button_down) and self.button_up:
            self.button_down=True
            self.button_up=False
            self.counter=ticks_ms()

        elif self.button.value()== self.state:
            if ticks_diff(ticks_ms(),self.counter)>self.long_click and self.button_down:
                self.button_down=False
                self._long_click()
            elif ticks_diff(ticks_ms(),self.counter)>self.single_click and self.button_down:
                self.button_down=False
                if ticks_diff(ticks_ms(),self.counter_fst_click)>self.double_click:
                    
                    self.counter_fst_click=ticks_ms()
                    self.sng_click_timer.init(period=self.double_click-self.single_click, mode=Timer.ONE_SHOT, callback=self._single_click)
                else:
                    self.sng_click_timer.deinit()
                    self._double_click()
            
            self.button_up=True
            self.counter=ticks_ms()
            
    def _single_click(self,p):
        print('Single click')
        if not self.single_click_fnc==None:
            self.single_click_fnc()
     
    def _long_click(self):
        print('long click')
        if not self.long_click_fnc==None:
            self.long_click_fnc()
    
    def _double_click(self):
        print('double click')
        if not self.double_click_fnc==None:
            self.double_click_fnc()
        