from tkinter import *
from array import *
import time, os, sys

#Stores the option menu for later
equips = list()
for i in range(0,6):
    equips.append([])
    for j in range (0,10):
        equips[i].append(0)

#Stores the stats to be displayed
stats = list()
for i in range(0,9):
    stats.append(0)

#Character class
class Character():
    def __init__(self):
        self.name = 'Yuna'
        self.level = '50'
        self.star = '5'
        self.awake = '5'
        self.attack = '742'
        self.defense = '446'
        self.health = '4074'
        self.speed = '112'
        self.critC = '15%'
        self.critD = '150%'
        self.effect = '0'
        self.resist = '0'
        self.dual = '5%'
        
#Edited optionMenu
class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master) #This has to be StringVar so that the name can change when option selected
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(indicatoron=0, font=("Arial", 10), bg="#000000", fg="#AAAAAA", height=1, width=11, activebackground="grey") #turn off the weird box and change the look
        self['menu'].config(font=("Arial", 10), bg="#000000", fg="#AAAAAA")
        self["highlightthickness"]=0

    #Get the current selected option
    def get(self):
        return self.var.get()

    def set(self, name):
        self.var.set(name)

#This function takes care of when we swap between heroes
#def swap

#This function takes care of the UI for the equipments
def createEquip(self, name, main_name, main_value, sub1_name, sub1_value, sub2_name, sub2_value, sub3_name, sub3_value, sub4_name, sub4_value):
    subtitle = Label(self, text=name, font=("Arial", 10), bg="black", fg="red")
    subtitle.grid(columnspan=2)

    #list to store the stat names used in creation of the equips tab
    current_equips = [main_name, main_value, sub1_name, sub1_value, sub2_name, sub2_value, sub3_name, sub3_value, sub4_name, sub4_value]
    
    #Left side
    if (name == "Weapon" or name == "Helmet" or name == "Armor"):
        if (name == "Weapon"):
            pos = 0
            equips[pos][0] = Label(self, text="Attack", font=("Arial bold", 11), height=1, width=10, bg="#000000", fg="White")
            equips[pos][0].grid(row=1, sticky=W) #row=1 cuz 0 is the subtitle
            #For each substat
            for i in range(1,5):
                equips[pos][i*2] = MyOptionMenu(self, "Sub", "Attack", "Health", "Speed", "CritC", "CritD", "Effect", "Resist")
                equips[pos][i*2].set(current_equips[i*2])
                equips[pos][i*2].grid(row=i*2, sticky=W)
                equips[pos][i*2+1] = Entry(self, width=8)
                equips[pos][i*2+1].insert(END, current_equips[i*2+1])
                equips[pos][i*2+1].config(font=("Arial", 10), bg="#000000", fg="#AAAAAA", insertbackground='white', justify=RIGHT)
                #insertbackground changes the color of the cursor
                equips[pos][i*2+1].grid(row=i*2, column=1)
            
        elif (name == "Helmet"):
            pos = 1
            equips[pos][0] = Label(self, text="Health", font=("Arial bold", 11), height=1, width=10, bg="#000000", fg="White")
            equips[pos][0].grid(row=1, sticky=W)
            #For each substat
            for i in range(1,5):
                equips[pos][i*2] = MyOptionMenu(self, "Sub", "Attack", "Health", "Defense", "Speed", "CritC", "CritD", "Effect", "Resist")
                equips[pos][i*2].set(current_equips[i*2])
                equips[pos][i*2].grid(row=i*2, sticky=W)
                equips[pos][i*2+1] = Entry(self, width=8)
                equips[pos][i*2+1].insert(END, current_equips[i*2+1])
                equips[pos][i*2+1].config(font=("Arial", 10), bg="#000000", fg="#AAAAAA", insertbackground='white', justify=RIGHT)
                equips[pos][i*2+1].grid(row=i*2, column=1)
                
        else:
            pos = 2
            main_L = Label(self, text="Defense", font=("Arial bold", 11), height=1, width=10, bg="#000000", fg="White")
            main_L.grid(row=1, sticky=W)
            #For each substat
            for i in range(1,5):
                equips[pos][i*2] = MyOptionMenu(self, "Sub", "Health", "Defense",  "Speed", "CritC", "CritD", "Effect", "Resist")
                equips[pos][i*2].set(current_equips[i*2])
                equips[pos][i*2].grid(row=i*2, sticky=W)
                equips[pos][i*2+1] = Entry(self, width=8)
                equips[pos][i*2+1].insert(END, current_equips[i*2+1])
                equips[pos][i*2+1].config(font=("Arial", 10), bg="#000000", fg="#AAAAAA", insertbackground='white', justify=RIGHT)
                equips[pos][i*2+1].grid(row=i*2, column=1)

        #Here we have even index gives name and odd index gives value
        #Main stat
        equips[pos][1] = Entry(self, width=8)
        equips[pos][1].insert(END, str(current_equips[1]))
        equips[pos][1].config(font=("Arial", 11), bg="#000000", fg="white", insertbackground='white', width=7, justify=RIGHT)
        equips[pos][1].grid(row=1, column=1)

    #Right side
    else:
        if (name == "Necklace"):
            pos = 3
            equips[pos][0] = MyOptionMenu(self, "Main", "Attack", "Health", "Defense", "CritR", "CritD")
            equips[pos][0].config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
            equips[pos][0].set(current_equips[0])
            equips[pos][0].grid(row=1, sticky=W) #row=1 cuz 0 is the subtitle
            
        elif (name == "Ring"):
            pos = 4
            equips[pos][0] = MyOptionMenu(self, "Main", "Attack", "Health", "Defense", "Effect", "Resist")
            equips[pos][0].config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
            equips[pos][0].set(current_equips[0])
            equips[pos][0].grid(row=1, sticky=W)
            
        else:
            pos = 5
            equips[pos][0] = MyOptionMenu(self, "Main", "Attack", "Health", "Defense", "Speed")
            equips[pos][0].config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
            equips[pos][0].set(current_equips[0])
            equips[pos][0].grid(row=1, sticky=W)

        equips[pos][1] = Entry(self, width=7)
        equips[pos][1].insert(END, str(current_equips[1]))
        equips[pos][1].config(font=("Arial", 11), bg="#000000", fg="white", insertbackground='white', justify=RIGHT)
        equips[pos][1].grid(row=1, column=1)
        
        for i in range(1,5):
            equips[pos][i*2] = MyOptionMenu(self, "Sub", "Attack", "Health", "Defense", "Speed", "CritC", "CritD", "Effect", "Resist")
            equips[pos][i*2].set(current_equips[i*2])
            equips[pos][i*2].grid(row=i*2, sticky=W)
            equips[pos][i*2+1] = Entry(self, width=8)
            equips[pos][i*2+1].insert(END, current_equips[i*2+1])
            equips[pos][i*2+1].config(font=("Arial", 10), bg="#000000", fg="#AAAAAA", insertbackground='white', justify=RIGHT)
            equips[pos][i*2+1].grid(row=i*2, column=1)

