import random
from tkinter import *
from tkinter import ttk

#main 
def main(): 

    symbols = ["%", "§", "&", "7", "v"]
    weights = [40, 30, 20, 9, 1]

    geld = int(0);
    #int(geldeinzahlen);

    fenster();

    print("SLOTMACHINE")

    #print("Wollen Sie frei gamblen (1) oder einzahlen (0)?")
    entscheidung = bool(input("Wollen Sie frei gamblen (1) oder einzahlen (0)? "))

    if entscheidung:
        einzahlen(geld);
    
    else:
        freiGamblen(geld);

    
def einzahlen(geld):
    #print("Wie viel Geld wollen Sie einzahlen?")
    geldeinzahlen = int(input("Wie viel Geld wollen Sie einzahlen? "))
    geld = geld + geldeinzahlen;

def freiGamblen():
    geld = geld + 150000;

def fenster():
    root = Tk();
    root.mainloop();


#main ausgabe
main();
