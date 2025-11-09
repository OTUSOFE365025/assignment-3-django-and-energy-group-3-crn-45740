#controller.py
""" Controller module for the Cash Register application. """

import datetime
import tkinter as tk
import tkinter.messagebox as messagebox
from db.models import Product
from Cash_Register.scanner_for_app import generate_upc

class Controller:
    def __init__(self, view):
        self.view = view
        self.subtotal = 0.0 #track running subtotal
        self.scanned_items = [] #list of scanned items 
        self.view.on_scan_button_clicked(self.handle_scan) #executes scan button function
        self.view.on_finish_button_clicked(self.export_receipt) #executes finish button function
        self.view.on_clear_button_clicked(self.clear_transaction) #executes clear button function
    
    def handle_scan(self):
        upc = self.view.upc_entry.get().strip() #get UPC from entry box
        if not upc: #if user presses can with no UPC code entered
            messagebox.showwarning("Input Error", "Please enter a UPC code.")
            return
        
        if not upc.isdigit(): #if user enters characters in UPC
            messagebox.showerror("Invalid UPC", "UPC must contain digits only.")
            self.view.upc_entry.delete(0, tk.END)
            return
        
        try:
            product = Product.objects.get(upc=upc) #query databse via Django-ORM method (.get())
            self.subtotal += float(product.price) #add to subtotal
            self.scanned_items.append((product.name, float(product.price))) #track scanned item
            self.view.update_display(product.name, product.get_rounded_price()) #update product display
            self.view.update_subtotal(self.subtotal) #update subtotal display  
            self.view.upc_entry.delete(0, tk.END)  #clear entry box after scan
        except Product.DoesNotExist:
                self.view.update_display("Product Not Found", 0.00)
        
    
    def clear_transaction(self):
        self.scanned_items.clear()
        self.subtotal = 0.0
        self.view.result_text.delete(1.0, tk.END)
        self.view.update_subtotal(self.subtotal)
                
    def export_receipt(self):
        if not self.scanned_items:
            messagebox.showwarning("No Items", "No items scanned for receipt. Please scan at least one item before printing receipt.")
            return #exit early, don't export empty receipt
        
        #generate receipt content
        try:
            receipt_lines = [
                "Receipt",
                "---------------------"
            ]
            #All scanned items
            for name, price in self.scanned_items:
                receipt_lines.append(f"{name}: ${price:.2f}")
            
            receipt_lines.append("---------------------")
            receipt_lines.append(f"Total: ${self.subtotal:.2f}")
            
            receipt_text = "\n".join(receipt_lines)
            
            #Generate timestamped filename
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"receipt_{timestamp}.txt"
            
            #save to file
            with open(filename, "w") as f:
                f.write(receipt_text)

            #show full receipt in message box
            messagebox.showinfo("Export Successful", receipt_text)
            
        except Exception as e: #Receipt fails to generate and save
            messagebox.showerror("Error", f"Failed to save receipt: {e}")