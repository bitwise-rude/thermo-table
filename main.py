'''
    Written By : Meyan Adhikari (080BEL042)
'''
# --------------------------
import tkinter as tk
import json
from dataclasses import dataclass

# --------------------------
FILE_1 = "data/com_liq_sup_steam.json"  # COMPRESSED LIQUID and SUPERHEATED STEAM
FILE_2 = "data/sat_pres.json" # SATURATED WATER BY PRESSURE
FILE_3 = "data/sat_temp.json" # SATURATED WATER BY TEMPERATURE

# These are global values containing table data, will be updated later
com_sup = sat_pres = sat_temp = None


# -------------------------
@dataclass
class SuperResult:
    p : float
    t : float
    v : float
    e : float
    ph : str

    ''' Stores the result from Super heated condition
        p -> Pressure
        t -> Temperature
        v -> Specific Volume
        e -> Enthalpy
        ph -> Phase
    '''

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
        def btn_fn_superheated() -> None:
            vals = (sup_pre.get(), super_temp.get(), super_vol.get())

            found = None
            results: list[SuperResult] = []

            for  i, val in enumerate(vals):
                try:
                    val_f  = float(val)

                    if  i ==  0:  results = get_superheated_from_pressure(val_f)
                    break

                except ValueError:
                    continue
            print(results)

        lf1 = tk.LabelFrame(text="SuperHeated Steam")
        lf1.pack()

        tk.Label(lf1, text= "Enter Pressure (MPa)").pack()
        sup_pre= tk.Entry(lf1)
        sup_pre.pack(pady=10)

        tk.Label(lf1, text= "Enter Temperature (°C)").pack()
        super_temp= tk.Entry(lf1)
        super_temp.pack()

        tk.Label(lf1, text= "Enter Specific Volume (m^3/kg)").pack()
        super_vol= tk.Entry(lf1)
        super_vol.pack()


        tk.Button(lf1, text="Find",command=btn_fn_superheated).pack(pady=10)



# ----------------------
def main() -> None:
    global com_sup, sat_pres, sat_temp

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

def get_superheated_from_pressure(val:float) -> list[SuperResult]:
    ''' From the chart, gets the value of superheated from pressure'''
    results: list[SuperResult] = []

    for p_data in com_sup['data']:
        if p_data[0] == val:
            results.append(SuperResult(
                p_data[0],
                p_data[1],
                p_data[2],
                p_data[-3],
                p_data[-1]
            ))

    return results

if __name__ == "__main__":
    main()







