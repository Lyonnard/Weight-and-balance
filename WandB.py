import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        masses = [float(mass_var.get()) for mass_var in mass_vars]
        arms = [float(arm_var.get()) for arm_var in arm_vars]
        total_mass = sum(masses)
        moment = sum(mass * arm for mass, arm in zip(masses, arms))
        cg_position = moment / total_mass
        
        max_cg = float(max_cg_var.get())
        min_cg = float(min_cg_var.get())
        max_weight = float(max_weight_var.get())
        
        cg_percent = ((cg_position - min_cg) / (max_cg - min_cg)) * 100
        weight_percent = (total_mass / max_weight) * 100
        
        cg_bar['value'] = cg_percent
        weight_bar['value'] = weight_percent
        
        cg_label.config(text=f"CG Position: {cg_position:.2f} mm")
        weight_label.config(text=f"Total Weight: {total_mass:.2f} kg")
        
    except ValueError:
        pass  # Handle invalid input if necessary

root = tk.Tk()
root.title("Glider Plane Weight and Balance")

elements = [
    "Empty Plane", "Pilot", "Passenger", 
    "Wing Water", "Tail Water", "Nose Weights", "Miscellaneous"
]

mass_vars = []
arm_vars = []

for i, element in enumerate(elements):
    tk.Label(root, text=element).grid(row=i, column=0, padx=5, pady=5)
    
    mass_var = tk.StringVar()
    arm_var = tk.StringVar()
    
    tk.Entry(root, textvariable=mass_var).grid(row=i, column=1, padx=5, pady=5)
    tk.Entry(root, textvariable=arm_var).grid(row=i, column=2, padx=5, pady=5)
    
    mass_vars.append(mass_var)
    arm_vars.append(arm_var)

tk.Label(root, text="Max CG (mm)").grid(row=len(elements), column=0, padx=5, pady=5)
max_cg_var = tk.StringVar()
tk.Entry(root, textvariable=max_cg_var).grid(row=len(elements), column=1, padx=5, pady=5)

tk.Label(root, text="Min CG (mm)").grid(row=len(elements)+1, column=0, padx=5, pady=5)
min_cg_var = tk.StringVar()
tk.Entry(root, textvariable=min_cg_var).grid(row=len(elements)+1, column=1, padx=5, pady=5)

tk.Label(root, text="Max Weight (kg)").grid(row=len(elements)+2, column=0, padx=5, pady=5)
max_weight_var = tk.StringVar()
tk.Entry(root, textvariable=max_weight_var).grid(row=len(elements)+2, column=1, padx=5, pady=5)

tk.Button(root, text="Calculate", command=calculate).grid(row=len(elements)+3, column=0, columnspan=2, pady=10)

cg_label = tk.Label(root, text="CG Position: ")
cg_label.grid(row=len(elements)+4, column=0, columnspan=2)

weight_label = tk.Label(root, text="Total Weight: ")
weight_label.grid(row=len(elements)+5, column=0, columnspan=2)

cg_bar = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
cg_bar.grid(row=len(elements)+6, column=0, columnspan=2, pady=5)

weight_bar = ttk.Progressbar(root, orient='vertical', length=200, mode='determinate')
weight_bar.grid(row=len(elements)+7, column=0, columnspan=2, pady=5)

root.mainloop()
