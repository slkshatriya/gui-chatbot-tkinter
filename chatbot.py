from tkinter import *                       
from random import choice                       
                                    
ask   = ["hi", "hello"]                         
hi    = ["hi", "hello"]
sq = ["whatsup", "kya kar rahe ho"]
rp = ["nothing u say", "kuch nhi ap btao"]
hr = ["who are you", "what is your name"]
rh = ["i am a chatbot created by suraj singh"] 
emotion = ["i like you","i love you"]
express = ["i like you too"]                                         #you can add more conversation whatever you like 
error = ["sorry, i don't know", "what u said?","can't recognise" ]            
                                                                    
root = Tk()                             
user = StringVar()                          
bot  = StringVar()                          
                                    
root.title("SurajsBot ")                  
Label(root, text=" user : ").pack(side=LEFT)                
Entry(root, textvariable=user).pack(side=LEFT)          
Label(root, text=" Bot  : ").pack(side=LEFT)                
Entry(root, textvariable=bot).pack(side=LEFT)               
                            
                                
def main():                             
       question = user.get()                        
       if question in ask:                      
             bot.set(choice(hi))
       elif question in sq:
           bot.set(choice(rp))
       elif question in hr:
           bot.set(choice(rh))
       elif question in emotion:
           bot.set(choice(express))
       else:                                
             bot.set(choice(error))                 
                                
Button(root, text="speak", command=main).pack(side=LEFT)        
                                    
mainloop()                              

