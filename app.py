import tkinter as tk

# This pulls the functions from the other two files in your folder
from receiver import run_receiver
from sender import run_sender

# Variable to track which mode the user clicks
selected_mode = None

def choose_receiver():
    global selected_mode
    selected_mode = "receiver"
    menu.destroy() # Closes the menu window

def choose_sender():
    global selected_mode
    selected_mode = "sender"
    menu.destroy() # Closes the menu window

# Build the Main Menu Window
menu = tk.Tk()
menu.title("Session Tracker Setup")
menu.geometry("300x150")

tk.Label(menu, text="Choose Mode for this Computer:", font=("Arial", 12)).pack(pady=10)
tk.Button(menu, text="Run as RECEIVER", bg="lightblue", font=("Arial", 12), command=choose_receiver).pack(pady=5)
tk.Button(menu, text="Run as SENDER", bg="lightgreen", font=("Arial", 12), command=choose_sender).pack(pady=5)

# Keep the menu open until a button is clicked
menu.mainloop()

# After the menu closes, trigger the correct file
if selected_mode == "receiver":
    run_receiver()
elif selected_mode == "sender":
    run_sender()