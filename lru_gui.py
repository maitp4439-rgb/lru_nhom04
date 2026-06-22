import tkinter as tk
from tkinter import messagebox

def run_lru():
    text_out.delete(1.0, tk.END) 
    try:
        raw_input = ent_ref.get().replace(',', ' ').split()
        pages = [int(x.strip()) for x in raw_input if x.strip()]
        frames = int(ent_frames.get())
        if frames <= 0 or not pages: raise ValueError
    except:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return

    # --- LRU ALGORITHM LOGIC & OUTPUT FORMATTING ---
    memory = [] 
    faults = 0

    text_out.insert(tk.END, "=" * 70 + "\n")
    text_out.insert(tk.END, "DETAILED PROCESSING\n")
    text_out.insert(tk.END, f"Frames: {frames} | String: {pages}\n")
    text_out.insert(tk.END, "=" * 70 + "\n")

    for p in pages:
        action = ""
        if p in memory:
            action = "Page Fault: NO  (HIT)"
            memory.remove(p)
            memory.append(p)
        else:
            faults += 1
            if len(memory) == frames: 
                replaced_page = memory.pop(0) 
                action = f"Page Fault: YES (MISS - Replaced page {replaced_page})"
            else:
                action = "Page Fault: YES (MISS - Added to free frame)"
            memory.append(p) 

        text_out.insert(tk.END, f"Reference {p}: \u27A1\t{action}\n")
        text_out.insert(tk.END, f"    Memory state: {memory}\n")
        

    fault_rate = (faults / len(pages)) * 100
    text_out.insert(tk.END, "\n" + "=" * 70 + "\n")
    text_out.insert(tk.END, "SUMMARY RESULT\n")
    text_out.insert(tk.END, f"Total Page Faults: {faults}\n")
    text_out.insert(tk.END, f"Page Fault Rate  : {fault_rate:.2f}%\n")
    text_out.insert(tk.END, "=" * 70 + "\n")


def load_example():
    clear_all()
# Example LRU
    ent_ref.insert(0, "7, 0, 1, 2, 0, 3, 0, 4, 2, 3")
    ent_frames.insert(0, "3")


def clear_all():
    ent_ref.delete(0, tk.END)
    ent_frames.delete(0, tk.END)
    text_out.delete(1.0, tk.END)


# -- GUI SETUP -- 
root = tk.Tk()
root.title("LRU ALGORITHM")
root.geometry("680x650") 
root.config(padx=20, pady=20, bg="#f0f0f0")

# Title
tk.Label(root, text="LRU PAGE REPLACEMENT ALGORITHM", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=(0, 20))

# 1. Input Container
f_in = tk.Frame(root, bg="#f0f0f0")
f_in.pack()

tk.Label(f_in, text="Page string (comma-separated):", font=("Arial", 11), bg="#f0f0f0").grid(row=0, column=0, sticky="e", pady=5, padx=5)
ent_ref = tk.Entry(f_in, width=40, font=("Arial", 11))
ent_ref.grid(row=0, column=1, pady=5, ipady=2)

tk.Label(f_in, text="Frames (capacities):", font=("Arial", 11), bg="#f0f0f0").grid(row=1, column=0, sticky="e", pady=5, padx=5)
ent_frames = tk.Entry(f_in, width=15, font=("Arial", 11))
ent_frames.grid(row=1, column=1, sticky="w", pady=5, ipady=2)

# 2. Buttons Container
f_btn = tk.Frame(root, bg="#f0f0f0")
f_btn.pack(pady=15)

tk.Button(f_btn, text="Run", command=run_lru, width=12).grid(row=0, column=0, padx=10)
tk.Button(f_btn, text="Example", command=load_example, width=12).grid(row=0, column=1, padx=10)
tk.Button(f_btn, text="Clear", command=clear_all, width=12).grid(row=0, column=2, padx=10)

# 3. Result Container
f_out = tk.LabelFrame(root, text="Result", font=("Arial", 11, "bold"), bg="#f0f0f0", padx=10, pady=10)
f_out.pack(fill="both", expand=True, pady=10)

# Main output text box
text_out = tk.Text(f_out, height=20, width=70, font=("Courier", 11), relief="solid", borderwidth=1)
text_out.pack(fill="both", expand=True)

# Run the application
root.mainloop()