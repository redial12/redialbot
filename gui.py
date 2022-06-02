from msilib import text
from shutil import which
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from turtle import color
from redialbot import botting, botting_captions, get_filename
from Person import Person

#clears all widgets inside frame called background
def clear():
    for widget in root.winfo_children():
        # print(widget.widgetName)
        if(widget.widgetName != "menu"):
            widget.destroy()

def welcomeScreen():
    clear()
    global currentScreen
    currentScreen = "welcome"
    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    redialBot = tk.Label(background, text="redialBOT", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    firstbutton = tk.Button(background, text = "Continue!", command= loginScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    greeting = tk.Message(background, width=1250, text= "Started out as a project to help find UT Austin students with similar interests, but turned into something versatile with the possibility for many different applications.", bg=primary_color, fg=tertiary_color, font=("Courier New", 25))
    introwidth = 0.15
    redialBot.place(relwidth= introwidth, relx= 0.5 - (introwidth/2), rely= 0.1)
    firstbutton.place(relwidth= 0.05, rely=0.70, relx= 0.5 - 0.025)
    greetwidth = 0.8
    greeting.place(relwidth = greetwidth, relx= 0.5 - greetwidth / 2, rely= 0.25)

def loginScreen():
    clear()
    global currentScreen
    currentScreen = "login"
    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    username = tk.Entry(background, bg=secondary_color, fg = tertiary_color, font=("Courier New", 25), textvariable=user_var)
    password = tk.Entry(background, bg=secondary_color, fg = tertiary_color, show="*", font=("Courier New", 25), textvariable=pass_var)
    page = tk.Entry(background, bg=secondary_color, fg = tertiary_color, font=("Courier New", 25), textvariable=page_var)
    userLabel = tk.Label(background, text="Username", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    passLabel = tk.Label(background, text="Password", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    pageLabel = tk.Label(background, text="Page", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    secondbutton = tk.Button(background, text = "Enter!", command= pickScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    backbutton = tk.Button(background, text = "Back", command= welcomeScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    username.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.2)
    userLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.15)
    password.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.4)
    passLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.35)
    page.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.6)
    pageLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.55)
    secondbutton.place(relwidth= 0.05, rely=0.8, relx= 0.5 - 0.025)
    backbutton.place(relwidth= 0.04, rely=0.85, relx= 0.5 - 0.02)
    
def pickScreen():
    global currentScreen
    global usernameGUI
    global passwordGUI
    global pageGUI
    global whichvar
    currentScreen = "pick"
    usernameGUI = user_var.get()
    passwordGUI = pass_var.get()
    pageGUI = page_var.get()
    whichvar = "caption"
    print("usernameGUI: " + usernameGUI)
    print("passwordGUI: " + passwordGUI)
    clear()

    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    #if any fields are empty, show msg box and go back to loginscreen
    if(usernameGUI == "" or passwordGUI == "" or pageGUI == ""):
        loginScreen()
        messagebox.showerror("Error!", "All fields must be completed!")
    else:
        backbutton = tk.Button(background, text = "Back", command= loginScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
        capbutton = tk.Button(background, text = "Caption", activebackground= "#6F8F96", bg = secondary_color, command = lambda: startScreen(), fg = tertiary_color)
        conbutton = tk.Button(background, text = "Condition", activebackground= "#6F8F96", bg = secondary_color, command = conditionScreen, fg = tertiary_color)
        capbutton.place(relwidth= 0.1, rely=0.5, relx= 0.5 - 0.15, relheight=0.05)
        conbutton.place(relwidth= 0.1, rely=0.5, relx= 0.5 + 0.05, relheight=0.05)
        backbutton.place(relwidth= 0.04, rely=0.85, relx= 0.5 - 0.02)

def conditionScreen():
    global currentScreen
    global usernameGUI
    global passwordGUI
    global pageGUI
    global whichvar
    currentScreen = "condition"
    usernameGUI = user_var.get()
    passwordGUI = pass_var.get()
    pageGUI = page_var.get()
    whichvar = "condition"
    print("usernameGUI: " + usernameGUI)
    print("passwordGUI: " + passwordGUI)
    clear()
    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    firstCon = tk.Entry(background, bg=secondary_color, fg = tertiary_color, font=("Courier New", 25), textvariable=first_var)
    secondCon = tk.Entry(background, bg=secondary_color, fg = tertiary_color, font=("Courier New", 25), textvariable=second_var)
    secondbutton = tk.Button(background, text = "Enter!", command= lambda: startScreen(), activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    backbutton = tk.Button(background, text = "Back", command= pickScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    firstLabel = tk.Label(background, text="First Term", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    secondLabel = tk.Label(background, text="Second Term", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    firstCon.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.3)
    secondCon.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.5)
    secondbutton.place(relwidth= 0.05, rely=0.8, relx= 0.5 - 0.025)
    backbutton.place(relwidth= 0.04, rely=0.85, relx= 0.5 - 0.02)
    firstLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.25)
    secondLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.45)

#TODO: *DONE* multiple data files that save with the current time
#TODO: *DONE* make a post counter along with the output (?/TOTAL) GET # OF POSTS USING SELENIUM
#TODO: *DONE* if file is empty, delete it
#TODO: *DONE* displays error message on start button if there are no values
#TODO: *DONE* file menu with quit button and other options
#TODO: *DONE* make scrollbar actually work
#TODO: *DONE* open data from old file
#TODO: *DONE* back button on output screen
#TODO: get the bot to scroll all the way down all devices
#TODO: functional with graphic instagram login screen
#TODO: light/dark mode using color variables
#TODO: autofill login info
#TODO: settings file
#TODO: await presence for like all elements LMAO
#TODO: must have first and second conditions

def startScreen():
    global currentScreen
    global usernameGUI
    global passwordGUI
    global pageGUI
    global firstconGUI
    global secondconGUI
    currentScreen = "start"
    firstconGUI = first_var.get()
    secondconGUI = second_var.get()
    print("firstconGUI: " + firstconGUI)
    print("secondconGUI: " + secondconGUI)
    clear()
    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    if(whichvar == "condition"):
        startbutton = tk.Button(background, text = "Start Conditions!", activebackground= "#6F8F96", bg = secondary_color, command= lambda: botting(usernameGUI, passwordGUI, pageGUI, firstconGUI, secondconGUI), fg = tertiary_color)
        backbutton = tk.Button(background, text = "Back", command= conditionScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    elif(whichvar == "caption"):
        startbutton = tk.Button(background, text = "Start Captions!", activebackground= "#6F8F96", bg = secondary_color, command= lambda: botting_captions(usernameGUI, passwordGUI, pageGUI), fg = tertiary_color)
        backbutton = tk.Button(background, text = "Back", command= pickScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    
    resultsButton = tk.Button(background, text = "See results!", activebackground= "#6F8F96", bg = secondary_color, command= lambda: finishScreen(False), fg = tertiary_color)
    resultsButton.place(relwidth= 0.08, rely=0.675, relx= 0.5 - 0.04, relheight=0.05)
        
    startbutton.place(relwidth= 0.1, rely=0.5, relx= 0.5 - 0.05, relheight=0.05)
    backbutton.place(relwidth= 0.04, rely=0.85, relx= 0.5 - 0.02)

#displays after program is done running, displays output/results
def finishScreen(open_file):
    global currentScreen
    currentScreen = "finish"
    clear()
    background = tk.Frame(root, width= screen_width, height= screen_height, background=primary_color, cursor="circle")
    background.pack()
    global file
    global file_name
    if(open_file == False):
        file_name = get_filename()
        file = open(file_name, "rt", encoding="utf-8")
    else:
        file_name = filedialog.askopenfilename()
        file = open(file_name, "rt", encoding="utf-8")
    filetext = file.read()
    outputLabel = tk.Label(background, text="Output", font=("Courier New", 25), background=primary_color, fg = tertiary_color)
    textoutput = tk.Text(background, font=("Courier New", 10), background=primary_color, fg = tertiary_color)
    textoutput.insert(tk.INSERT, filetext)
    scrollbar = tk.Scrollbar(textoutput, command = textoutput.yview)
    backbutton = tk.Button(background, text = "Back", command= loginScreen, activebackground= "#6F8F96", bg = secondary_color, fg = tertiary_color)
    scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
    textoutput['yscrollcommand'] = scrollbar.set
    outputLabel.place(relwidth=0.15, relx = 0.5 - 0.075, rely=0.10)
    textoutput.place(relwidth=0.8, relx = 0.5 - 0.4, rely=0.15, relheight=0.6)
    backbutton.place(relwidth= 0.04, rely=0.85, relx= 0.5 - 0.02)

def toggleLightMode():
    global primary_color
    global secondary_color
    global tertiary_color
    global toggleLightBool
    global currentScreen
    if(not toggleLightBool):
        primary_color = "#f7f7f7"
        secondary_color = "#99aab5"
        tertiary_color = "#000000"
        toggleLightBool = True
    else:
        primary_color = "#121212"
        secondary_color = "#4D4D4D"
        tertiary_color = "#FAFAFA"
        toggleLightBool = False

    getCurrentScreen(currentScreen)
    
    
def getCurrentScreen(current):
    match current:
        case "welcome":
            return welcomeScreen()
        case "login":
            return loginScreen()
        case "pick":
            return pickScreen
        case "condition":
            return conditionScreen()
        case "start":
            return startScreen()
        case "finish":
            return finishScreen()

global root
global screen_width
global screen_height
global background
global primary_color
global secondary_color
global tertiary_color
global toggleLightBool
global whichvar
global currentScreen
usernameGUI = ""
passwordGUI = ""
pageGUI = ""
firstconGUI = ""
secondconGUI = ""
primary_color = "#121212"
secondary_color = "#4D4D4D"
tertiary_color = "#FAFAFA"
toggleLightBool = False
root = tk.Tk(className = 'redialBOT')
root.state('zoomed')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
user_var = tk.StringVar(root, value="")
pass_var = tk.StringVar(root, value="")
page_var = tk.StringVar(root, value="")
first_var = tk.StringVar(root, value="")
second_var = tk.StringVar(root, value="")
welcomeScreen()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
settingsmenu = tk.Menu(menubar, tearoff=0)

filemenu.add_command(label="New", command=loginScreen)
filemenu.add_command(label="Open", command = lambda: finishScreen(True))
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

settingsmenu.add_command(label="Toggle Light Mode", command=toggleLightMode)
settingsmenu.add_checkbutton(label="Remember Login")
menubar.add_cascade(label = "Settings", menu=settingsmenu)
root.config(menu = menubar)
root.mainloop()
