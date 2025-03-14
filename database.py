import random
import csv

def generate_phone_number():
    return str(random.randint(6000000000, 9999999999))

def save_phone_numbers(filename, count):
    phone_numbers = [generate_phone_number() for _ in range(count)]
    
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Phone Number"])  # Add header
        for number in phone_numbers:
            writer.writerow([number])  # Save as string
    
    return phone_numbers

def load_phone_numbers(filename):
    phone_numbers = []
    
    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            phone_numbers.append(row[0].strip())  # Strip spaces
    
    return phone_numbers
