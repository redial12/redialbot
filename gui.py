import tkinter as tk
from redialbot import botting

def clear():
    for widget in background.winfo_children():
        widget.destroy()

def firstScreen():
    redialBot = tk.Label(background, text="redialBOT", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    firstbutton = tk.Button(background, text = "Continue!", command= secondScreen, activebackground= "#6F8F96", bg = "#4D4D4D")
    greeting = tk.Message(background, width=1250, text= "Started out as a project to help find UT Austin students with similar interests, but turned into something versatile with the possibility for many different applications.", bg="#121212", fg="#FAFAFA", font=("Courier New", 25))
    background.pack()
    introwidth = 0.15
    redialBot.place(relwidth= introwidth, relx= 0.5 - (introwidth/2), rely= 0.1)
    firstbutton.place(relwidth= 0.05, rely=0.70, relx= 0.5 - 0.025)
    greetwidth = 0.8
    greeting.place(relwidth = greetwidth, relx= 0.5 - greetwidth / 2, rely= 0.25)

def secondScreen():
    clear()
    username = tk.Entry(background, bg="#4D4D4D", fg = "#FAFAFA", font=("Courier New", 25), textvariable=user_var)
    password = tk.Entry(background, bg="#4D4D4D", fg = "#FAFAFA", show="*", font=("Courier New", 25), textvariable=pass_var)
    page = tk.Entry(background, bg="#4D4D4D", fg = "#FAFAFA", font=("Courier New", 25), textvariable=page_var)
    userLabel = tk.Label(background, text="Username", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    passLabel = tk.Label(background, text="Password", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    pageLabel = tk.Label(background, text="Page", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    secondbutton = tk.Button(background, text = "Enter!", command= thirdScreen, activebackground= "#6F8F96", bg = "#4D4D4D")
    username.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.2)
    userLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.15)
    password.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.4)
    passLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.35)
    page.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.6)
    pageLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.55)
    secondbutton.place(relwidth= 0.05, rely=0.8, relx= 0.5 - 0.025)
    
def thirdScreen():
    global usernameGUI
    global passwordGUI
    global pageGUI
    usernameGUI = user_var.get()
    passwordGUI = pass_var.get()
    pageGUI = page_var.get()
    print("usernameGUI: " + usernameGUI)
    print("usernameGUI: " + passwordGUI)
    clear()
    firstCon = tk.Entry(background, bg="#4D4D4D", fg = "#FAFAFA", font=("Courier New", 25), textvariable=first_var)
    secondCon = tk.Entry(background, bg="#4D4D4D", fg = "#FAFAFA", font=("Courier New", 25), textvariable=second_var)
    secondbutton = tk.Button(background, text = "Enter!", command= fourthScreen, activebackground= "#6F8F96", bg = "#4D4D4D")
    firstLabel = tk.Label(background, text="First Term", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    secondLabel = tk.Label(background, text="Second Term", font=("Courier New", 25), background="#121212", fg = "#FAFAFA")
    firstCon.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.3)
    secondCon.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.5)
    secondbutton.place(relwidth= 0.05, rely=0.8, relx= 0.5 - 0.025)
    firstLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.25)
    secondLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.45)

def fourthScreen():
    global usernameGUI
    global passwordGUI
    global pageGUI
    global firstconGUI
    global secondconGUI
    firstconGUI = first_var.get()
    secondconGUI = second_var.get()
    print("firstconGUI: " + firstconGUI)
    print("secondconGUI: " + secondconGUI)
    clear()
    startbutton = tk.Button(background, text = "Start!", activebackground= "#6F8F96", bg = "#4D4D4D", command= lambda: botting(usernameGUI, passwordGUI, pageGUI, firstconGUI, secondconGUI))
    startbutton.place(relwidth= 0.1, rely=0.5, relx= 0.5 - 0.05, relheight=0.05)

global root
global screen_width
global screen_height
global background
usernameGUI = ""
passwordGUI = ""
pageGUI = ""
firstconGUI = ""
secondconGUI = ""
root = tk.Tk(className = 'redialBOT')
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
background = tk.Frame(root, width= screen_width, height= screen_height, background="#121212", cursor="circle")
user_var = tk.StringVar(root, value="")
pass_var = tk.StringVar(root, value="")
page_var = tk.StringVar(root, value="")
first_var = tk.StringVar(root, value="")
second_var = tk.StringVar(root, value="")
firstScreen()
root.mainloop()
