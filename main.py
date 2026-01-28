'''
    Written By : Meyan Adhikari (080BEL042)
'''
# --------------------------
import tkinter as tk
import json


# --------------------------
FILE_1 = "data/com_liq_sup_steam.json"  # COMPRESSED LIQUID and SUPERHEATED STEAM
FILE_2 = "data/sat_pres.json" # SATURATED WATER BY PRESSURE
FILE_3 = "data/sat_temp.json" # SATURATED WATER BY TEMPERATURE



# -------------------------
class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Thermo Water Properties")
        self.geometry("800x500")
        self.style_window()

    def style_window(self) -> None:
        # These are styling codes for all the style you see on the GUI

        tk.Label(text="STEAM/WATER VALUES",
                fg = "darkblue",
                 font= ("Arial", 16)).pack()

        # Super Heated Steam    
        lf1 = tk.LabelFrame(text="SuperHeated Steam")
        lf1.pack()

        tk.Label(lf1, text= "Enter Pressure").pack()
        sup_pre= tk.Entry(lf1)
        sup_pre.pack(pady=10)

        tk.Label(lf1, text= "Enter Temperature").pack()
        super_temp= tk.Entry(lf1)
        super_temp.pack()

        tk.Button(lf1, text="Find").pack(pady=10)



# ----------------------
def main() -> None:
    com_sup, sat_pres, sat_temp = load_json()

    win = Window()
    win.mainloop()

def load_json() -> tuple[dict]:
    ''' Loads the files as python dictionary and returns them '''

    with open(FILE_1, 'r', encoding ='utf-8-sig') as file:
        com_sup =  json.load(file)
    with open(FILE_2, 'r', encoding ='utf-8-sig') as file:
        sat_pres = json.load(file)
    with open(FILE_3, "r", encoding ='utf-8-sig') as file:
        sat_temp = json.load(file)

    return com_sup, sat_pres, sat_temp

if __name__ == "__main__":
    main()







