# Dyadic Retrieval Algorithm

## What is this?

This is a fun little program that lets you create groups of items and use the "dyadic algorithm" to break down numbers into powers of 2. It's a cool way to organize data using binary math!

## How it Works

The program has a **superset** - a master list of all possible items. Then you can create **subsets** - smaller groups of items you want. Each item is assigned a power of 2 (like 1, 2, 4, 8, 16, etc.), and when you add items to a group, it adds up their values.

The dyadic algorithm then takes that sum and breaks it back down into the original powers of 2 to show you which items are in that group.

## How to Use It

1. Add items to `superset.txt` from `Data` folder
2. Run `main.py` from the Python folder
2. You'll see a menu with 4 options:
   - **Create a subset** - Make a new group and add items to it
   - **Output a subset** - See what items are in a specific group
   - **Show all subsets** - View all your groups and their items
   - **Show all items** - List everything in the superset
4. Your groups are saved automatically to `subsets.json`

## Files

- `superset.txt` - All the available items you can add
- `subsets.json` - Your saved groups (created when you add items)
- `main.py` - The program itself