#This function saves the data on submission and changes the display values
def save():
    print('saving')
    file = open("./Data/Yuna.txt", 'w+')
    if (str(awake_E.get()) == '5'):
        hero.level = '50'
    else:
        hero.level = '60'
    file.write('Ice,'+ hero.level +',' + str(awake_E.get()) + ',' + str(awake_E.get()) +',Leo,\n')
    #left side
    for i in range(0,3):
        for j in range(1,10):
            file.write(equips[i][j].get() + ',')
        file.write('\n')
    #right side
    for i in range(3,6):
        for j in range(0,10):
            file.write(equips[i][j].get() + ',')
        file.write('\n')
    file.write(str(atk_E.get()) + ',' + str(hp_E.get()) + ',\n')
    file.write(str(set1.get()) + ',' + str(set2.get()) + ',' + str(set3.get()) + ',\n')
    file.close()

#This function applies the changes on submission
def submit():
    #make changes depending on hero
    print('submitting')
    #check for the character change
    if (hero.name != str(charaName.get())):
        print("changing")
        #change image + stats + equips
    #check
    hero.awake = str(awake_E.get())
    if (hero.awake == '5'):
        hero.level = '50'
        hero.star = '5'
##    #Awakening stats (this is true for all heroes)
##    if (int(hero.awake) > 0):
##        hero.attack = str(int(hero.attack) + 20)
##        hero.health = str(int(hero.health) + 60)
##    if (int(hero.awake) > 1):
##        hero.attack = str(int(hero.attack) + 20)
##        hero.health = str(int(hero.health) + 60)
##        if (int(hero.awake) > 2):
##            hero.attack = str(int(hero.attack) + 20)
##            hero.health = str(int(hero.health) + 60)
##            if (int(hero.awake) > 3):
##                hero.attack = str(int(hero.attack) + 30)
##                hero.health = str(int(hero.health) + 60)
##                if (int(hero.awake) > 4):
##                    hero.attack = str(int(hero.attack) + 30)
##                    hero.health = str(int(hero.health) + 60)
##                    if (int(hero.awake) > 5):
##                        hero.attack = str(int(hero.attack) + 30)
##                        hero.health = str(int(hero.health) + 60)

    #check for percentile and flat
