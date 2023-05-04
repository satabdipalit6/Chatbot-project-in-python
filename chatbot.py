from tkinter import *
from tkinter import ttk
import os
import sys
import webbrowser



def main():

    win=Tk()
    app=welcome_window(win)
    win.mainloop()



class welcome_window:
    def __init__(self,root):
       self.root=root
       self.root.title("Welcome screen")
       self.root.geometry('925x500+300+200')
       self.root.configure(bg="yellow")

       #######---------------Contains of Welcome screen----------------------######################

       self.root.lbl1=Label(root,text="***WELCOME TO BEST***",font=("Arial", 15),bg="red",borderwidth=20,relief="solid",width=112,height=8).grid()
       self.root.lbl2=Label(root,text="                     ",font=("Times,120"),bg="yellow").grid()
       self.root.lbl3=Label(root,text="ANY QUERIES???",font=("Times,80"),bg="green",borderwidth=5,relief="solid",width=50,height=3).grid()
       self.root.lbl4=Label(root,text="                     ",font=("Times,120"),bg="yellow").grid()
       self.root.lbl5=Label(root,text="NO WORRIES OUR INCREDIBLE IS HERE!!!",font=("Times,100"),bg="orange",borderwidth=5,relief="solid",width=50,height=3).grid()
       self.root.lbl6=Label(root,text="                     ",font=("Times,120"),bg="yellow").grid()
       self.root.btn1=Button(root,text="ASK QUESTION!",bg="pink",font=("Calibri",12,"bold"),borderwidth=5,relief="solid",command=self.chatbot).grid() 
       self.root.lbl7=Label(root,text="click on ask question to move ahead>>>",font=("Times,120"),bg="light green",borderwidth=5,relief="solid",width=50,height=3).grid()
       self.root.lbl8=Label(root,text="                     ",font=("Times,120"),bg="yellow").grid()
       self.root.lbl9=Label(root,text="DEVELOPED BY Computer Science & Engg Department",font=("Calibri",16,"bold"),bg="light blue",borderwidth=2,relief="solid",width=110,height=2).grid()
    
    def chatbot(self):

            self.new_window=Toplevel(self.root)
            self.app= chatbot(self.new_window)
            



class chatbot:


    def __init__(self,root):

        self.root=root
        self.root.title("Welcome To Chatbot ")   
        self.root.geometry("1366x768+0+0")
        self.root.config (bg='pink')  
        self.root.lbl10=Label(root,text="EVERY ANSWER TO YOUR QUESTION IS HERE!!!",font=("Arial", 15),bg="yellow",borderwidth=20,relief="solid",width=112,height=8).grid()
        # self.root.btn1=Button(root,text="ASK QUESTION!",bg="Green",font=("Calibri",12,"bold"),borderwidth=5,relief="solid",command=self.link).grid()
        self.root.my_link=Label(root,text="BEST CSE Chatbot",fg='red',cursor='hand2',font=('Arial',20,'underline'))
        self.root.my_link.grid(row=15,column=0,padx=20,pady=20)
        self.root.bind('<Button-1>',lambda x:webbrowser.open_new("https://bot.dialogflow.com/68bf6ba8-189c-45c6-9470-a91ae49cffa4"))
        # self.root.lbl20=Label(root,text="DEVELOPED BY Computer Science & Engg Department",font=("Calibri",16,"bold"),bg="light blue",borderwidth=2,relief="solid",width=110,height=2).grid()
        # self.root.lbl20.grid(row=130,column=0,padx=20,pady=20)

if __name__ == "__main__":

       main()