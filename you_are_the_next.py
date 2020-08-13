from tkinter import *
import numpy as np
import json


# Callback function of start button
# Used to start and stop random selection
def start_button_callback():
    global start
    start = ~start
    if start:
        btn_start.configure(text="Stop", bg="#fc6b51")
        window.after(10, update_label)
    else:
        btn_start.configure(text="Start", bg="#60f000")
        btn_update.config(state="normal")


# Callback function of update button
# Used to update database file
def update_button_callback():
    # Update database
    data["unsafe"].remove(name)
    data["safe"].append(name)

    # Next round
    if len(data["unsafe"]) == 0:
        data["unsafe"] = data["safe"]
        data["safe"] = []

    # Save updated database to json file
    with open("database.json", "w") as f:
        json.dump(data, f, indent=4)
    lbl.configure(text="Database updated!")
    btn_update.config(state="disabled")

# Update the label text to a new name every 10ms
def update_label():
    global name
    # Random pick an index
    index = np.random.randint(0, len(data["unsafe"]))
    name = data["unsafe"][index]
    # Update label
    lbl.configure(text=name)
    # Start next iteration in 10 ms until stop button clicked
    if start:
        window.after(10, update_label)


# Global variable
start = False
name = ""

# Read Library
with open("database.json") as f:
    data = json.load(f)

# Create GUI object
window = Tk()
window.title("Lucky Draw")
window.geometry("400x250")
window.configure(bg="#fffbe0")

# Create Label
lbl = Label(window, text="Click Start to begin", font=("Arial Bold", 30), bg="#fffbe0")
lbl.pack(side=TOP, pady=15)

# Create Start Button
btn_start = Button(window, text="Start", font=("Arial Bold", 12),bg="#60f000", fg="black",
                     height=2, width=15, command=start_button_callback)
btn_start.pack(side=TOP, pady=10)

# Create Update Database Button
btn_update = Button(window, text="Update database", font=("Arial Bold", 12),bg="#009be8", fg="black",
                     height=2, width=15, state="disabled", command=update_button_callback)
btn_update.pack(side=TOP, pady=15)
window.mainloop()
