import tkinter as tk
from tkinter import ttk, messagebox


# ===================== LRU Algorithm =====================
def lru_page_replacement(pages, capacity):
    frames = []
    recent = []
    result = []

    hits = 0
    faults = 0

    for page in pages:
        hit = False

        # Page already exists
        if page in frames:
            hits += 1
            hit = True

            recent.remove(page)
            recent.append(page)

        else:
            faults += 1

            if len(frames) < capacity:
                frames.append(page)
                recent.append(page)

            else:
                lru = recent.pop(0)
                index = frames.index(lru)

                frames[index] = page
                recent.append(page)

        result.append((page, frames.copy(), "Hit" if hit else "Fault"))

    return result, hits, faults


# ===================== Run Simulation =====================
def run_simulation():
    try:
        pages = list(map(int, entry_pages.get().split()))
        capacity = int(entry_frames.get())

        if capacity <= 0:
            messagebox.showerror("Error", "Số frame phải > 0")
            return

        # Clear old data
        for item in tree.get_children():
            tree.delete(item)

        result, hits, faults = lru_page_replacement(pages, capacity)

        for step, (page, frames, status) in enumerate(result, start=1):
            frame_text = " | ".join(map(str, frames))
            tree.insert("", "end",
                        values=(step, page, frame_text, status))

        lbl_result.config(
            text=f"Page Hits: {hits}     Page Faults: {faults}"
        )

    except:
        messagebox.showerror("Error", "Nhập dữ liệu không hợp lệ")


# ===================== GUI =====================
root = tk.Tk()
root.title("LRU Page Replacement Simulator")
root.geometry("750x500")
root.resizable(False, False)


# Title
title = tk.Label(root,
                 text="MÔ PHỎNG GIẢI THUẬT LRU",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)


# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame,
         text="Reference String:",
         font=("Arial", 11)).grid(row=0, column=0, padx=5)

entry_pages = tk.Entry(input_frame, width=40)
entry_pages.grid(row=0, column=1, padx=5)

tk.Label(input_frame,
         text="Number of Frames:",
         font=("Arial", 11)).grid(row=1, column=0, pady=10)

entry_frames = tk.Entry(input_frame, width=10)
entry_frames.grid(row=1, column=1, sticky="w")


# Button
btn = tk.Button(root,
                text="Run Simulation",
                font=("Arial", 11),
                bg="lightblue",
                command=run_simulation)

btn.pack(pady=10)


# Table
columns = ("Step", "Page", "Frames", "Status")

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150, anchor="center")

tree.pack(pady=10)


# Result
lbl_result = tk.Label(root,
                      text="",
                      font=("Arial", 7, "bold"),
                      fg="blue")

lbl_result.pack(pady=10)

root.mainloop()