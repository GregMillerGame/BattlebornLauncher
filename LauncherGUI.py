import os
import subprocess
import PySimpleGUI as sg
import sys

global MapValue, CharacterValue, Maps, Characters
ClientPath = "rebornlauncher_scuffed.exe"

def LaunchNow(MapID,CharacterID,autoClose):
    print("Checking values...")
    print("Current Map: " + str(Maps[MapID-1]) + "\nCurrent Character: " + str(Characters[CharacterID-1]))
    return_code = subprocess.call("(echo " + str(MapID) + " && echo " + str(CharacterID) + ") | rebornlauncher_scuffed.exe", shell=True)
    print("Starting ReBorn...")


Maps = ('Prologue', 'The Algorithm', "Void's Edge", 'The Renegade', 'The Archive', 'Sentinel', 'The Experiment',"The Sabotuer","Heliophage","Atticus and the Thrall Rebellion","Toby's Friendship Raid","Oscar Mike vs the Battleschool","Montana and the Demon Bear","Pheobe and the Heart of Ekkunar")
Characters = ("Alani", "Ambra", "Attikus", "Beatrix", "Benedict", "Boldur","Caldarius","Deande", "El Dragon", "Ernest", "Galilea", "Ghalt", "ISIC", "Kelvin", "Kid Ultra", "Kleese", "Marquis", "Mellka", "Miko", "Montana", "Orendi", "Oscar Mike", "Pendles", "Phoebe", "Rath", "Reyna", "Shayne & Aurox","Thorn","Toby","Whiskey Foxtrot")



menu_def = [['&Settings', ['&Properties', 'E&xit']],
            ['&Info', ['&About...','&Help']]]

layout = [sg.Menu(menu_def),
          [sg.Text("Map Selector: ", size=(28, 1)),sg.Text("Character Selector: ", size=(28, 1))],
          [sg.Listbox(Maps, size=(30, 10), enable_events=True,key='-Map-'),sg.Listbox(Characters, enable_events=True,size=(30, 10), key='-Character-')],
          [sg.Button('Start Game!'),sg.Checkbox("Auto-close launcher:",key="CloseLauncher")],
          [sg.Output(s=(100, 10),font="Consolas")]],

sg.MENU_RIGHT_CLICK_README = ['', ['Help', 'About...', 'Exit']]



# Create the window
sg.theme("Black")
sg.theme_use_custom_titlebar = True
MapValue = 1
CharacterValue = 1

window = sg.Window('Bad Battleborn ReBorn Launcher', layout,right_click_menu=sg.MENU_RIGHT_CLICK_README)  # Part 3 - Window Defintion

# Display and interact with the Window
event, values = window.read()  # Part 4 - Event loop or Window.read call

# Do something with the information gathered
while True:
    #get input
    event, values = window.read()
    #get button inputs
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Select Launcher Folder':
        ClientPath = sg.popup_get_folder('Please enter a file name')
        sg.popup('Launcher Successfully added!', 'Current Launcher is:', ClientPath)
        window["filePathBox"].update(ClientPath)
    elif event == "About...":
        sg.popup('Bad Battleborn ReBorn Launcher by Greg Miller \n Version 0.1')
    elif event == "Help":
        sg.popup('Steps to use: \n - Put in same folder as ReBorn \n - Select Map and Character \n - Hit Play!')
    #Character Select
    if event == "-Character-":
        if values['-Character-']:
            for position, item in enumerate(Characters):
                if item == values['-Character-'][0]:
                    CharacterValue = position + 1
                    print("You have selected: " + Characters[CharacterValue-1] + " as the Character!")
        # Character Select
    if event == "-Map-":
        if values['-Map-']:
            for position, item in enumerate(Maps):
                if item == values['-Map-'][0]:
                    MapValue = position + 1
                    print("You have selected: " + Maps[MapValue-1] + " as the Map!")
    elif event == 'Start Game!':
        if values['-Map-']:
            for position, item in enumerate(Maps):
                if item == values['-Map-'][0]:
                    MapValue = position + 1
        if values['-Character-']:
            for position, item in enumerate(Characters):
                if item == values['-Character-'][0]:
                    CharacterValue = position + 1
        window.perform_long_operation(lambda: LaunchNow(MapValue,CharacterValue,values["CloseLauncher"]), '-FUNCTION COMPLETED-')
    elif event == '-FUNCTION COMPLETED-':
        if values["CloseLauncher"]:
            sys.exit()





