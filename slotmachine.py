import random
#from tkinter import *
#from tkinter import ttk
#from tkinter import messagebox
import keyboard

#main 
def main(): 

    #symbols = ["%", "§", "&", "7", "v"]
    #weights = [40, 30, 20, 9, 1]

    geld = 0;
    #int(geldeinzahlen);

    #fenster();

    print("SLOTMACHINE")

    #print("Wollen Sie frei gamblen (1) oder einzahlen (0)?")
    entscheidung = int(input("Wollen Sie frei gamblen (0) oder einzahlen (1)? "))

    if entscheidung == 1:
        geld= einzahlen(geld);
    
    else:
        geld= freiGamblen(geld);
    
    print("Startgeld: ", geld)

    #keyboard.add_hotkey('space', zufällig)
    #print("Drücke SPACE zum Drehen...")
    #keyboard.wait("esc")
    print("\nDrücke ENTER zum Drehen oder 'q' zum Beenden.")

    while True:
        command = input("> ")
        if command.lower() == 'q':
            print("Spiel beendet.")
            break
        zufällig()


    
def einzahlen(geld):
    #print("Wie viel Geld wollen Sie einzahlen?")
    geldeinzahlen = int(input("Wie viel Geld wollen Sie einzahlen? "))
    return geld + geldeinzahlen;

def freiGamblen(geld):
    return geld + 150000;

def zufällig():
    symbole = ["🍒", "🍋","🔔","7","💎"]
    gewichte = [0.5, 0.3, 0.15,0.04,0.01]

    ergebnis = random.choices(symbole, weights=gewichte, k=3)
    print (ergebnis)

#def fenster():
#    root = Tk();
#    root.attributes("-fullscreen", True)
#
#    menu_offen = False
#
#    overlay = Frame(root, bg="black") #container "menü"
#
#    menu = Frame(overlay, bg="#222", padx=30, pady=20); #menü
#    menu.place(relx=0.5, rely=0.5, anchor="center");#wo das menü positioniert ist
#    
#    rausgehen = Button(root, text="BEENDEN", command=root.destroy); #erstellt ein button und wird root (das fenster) wird "kaputt gemacht"
#    rausgehen.pack(); #zeigt button an
#
#    def esc(event=None):
#        nonlocal menu_offen
#
#        if menu_offen:
#            overlay.place_forget()
#            menu_offen = False
#        else:
#            overlay.place(relwidth=1, relheight=1)
#            menu_offen = True
#
#    root.bind("<Escape>", esc)
#    
#    root.mainloop();

#main ausgabe
main()