##    for i in range(0,6):
##        for j in range(0,10):
##            equips[i][j]
    #do the changes
##    calc[0][0] = int(hero.attack)
    
    #Stat setup
##    for i in range(0,9):
##        stats[i]['text'] = str(calc[i][0]*calc[i][1] + calc[i][2])

#This function prints something on click
def printme():
    print("type in sub3 for weapon is:", equips[0][6].get())
    print('value of attack is:', attack)

def changeme():
    print('increased attack')
    attack = 2
    
#Start program
hero = Character()

root = Tk()
root.title("Epic 7 Equipment Simulator")
root["bg"] = "#000000"
root.resizable(0, 0) #make the window unresizable

###Status bar initialize
##status = Label(root, text="Program started", bd=1, relief=SUNKEN, anchor=W)
##status.pack(side=BOTTOM, fill=X)

#Title display
title = Label(root, text="Epic 7 Equipment Simulator", font=("Arial bold", 20), bg="#000000", fg="white")
title.grid(columnspan=3)

#Equipment Area
eArea = Frame(root)
eArea.grid(row=1)
eArea["bg"] = "#000000"

#Weapon stats
weapon = Frame(eArea)
createEquip(weapon, "Weapon",0,5,"Speed",6,"Resist",7,"Health",8,"Health",9)
weapon.grid(row=0, padx=20, pady=10) #pad adds space for the grid
weapon["bg"] = "#000000"

helmet = Frame(eArea)
createEquip(helmet, "Helmet",0,5,"Speed",6,"Resist",7,"Health",8,"Health",9)
helmet.grid(row=1,  padx=20, pady=10)
helmet["bg"] = "#000000"

armor = Frame(eArea)
createEquip(armor, "Armor",0,10,"Speed",11,"Resist",12,"Health",13,"Health",14)
armor.grid(row=2,  padx=20, pady=10)
armor["bg"] = "#000000"

necklace = Frame(eArea)
createEquip(necklace, "Necklace","Attack",0,"Speed",0,"Resist",0,"Health",0,"Health",0)
necklace.grid(row=0, column=1,  padx=20, pady=10)
necklace["bg"] = "#000000"

ring = Frame(eArea)
createEquip(ring, "Ring","Attack",0,"Speed",0,"Resist",0,"Health",0,"Health",0)
ring.grid(row=1, column=1,  padx=20, pady=10)
ring["bg"] = "#000000"

boots = Frame(eArea)
createEquip(boots, "Boots","Attack",0,"Speed",0,"Resist",0,"Health",0,"Health",0)
boots.grid(row=2, column=1,  padx=20, pady=10)
boots["bg"] = "#000000"

artifact = Frame(eArea)
artifact['bg'] = 'black'
artif_L = Label(artifact, text='Artifact', font=('arial', 10), bg='black', fg='red')
artif_L.grid(columnspan=4)
atk_L = Label(artifact, text='Attack', font=('arial bold', 11), bg='black', fg='white')
atk_L.grid(row=1)
atk_E = Entry(artifact, width=8)
atk_E.insert(END, 0)
atk_E.config(font=("Arial", 11), bg="#000000", fg="white", insertbackground='white')
atk_E.grid(row=1, column=1)
hp_L = Label(artifact, text='Health', font=('arial bold', 11), bg='black', fg='white')
hp_L.grid(row=1, column=2)
hp_E = Entry(artifact, width=8)
hp_E.insert(END, 0)
hp_E.config(font=("Arial", 11), bg="#000000", fg="white", insertbackground='white')
hp_E.grid(row=1, column=3)
artifact.grid(columnspan=2)

