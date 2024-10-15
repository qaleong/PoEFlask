import random
import time
import pyautogui
import pygetwindow
import threading

import tkinter as tk
from tkinter import messagebox

def flask_1(time1,time2,button):
    global running
    if time1 > time2:
        messagebox.showerror("Error", "Max time must be greater than min time.")
        stop_timer()
        return
    elif  time2 == 0:
        messagebox.showerror("Error", "Cannot have a duration of zero")
        stop_timer()
        return
    elif time1 < 0 or time2 <0:
        messagebox.showerror("Error", "Max time cannot be less than zero.")
        stop_timer()
        return
    else:
        while running:
            timesec = random.uniform(time1,time2)
            time.sleep(timesec)  
            windowtitle = str(pygetwindow.getActiveWindow())
            #print(windowtitle)
            if windowtitle.endswith('Exile">'):
                pyautogui.press(button)

def start_timer():
    global running
    running = True  # Set the flag to True to start timers
    status_label.config(text="timer running")
    time_ranges = [
        (float(min_time_entry1.get()), float(max_time_entry1.get()), '1', flask1_var.get()),
        (float(min_time_entry2.get()), float(max_time_entry2.get()), '2', flask2_var.get()),
        (float(min_time_entry3.get()), float(max_time_entry3.get()), '3', flask3_var.get()),
        (float(min_time_entry4.get()), float(max_time_entry4.get()), '4', flask4_var.get())
    ]

    for min_time, max_time, button, enabled in time_ranges:
        if enabled:
            threading.Thread(target=flask_1, args=(min_time, max_time, button)).start()


def stop_timer():
    global running
    running = False  # Set the flag to False to stop timers
    status_label.config(text="Timers Stopped.")  # Update the status label

def create_timer_row(flask_num, min_time_var, max_time_var, check_var):
    """Helper function to create a row in the GUI for a flask timer"""
    min_time_label = tk.Label(frame, text=f"Flask {flask_num} Min Time (seconds):")
    min_time_label.grid(row=flask_num, column=0, sticky="w", pady=2)

    min_time_entry = tk.Entry(frame, textvariable=min_time_var, validate="key", validatecommand=Numeric_check)
    min_time_entry.grid(row=flask_num, column=1, pady=2)

    max_time_label = tk.Label(frame, text=f"Flask {flask_num} Max Time (seconds):")
    max_time_label.grid(row=flask_num, column=2, sticky="w", pady=2)

    max_time_entry = tk.Entry(frame, textvariable=max_time_var, validate="key", validatecommand=Numeric_check)
    max_time_entry.grid(row=flask_num, column=3, pady=2)

    flask_checkbox = tk.Checkbutton(frame, text="Enable", variable=check_var)
    flask_checkbox.grid(row=flask_num, column=4, pady=2)

    return min_time_entry, max_time_entry    

def validate_numeric_input(P):
    """Validation function to allow only numeric input (including decimal points)."""
    if P == "":  # Allow backspace (empty string)
        return True
    try:
        float(P)  # Try to convert to float
        return True
    except ValueError:
        return False
# Create the GUI
root = tk.Tk()
root.title("Auto Flask")

Numeric_check = (root.register(validate_numeric_input), "%P")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

flask1_var = tk.IntVar(value=1)
flask2_var = tk.IntVar(value=1)
flask3_var = tk.IntVar(value=1)
flask4_var = tk.IntVar(value=1)
# Create input rows for each flask timer, initializing the values to "0"
min_time_entry1, max_time_entry1 = create_timer_row(1, tk.StringVar(value='0'), tk.StringVar(value='0'), flask1_var)
min_time_entry2, max_time_entry2 = create_timer_row(2, tk.StringVar(value='0'), tk.StringVar(value='0'), flask2_var)
min_time_entry3, max_time_entry3 = create_timer_row(3, tk.StringVar(value='0'), tk.StringVar(value='0'), flask3_var)
min_time_entry4, max_time_entry4 = create_timer_row(4, tk.StringVar(value='0'), tk.StringVar(value='0'), flask4_var)



# Button to start the timer
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack()

# Label to show the result
status_label = tk.Label(root, text="")
status_label.pack()

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack()

# Start the GUI main loop
root.mainloop()
