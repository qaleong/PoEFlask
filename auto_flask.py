import random
import time
import pyautogui
import pygetwindow
import threading

import tkinter as tk
from tkinter import ttk,messagebox

def flask_1(time1,time2,button):
    global running
    if time1 > time2:
        messagebox.showerror("Error", "Max time must be greater than min time.")
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
    min_time1 = float(min_time_entry1.get())
    max_time1 = float(max_time_entry1.get())
    min_time2 = float(min_time_entry2.get())
    max_time2 = float(max_time_entry2.get())
    min_time3 = float(min_time_entry3.get())
    max_time3 = float(max_time_entry3.get())
    min_time4 = float(min_time_entry4.get())
    max_time4 = float(max_time_entry4.get())

    t1 = threading.Thread(target=flask_1, args=(min_time1,max_time1,'1'))
    t2 = threading.Thread(target=flask_1, args=(min_time2,max_time2,'2'))
    t3 = threading.Thread(target=flask_1, args=(min_time3,max_time3,'3'))
    t4 = threading.Thread(target=flask_1, args=(min_time4,max_time4,'4'))
    t1.start()
    t2.start()
    t3.start()
    t4.start()

def stop_timer():
    global running
    running = False  # Set the flag to False to stop timers
    status_label.config(text="Timers Stopped.")  # Update the status label
        
# Create the GUI
root = tk.Tk()
root.title("Auto Flask")

# Create labels and input fields
min_time_label1 = tk.Label(root, text="Enter minimum time for flask 1(seconds):")
min_time_label1.pack()

min_time_entry1 = tk.Entry(root)
min_time_entry1.pack()

max_time_label1 = tk.Label(root, text="Enter maximum time for flask 1 (seconds):")
max_time_label1.pack()

max_time_entry1 = tk.Entry(root)
max_time_entry1.pack()

min_time_label2 = tk.Label(root, text="Enter minimum time for flask 2 (seconds):")
min_time_label2.pack()

min_time_entry2 = tk.Entry(root)
min_time_entry2.pack()

max_time_label2 = tk.Label(root, text="Enter maximum time for flask 2 (seconds):")
max_time_label2.pack()

max_time_entry2 = tk.Entry(root)
max_time_entry2.pack()

min_time_label3 = tk.Label(root, text="Enter minimum time for flask 3 (seconds):")
min_time_label3.pack()

min_time_entry3 = tk.Entry(root)
min_time_entry3.pack()

max_time_label3 = tk.Label(root, text="Enter maximum time for flask 3 (seconds):")
max_time_label3.pack()

max_time_entry3 = tk.Entry(root)
max_time_entry3.pack()

min_time_label4 = tk.Label(root, text="Enter minimum time for flask 4 (seconds):")
min_time_label4.pack()

min_time_entry4 = tk.Entry(root)
min_time_entry4.pack()

max_time_label4 = tk.Label(root, text="Enter maximum time for flask 4 (seconds):")
max_time_label4.pack()

max_time_entry4 = tk.Entry(root)
max_time_entry4.pack()

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
