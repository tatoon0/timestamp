from tkinter import *
from tkinter import ttk
from datetime import datetime

# Timestamp list
timestamp = []

def add_timestamp():
    # Get input and parse it
    time_input = input_field.get()
    minutes, seconds = map(int, time_input.split(":"))
    total_seconds = minutes * 60 + seconds
    
    # Add timestamp to the list
    timestamp.append(total_seconds)
    
    # Update the listbox display
    listbox.insert(END, f"{minutes}m {seconds}s")
    input_field.delete(0, END)

# Event handler for Enter key
def on_enter_key(event):
    add_timestamp()

def remove_selected():
    # Get the selected index
    selected_index = listbox.curselection()[0]
    
    # Remove from both the list and the Listbox
    listbox.delete(selected_index)
    timestamp.pop(selected_index)

def calculate_difference():
    # Get inputs and parse them
    time1 = time1_field.get()
    time2 = time2_field.get()
    
    minutes1, seconds1 = map(int, time1.split(":"))
    minutes2, seconds2 = map(int, time2.split(":"))
    
    total_seconds1 = minutes1 * 60 + seconds1
    total_seconds2 = minutes2 * 60 + seconds2
    
    # Calculate difference
    difference = abs(total_seconds1 - total_seconds2)
    
    # Adjust all timestamps
    for i in range(len(timestamp)):
        timestamp[i] = max(0, timestamp[i] - difference)  # Ensure no negative times
    
    # Update Listbox
    listbox.delete(0, END)
    for t in timestamp:
        minutes, seconds = divmod(t, 60)
        listbox.insert(END, f"{minutes}m {seconds}s")

# Create the main Tkinter window
root = Tk()
root.title("Timestamp Manager")

# Set window size
root.geometry("400x400")  # Set width to 400 pixels and height to 400 pixels

### TOP ###

# Top frame to hold input components
top_frame = Frame(root)
top_frame.pack(side=TOP, fill=X, pady=10)

# Sub-frame to center align components
center_frame = Frame(top_frame)
center_frame.pack(side=TOP, pady=5)  # Align center_frame to top with padding

# Input field for minutes and seconds
input_label = ttk.Label(center_frame, text="Enter time (MM:SS):")
input_label.pack(side=LEFT, padx=5)

input_field = Entry(center_frame, width=20)
input_field.pack(side=LEFT)
input_field.bind("<Return>", on_enter_key)  # Bind Enter key to the input field

# Button to add the timestamp
add_button = ttk.Button(center_frame, text="Add Timestamp", command=add_timestamp)
add_button.pack(side=LEFT, padx=5)

### LEFT ###

# Left frame to hold time difference components
left_frame = Frame(root)
left_frame.pack(side=LEFT, fill=Y, padx=(20,0), pady=10)

# Fields to calculate the difference between two times
time1_label = ttk.Label(left_frame, text="Enter first time (MM:SS):")
time1_label.pack(anchor="w", pady=2)

time1_field = Entry(left_frame, width=20)
time1_field.pack(anchor="w")

time2_label = ttk.Label(left_frame, text="Enter second time (MM:SS):")
time2_label.pack(anchor="w", pady=2)

time2_field = Entry(left_frame, width=20)
time2_field.pack(anchor="w")

# Button to calculate the time difference
calculate_button = ttk.Button(left_frame, text="Calculate Difference", command=calculate_difference)
calculate_button.pack(anchor="e", pady=5, padx=5)

### RIGHT ###

# Right frame for listbox and related buttons
right_frame = Frame(root)
right_frame.pack(side=RIGHT, fill=Y, padx=20, pady=10)

# Listbox to display the timestamps
listbox_label = ttk.Label(right_frame, text="Timestamps:")
listbox_label.pack(anchor="w", pady=5)

listbox = Listbox(right_frame, width=30, height=15)
listbox.pack(anchor="w", pady=5)

# Button to remove the selected timestamp
remove_button = ttk.Button(right_frame, text="Remove Selected", command=remove_selected)
remove_button.pack(anchor="e", pady=5)

# Run the Tkinter event loop
root.mainloop()