#Sets
setArea = Frame(eArea)
setArea['bg'] = 'black'
set_L = Label(setArea, text='Sets', font=("Arial bold", 11), bg="#000000", fg="white")
set_L.grid(columnspan=3)
set1 = MyOptionMenu(setArea, "Set1", "None", "Attack", "Health", "Defense", "Speed", "Critical", "Hit Rate", "Destruction", "Lifesteal", "Counter", "Resist", "Unity", "Rage", "Immunity")
set1.config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
set1.set("None")
set1.grid(row=1, padx=10)
setArea['bg'] = 'black'
set2 = MyOptionMenu(setArea, "Set1", "None", "Attack", "Health", "Defense", "Speed", "Critical", "Hit Rate", "Destruction", "Lifesteal", "Counter", "Resist", "Unity", "Rage", "Immunity")
set2.config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
set2.set("None")
set2.grid(row=1, column=1, padx=10)
setArea['bg'] = 'black'
set3 = MyOptionMenu(setArea, "Set1", "None", "Attack", "Health", "Defense", "Speed", "Critical", "Hit Rate", "Destruction", "Lifesteal", "Counter", "Resist", "Unity", "Rage", "Immunity")
set3.config(font=("Arial bold", 11), bg="#000000", fg="white", width=10)
set3.set("None")
set3.grid(row=1, column=2, padx=10)
setArea.grid(columnspan=2, pady=20)

