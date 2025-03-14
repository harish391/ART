from btree import BTree
from art import AdaptiveRadixTree
from database import load_phone_numbers
import time

# Dataset filenames
datasets = {
    1: "phones_100.csv",
    2: "phones_1000.csv",
    3: "phones_10000.csv",
    4: "phones_100000.csv"
}

# Select dataset size
print("\nSelect dataset size:")
for key, value in datasets.items():
    print(f"{key}. {value}")

choice = int(input("Enter choice (1-4): "))
filename = datasets.get(choice, "phones_100.csv")

# Load dataset
phone_numbers = load_phone_numbers(filename)

# Initialize B-Tree (degree 4)
btree = BTree(4)
for num in phone_numbers:
    btree.insert(num)

# Initialize Adaptive Radix Tree
art = AdaptiveRadixTree()
for num in phone_numbers:
    art.insert(num)

# Get user input for search
search_number = input("\nEnter phone number to search: ").strip()

# Search in B-Tree
start_time = time.time()
found_btree = btree.search(search_number)
btree_time = (time.time() - start_time) * 1000

# Search in Adaptive Radix Tree
start_time = time.time()
found_art = art.search(search_number)
art_time = (time.time() - start_time) * 1000

# Display results
print("\n🔍 Search Results:")
print(f"📂 B-Tree: {'✅ Found' if found_btree else '❌ Not Found'} | ⏱ {btree_time:.4f} ms")
print(f"🌳 Adaptive Radix Tree: {'✅ Found' if found_art else '❌ Not Found'} | ⏱ {art_time:.4f} ms")
