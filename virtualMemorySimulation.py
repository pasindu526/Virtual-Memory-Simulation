import tkinter as tk
from tkinter import messagebox, scrolledtext

PAGE_SIZE = 1024
NUM_PAGES = 8
NUM_FRAMES = 4
MAX_LOGICAL_ADDRESS = (NUM_PAGES * PAGE_SIZE) - 1


def simulate_gui():
    page_table = [-1] * NUM_PAGES
    frames = [None] * NUM_FRAMES

    raw = entry.get()
    if not raw.strip():
        messagebox.showerror("Error", "Please enter logical addresses!")
        return

    try:
        logical_addresses = list(map(int, raw.split(",")))
    except:
        messagebox.showerror("Error", "Invalid input! Use comma-separated numbers.")
        return

    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "=== Virtual Memory Simulation (GUI Version) ===\n\n")

    for la in logical_addresses:
        output_box.insert(tk.END, f"Logical Address: {la}\n")

        if la < 0 or la > MAX_LOGICAL_ADDRESS:
            output_box.insert(tk.END, " Invalid address! Must be between 0–8191.\n\n")
            continue

        page_number = la // PAGE_SIZE
        offset = la % PAGE_SIZE

        output_box.insert(tk.END, f" Page Number: {page_number}\n")
        output_box.insert(tk.END, f" Offset: {offset}\n")

        frame_number = page_table[page_number]

        if frame_number != -1:
            physical_address = frame_number * PAGE_SIZE + offset
            output_box.insert(tk.END, f" Frame Number: {frame_number}\n")
            output_box.insert(tk.END, f" Physical Address: {physical_address}\n\n")

        else:
            output_box.insert(tk.END, " Page Fault Occurred!\n")

            free_frame = None
            for i in range(NUM_FRAMES):
                if frames[i] is None:
                    free_frame = i
                    break

            if free_frame is not None:
                frames[free_frame] = page_number
                page_table[page_number] = free_frame

                physical_address = free_frame * PAGE_SIZE + offset
                output_box.insert(tk.END, f" Page Loaded into Frame: {free_frame}\n")
                output_box.insert(tk.END, f" Physical Address: {physical_address}\n\n")

            else:
                output_box.insert(tk.END, " No free frames available - cannot load page.\n\n")

    output_box.insert(tk.END, f"Final Page Table: {page_table}\n")
    output_box.insert(tk.END, f"Frames: {frames}\n")


# GUI Window
root = tk.Tk()
root.title("522512868 - Virtual Memory Simulation")
root.geometry("850x580")

# MAIN TITLE (smaller)
main_title = tk.Label(root, text="Virtual Memory Simulation",
                      font=("Arial", 14, "bold"), fg="#2c3e50")
main_title.pack(pady=15)

# SUB TITLE (smaller)
sub_title = tk.Label(root, text="Page Size: 1024 Bytes | Logical Memory: 8 Pages | Physical Memory: 4 Frames",
                     font=("Arial", 10), fg="#34495e")
sub_title.pack()

# Input Section
label = tk.Label(root, text="Enter Logical Addresses (comma-separated):",
                 font=("Arial", 9))
label.pack(pady=8)

entry = tk.Entry(root, width=88, font=("Arial", 10))
entry.pack(ipady=4)

# Stylish Button (smaller)
def on_enter(e):
    btn.config(bg="#1abc9c")

def on_leave(e):
    btn.config(bg="#16a085")

btn = tk.Button(root, text="Simulate", command=simulate_gui,
                font=("Arial", 10, "bold"),
                bg="#16a085", fg="white",
                padx=12, pady=3, relief="raised", bd=2)
btn.pack(pady=15)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Output Box
output_box = scrolledtext.ScrolledText(root, width=85, height=22, font=("Courier New", 9))
output_box.pack(pady=10)

root.mainloop()
