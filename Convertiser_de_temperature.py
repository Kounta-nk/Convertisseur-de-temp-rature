import tkinter as tk

def fahrenheit_to_celsius():
    """Convertit Fahrenheit en Celsius et affiche le résultat"""
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius = round(celsius, 2)
        lbl_result.config(text=f"{celsius} \N{DEGREE CELSIUS}")
    except ValueError:
        lbl_result.config(text="Entrez un nombre")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Convertisseur de température")
window.resizable(width=False, height=False)

# Création du cadre pour l'entrée
frm_entry = tk.Frame(master=window)

# Widget d'entrée pour Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=20)

# Étiquette pour le symbole Fahrenheit
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Organisation des widgets dans le cadre
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Bouton de conversion
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)

# Étiquette pour afficher le résultat en Celsius
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Organisation des widgets principaux
frm_entry.grid(row=0, column=0, padx=15)
btn_convert.grid(row=0, column=1, pady=20)
lbl_result.grid(row=0, column=2, padx=40)

# Lancement de l'application
window.mainloop()