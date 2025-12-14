
class TV:
   def __init__(self, channel_no):
      self.is_on = False
      self.channel_no = channel_no
   def turn_off(self):
      self.is_on = False
   def turn_on(self):
      self.is_on = True

   def show_status(self):
     if self.is_on:
       print(f"Your Tv is on , ", "Channel",self.channel_no)
     else:
        print("Your TV is off")
    
   

