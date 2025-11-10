#scan_ui.py

import tkinter as tk
class View:
    #Initialize GUI components
    def __init__(self, title="Cash Register"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("400x300")
        
        #label prompting user
        self.label = tk.Label(self.root, text="Scan Product UPC:")
        self.label.pack(pady=5)
       
       #Entry box for manual UPC entry
        self.upc_entry = tk.Entry(self.root)
        self.upc_entry.pack(pady=5)
         
        #Scan button (controller wires this to logic)
        self.scan_button = tk.Button(self.root, text="Scan")
        self.scan_button.pack(pady=5)
        
        #Frame for scrollable result display
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(fill=tk.BOTH, expand=False, pady=10)
        
        #Scrollbar for result display
        self.scrollbar = tk.Scrollbar(self.result_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        #Text widget to show scanned products
        self.result_text = tk.Text(self.result_frame, height=8, yscrollcommand=self.scrollbar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.result_text.yview)
        
        #Subtotal label to show running total
        self.subtotal_label = tk.Label(self.root, text="Subtotal: $0.00", fg="green")
        self.subtotal_label.pack(pady=5)
        
        #Frame for buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame = tk.Frame(self.root, bg="lightgrey")
        self.button_frame.pack(pady=0.5)
        
        #Finish button
        self.finish_button = tk.Button(self.button_frame, text="Finish")
        self.finish_button.pack(side=tk.LEFT, padx=5)

        # Clear button 
        self.clear_button = tk.Button(self.button_frame, text="Clear")
        self.clear_button.pack(side=tk.LEFT, padx=5)

    #Finish button callback
    def on_finish_button_clicked(self, callback):
        self.finish_button.config(command=callback)

    #Scan button callback
    def on_scan_button_clicked(self, callback):
        self.scan_button.config(command=callback)

    #Update display with scanned product info
    def update_display(self, name, price):
        self.result_text.insert(tk.END, f"{name}: ${price:.2f}\n")
        self.result_text.see(tk.END)  # Scroll to the end of the text widget
     
    #Update subtotal display   
    def update_subtotal(self, subtotal):
        self.subtotal_label.config(text=f"Subtotal: ${subtotal:.2f}")
        
    #Clear button callback
    def on_clear_button_clicked(self, callback):
        self.clear_button.config(command=callback)
    
    #Start the GUI event loop
    def start(self):
        self.root.mainloop()
        