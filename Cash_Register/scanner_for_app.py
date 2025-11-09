#scanner_for_app.py
""" Scanner module for the Cash Register application. """

import random

def generate_upc(file_name="prodInfo.txt"):
    """ Simulate scanning by randomly selecting a UPC from the product file. """
    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()
            if lines:
                line = random.choice(lines)
                parts = line.strip().split()
                if len(parts) >= 1:
                    return int(parts[0])
    except Exception as e:
        print(f"Error generating UPC: {e}")
    return None