#Character Area
charaArea = Canvas(root, bg='black', highlightthickness=0) #This left a white bar around the canvas, highlightthickness gets rid of it
charaArea.grid(row=1, column=1, padx=20)
#Name
charaName = MyOptionMenu(charaArea, "Character", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Luna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna", "Yuna")
charaName.config(font=("Arial bold", 20), bg="#000000", fg="white")
charaName.set("Yuna")
charaName.pack(side=TOP, fill=X)
charaName['menu'].config(font=("Arial", 20), bg="#000000", fg="#AAAAAA")
#Image
photo= PhotoImage(file="./Images/Yuna2.png")
charaImage = Label(charaArea, image=photo, bg='black', fg='black')
charaImage.pack()

##status.config(text="Building database")
##
##status.config(text="...")

#Stats
statArea = Frame(root, bg='black')
statArea.grid(row=1, column=2, padx=(0,20))
#Level
charaLevelFrame = Frame(statArea, bg='black')
charaLevelFrame.grid(row=0, stick=NW, pady=(0,100))
charaLevel_L = Label(charaLevelFrame, text="Lv. 50", font=("Arial bold", 15), bg='black', fg='orange')
charaLevel_L.grid(row=0, stick=W)
##charaLevel_E = MyOptionMenu(charaLevelFrame, "lv", "50", "60")
##charaLevel_E.config(bg='black', fg='orange', font=("Arial bold", 15), width=2)
##charaLevel_E.grid(row=0, column=1, stick=E)
#Star
starArea = Frame(statArea)
starArea['bg']='black'
star_L = Label(starArea, font=("Arial bold", 15), text='Star +', bg='black', fg='white')
star_L.grid(row=0, stick=W)
##star_E = MyOptionMenu(starArea, "starlv", "1", "2", "3", "4", "5", "6")
##star_E.config(font=("Arial bold", 15), bg="#000000", fg="white", width=2)
##star_E.grid(row=0, column=1, stick=E, padx=(20,0))
awake_L = Label(starArea, font=("Arial bold", 15), text='Awakening', bg='black', fg='white')
awake_L.grid(row=1, stick=W)
awake_E = MyOptionMenu(starArea, 'awake', "5", "6")
awake_E.config(font=("Arial bold", 15), bg="#000000", fg="white", width=2)
awake_E.grid(row=1, column=1, stick=E, padx=(20,0))
#Stats at the end (only a display)
stat_L = Label(statArea, text='Stats', font=('arial', 15), bg='black', fg='white')
stat_L.grid(columnspan=3)
starArea.grid(row=0, pady=50)

attack_L = Label(statArea, text='Attack', font=('arial', 10), bg='black', fg='#AAAAAA')
attack_L.grid(row=3, stick=W)
stats[0] = Label(statArea, text='696', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[0].grid(row=3, column=1, stick=E)

defense_L = Label(statArea, text='Defense', font=('arial', 10), bg='black', fg='#AAAAAA')
defense_L.grid(row=4, stick=W)
stats[1] = Label(statArea, text='696', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[1].grid(row=4, column=1, stick=E)

health_L = Label(statArea, text='Health', font=('arial', 10), bg='black', fg='#AAAAAA')
health_L.grid(row=5, stick=W)
stats[2] = Label(statArea, text='6969', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[2].grid(row=5, column=1, stick=E)

speed_L = Label(statArea, text='Speed', font=('arial', 10), bg='black', fg='#AAAAAA')
speed_L.grid(row=6, stick=W)
stats[3] = Label(statArea, text='69', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[3].grid(row=6, column=1, stick=E)

critC_L = Label(statArea, text='Critical Hit Chance', font=('arial', 10), bg='black', fg='#AAAAAA')
critC_L.grid(row=7, stick=W)
stats[4] = Label(statArea, text='69%', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[4].grid(row=7, column=1, stick=E)

critD_L = Label(statArea, text='Critical Hit Damage', font=('arial', 10), bg='black', fg='#AAAAAA')
critD_L.grid(row=8, stick=W, padx=(0, 10))
stats[5] = Label(statArea, text='69%', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[5].grid(row=8, column=1, stick=E)

effect_L = Label(statArea, text='Effectiveness', font=('arial', 10), bg='black', fg='#AAAAAA')
effect_L.grid(row=9, stick=W)
stats[6] = Label(statArea, text='69%', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[6].grid(row=9, column=1, stick=E)

resist_L = Label(statArea, text='Effect Resistance', font=('arial', 10), bg='black', fg='#AAAAAA')
resist_L.grid(row=10, stick=W)
stats[7] = Label(statArea, text='69%', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[7].grid(row=10, column=1, stick=E)

dual_L = Label(statArea, text='Dual Attack Chance', font=('arial', 10), bg='black', fg='#AAAAAA')
dual_L.grid(row=11, stick=W)
stats[8] = Label(statArea, text='69%', font=('arial', 10), bg='black', fg='#AAAAAA')
stats[8].grid(row=11, column=1, stick=E)

#Buttons
buttonFrame = Frame(statArea)
buttonFrame.grid(columnspan=2, pady=20)
buttonFrame["bg"] = "black"

button = Button(buttonFrame, text="Save", font=("Arial bold",11), width=9, bg="#40201E", fg="white", activebackground="#35281E", activeforeground="white", command=save)
button.grid(row=0, padx=5)

button = Button(buttonFrame, text="Submit", font=("Arial bold",11), width=9, bg="#40201E", fg="white", activebackground="#35281E", activeforeground="white", command=submit)
button.grid(row=0, column=2, padx=5)

#I need to store the percent increase of stats and the flat
calc = list()
for i in range(0,9):
    calc.append([])
    for j in range(0,3):
        calc[i].append(0)

#setup from the text file
if os.path.isfile('./Data/Yuna.txt'):
    #if file exists
    file = open("./Data/Yuna.txt", 'r')
    data = file.readlines()
    temp = data[0].split(',')
    hero.name = 'Yuna'
    charaName.set("Yuna")
    hero.level = str(temp[1])
    hero.star = str(temp[2])
    hero.awake = str(temp[3])
    charaLevel_L['text'] = 'Lv. ' + hero.level
    awake_E.set(hero.star)
    
    #update on window
    #left side
    for i in range(0,3):        
        temp = data[i+1].split(',')
        equips[i][1].delete(0,END)
        equips[i][1].insert(END, temp[0])
        for j in range(1,5):
            equips[i][j*2].set(str(temp[j*2-1]))
            equips[i][j*2+1].delete(0,END)
            equips[i][j*2+1].insert(END, temp[j*2])
    #right side
    for i in range(3,6):
        temp = data[i+1].split(',')
        
        for j in range(0,5):
            equips[i][j*2].set(temp[j*2])
            equips[i][j*2+1].delete(0,END)
            equips[i][j*2+1].insert(END, temp[j*2+1])

else:
    #if file doesn't exist
    save()
    file = open("./Data/Yuna.txt", 'r')
    data = file.readlines()
    hero.name = 'Yuna'
    hero.level = '50'
    hero.star = '5'
    hero.awake = '5'
    hero.attack = '742'
    hero.defense = '446'
    hero.health = '4074'
    hero.speed = '112'
    hero.critC = '15%'
    hero.critD = '150%'
    hero.effect = '0'
    hero.resist = '0'
    hero.dual = '5%'
file.close()

submit()


root.mainloop()

#I need to store the info somewhere, by default the page is on Yuna, in a text file?
#Should I build my database from the text file? something like this
#name, element, rarity, star, sign, weapon, helmet, chest, neck, ring, boot, artifact
