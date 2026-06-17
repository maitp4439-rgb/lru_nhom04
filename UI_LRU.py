import tkinter as tk
from tkinter import messagebox

def lru_simulation(pages, capacity):
    frames = []
    page_faults = 0
    history = []

    for i, page in enumerate(pages):
        if page not in frames:
            if len(frames) < capacity:
                frames.append(page)
            else:
                # tìm trang ít dùng gần nhất
                lru_index = -1 
                lru_page = None
                for f in frames:
                    if f not in pages[:i]:
                        lru_page = f
                        break
                    else:
                        last_used = pages[:i][::-1].index(f)
                        if last_used > lru_index:
                            lru_index = last_used
                            lru_page = f

                frames[frames.index(lru_page)] = page
            page_faults += 1

        history.append(frames.copy())

    return history, page_faults


def run_lru():
    try:
        pages = list(map(int, entry_pages.get().split()))
        capacity = int(entry_capacity.get())

        history, faults = lru_simulation(pages, capacity)

        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, f"Thuật toán: LRU\n")
        result_box.insert(tk.END, f"Số frame: {capacity}\n\n")

        for i, state in enumerate(history):
            result_box.insert(tk.END, f"Bước {i+1}: {state}\n")

        result_box.insert(tk.END, f"\nPage Faults: {faults}")

    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng!")


# GUI
root = tk.Tk()
root.title("LRU Page Replacement Simulator")
root.geometry("600x500")

title = tk.Label(root, text="LRU PAGE REPLACEMENT SIMULATOR", font=("Arial", 16, "bold"))
title.pack(pady=10)

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Chuỗi trang: ").grid(row=0, column=0)
entry_pages = tk.Entry(frame_input, width=40)
entry_pages.grid(row=0, column=1)
entry_pages.insert(0, "7 0 1 2 0 3 0 4")

tk.Label(frame_input, text="Số frame: ").grid(row=1, column=0)
entry_capacity = tk.Entry(frame_input, width=10)
entry_capacity.grid(row=1, column=1)
entry_capacity.insert(0, "3")

btn_run = tk.Button(root, text="Run LRU", command=run_lru, bg="lightblue")
btn_run.pack(pady=10)

result_box = tk.Text(root, height=20, width=70)
result_box.pack(pady=10)

root.mainloop()