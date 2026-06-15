import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("LRU Page Replacement")
root.geometry("900x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="LRU PAGE REPLACEMENT",
    font=("Arial", 18, "bold")
)
title.pack(pady=15)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(
    frame_input,
    text="Page Reference:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=5)

entry_pages = tk.Entry(
    frame_input,
    width=30,
    font=("Arial", 12)
)
entry_pages.grid(row=0, column=1, padx=5)

frame_number = tk.Frame(root)
frame_number.pack(pady=10)

tk.Label(
    frame_number,
    text="Number of Frames:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=5)

entry_frames = tk.Entry(
    frame_number,
    width=10,
    font=("Arial", 12)
)
entry_frames.grid(row=0, column=1, padx=5)

frame_button = tk.Frame(root)
frame_button.pack(pady=15)

btn_run = tk.Button(
    frame_button,
    text="Run LRU",
    width=12,
    height=2,
    font=("Arial", 11)
)
btn_run.grid(row=0, column=0, padx=10)

btn_clear = tk.Button(
    frame_button,
    text="Clear",
    width=12,
    height=2,
    font=("Arial", 11)
)

btn_clear.grid(row=0, column=1, padx=10)
#Them frame
memory_frame = tk.LabelFrame(
    root,
    text="Memory Frames",
    font=("Arial", 12, "bold")
)
memory_frame.pack(pady=10)

frame1 = tk.Label(memory_frame, text="Frame 1",
                  width=12, height=3,
                  relief="solid",
                  font=("Arial", 12))
frame1.grid(row=0, column=0, padx=10)

frame2 = tk.Label(memory_frame, text="Frame 2",
                  width=12, height=3,
                  relief="solid",
                  font=("Arial", 12))
frame2.grid(row=0, column=1, padx=10)

frame3 = tk.Label(memory_frame, text="Frame 3",
                  width=12, height=3,
                  relief="solid",
                  font=("Arial", 12))

frame3.grid(row=0, column=2, padx=10)
#Them bang lich su
history_frame = tk.LabelFrame(
    root,
    text="Simulation History",
    font=("Arial", 12, "bold")
)
history_frame.pack(pady=10)

columns = (
    "Page",
    "Frame1",
    "Frame2",
    "Frame3",
    "Status"
)

tree = ttk.Treeview(
    history_frame,
    columns=columns,
    show="headings",
    height=8
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

tree.pack()

frame_stats = tk.Frame(root)
frame_stats.pack(pady=10)

tk.Label(frame_stats, text="Page Faults:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
label_faults = tk.Label(frame_stats, text="0", font=("Arial", 12, "bold"))
label_faults.grid(row=0, column=1, padx=10)

tk.Label(frame_stats, text="Page Hits:", font=("Arial", 12)).grid(row=0, column=2, padx=10)
label_hits = tk.Label(frame_stats, text="0", font=("Arial", 12, "bold"))
label_hits.grid(row=0, column=3, padx=10)

#demo test(có thể xóa)
tree.insert("", "end", values=("7", "7", "", "", "Fault"))
tree.insert("", "end", values=("0", "7", "0", "", "Fault"))
tree.insert("", "end", values=("1", "7", "0", "1", "Fault"))

label_faults.config(text="3")
label_hits.config(text="0")

#run
root.mainloop()