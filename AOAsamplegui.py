# Grant Thornton
# Sample GUI for Testing


import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("AOA Inputs")

# Create a label widget for each value
SMA_label = tk.Label(root, text="SMA:")
SMA_label.grid(row=0, column=0)
ECC_label = tk.Label(root, text="ECC:")
ECC_label.grid(row=1, column=0)
INC_label = tk.Label(root, text="INC:")
INC_label.grid(row=2, column=0)
RAAN_label = tk.Label(root, text="RAAN:")
RAAN_label.grid(row=3, column=0)
AOP_label = tk.Label(root, text="AOP:")
AOP_label.grid(row=4, column=0)
TA_label = tk.Label(root, text="TA:")
TA_label.grid(row=5, column=0)
srp_area_label = tk.Label(root, text="SRP Area:")
srp_area_label.grid(row=6, column=0)
cr_label = tk.Label(root, text="Cr:")
cr_label.grid(row=7, column=0)
drymass_label = tk.Label(root, text="Dry Mass:")
drymass_label.grid(row=8, column=0)

# Create entry widgets for each value
SMA_entry = tk.Entry(root)
SMA_entry.grid(row=0, column=1)
ECC_entry = tk.Entry(root)
ECC_entry.grid(row=1, column=1)
INC_entry = tk.Entry(root)
INC_entry.grid(row=2, column=1)
RAAN_entry = tk.Entry(root)
RAAN_entry.grid(row=3, column=1)
AOP_entry = tk.Entry(root)
AOP_entry.grid(row=4, column=1)
TA_entry = tk.Entry(root)
TA_entry.grid(row=5, column=1)
srp_area_entry = tk.Entry(root)
srp_area_entry.grid(row=6, column=1)
cr_entry = tk.Entry(root)
cr_entry.grid(row=7, column=1)
drymass_entry = tk.Entry(root)
drymass_entry.grid(row=8, column=1)

# Create a function to write the inputted values to a text file
def write_to_file():
    # Open a text file for writing (create it if it doesn't exist)
    with open("inputs.txt", "w") as file:
        # Write the inputted values to the file
        file.write(f"SMA: {SMA_entry.get()}\n")
        file.write(f"ECC: {ECC_entry.get()}\n")
        file.write(f"INC: {INC_entry.get()}\n")
        file.write(f"RAAN: {RAAN_entry.get()}\n")
        file.write(f"AOP: {AOP_entry.get()}\n")
        file.write(f"TA: {TA_entry.get()}\n")
        file.write(f"SRP Area: {srp_area_entry.get()}\n")
        file.write(f"Cr: {cr_entry.get()}\n")
        file.write(f"Dry Mass: {drymass_entry.get()}\n")

# Create a button widget to submit the values
submit_button = tk.Button(root, text="Submit", command=write_to_file)
submit_button.grid(row=9, column=1)

# Run the main event loop
root.mainloop()