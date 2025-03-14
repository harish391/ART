import csv
import random
import os

def generate_phone_number():
    """Generate a random 10-digit phone number as a string."""
    return str(random.randint(6000000000, 9999999999))

def save_phone_numbers(filename, count):
    """Generate and save phone numbers in a CSV file."""
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)  # Ensure directory exists

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Phone Number"])  # Header
        for _ in range(count):
            writer.writerow([generate_phone_number()])

    print(f"✅ Dataset created: {filename}")

# Define dataset sizes
datasets = {
    "phones_100.csv": 100,
    "phones_1000.csv": 1000,
    "phones_10000.csv": 10000,
    "phones_100000.csv": 100000
}

# Generate all datasets
for file, count in datasets.items():
    save_phone_numbers(file, count)
