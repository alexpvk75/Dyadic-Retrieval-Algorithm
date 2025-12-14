import os, json, math

# Base paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data")
txt_path = os.path.join(data_dir, "superset.txt")
json_path = os.path.join(data_dir, "subsets.json")
os.makedirs(data_dir, exist_ok=True)

# Initialize files
if not os.path.exists(txt_path):
    open(txt_path, "w", encoding="utf-8").close()

if not os.path.exists(json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({}, f, indent=4)

# Read superset
with open(txt_path, "r", encoding="utf-8") as f:
    superset = [line.strip() for line in f if line.strip()]

# Read subsets
try:
    with open(json_path, "r", encoding="utf-8") as f:
        subsets = json.load(f)
        if not isinstance(subsets, dict):
            subsets = {}
except (json.JSONDecodeError, FileNotFoundError):
    subsets = {}

### Core Algorithm
def dyadic(suma, elements=None):
    if elements is None: elements = []
    if suma == 0:
        elements.sort()
        return elements
    i = 0
    while 2**(i + 1) <= suma:
        i += 1
    elements.append(2**i)
    return dyadic(suma - 2**i, elements)
###

def save_subsets():
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(subsets, f, indent=4)

def create_superset():
    print("\033[34m=== Superset Creation ===\033[0m")
    while True:
        item = input("Insert an item (X to stop): ").strip()
        if item.upper() == "X":
            break
        if item in superset:
            print("\033[33mElement already exists\033[0m")
            continue

        with open(txt_path, "a", encoding="utf-8") as f:
            f.write(item + "\n")

        superset.append(item)
        print("\033[32mItem added\033[0m")

def create_subset():
    print("\033[34m=== Subset Creation ===\033[0m")
    while True:
        name = input("Create a subset named (X to stop): ").strip()
        if name.upper() == "X":
            break

        if name in subsets:
            print("\033[33mSubset already exists\033[0m")
            continue

        subsets[name] = 0

        while True:
            insert = input("Add element (X to stop): ").strip()
            if insert.upper() == "X":
                break
            if insert not in superset:
                print("\033[31mElement does not exist\033[0m")
                continue
            item = 2 ** superset.index(insert)
            check = dyadic(subsets[name])
            if item in check:
                print("\033[33mElement already in the subset\033[0m")
            else:
                subsets[name] += item
                print("\033[32mElement added\033[0m")

        save_subsets()

def output_subset():
    if not subsets:
        print("\033[33mNo subsets available\033[0m")
        return
    print("\033[34m=== Subset Output ===\033[0m")
    while True:
        name = input("Which subset to output? (X to stop): ").strip()
        if name.upper() == "X":
            break
        if name not in subsets:
            print("\033[31mSubset not found\033[0m")
            continue

        print(f"\033[1;44m{name}\033[0m", end=": - ")
        chosen = dyadic(subsets[name])
        for i in chosen:
            print(f'\033[36m{superset[int(math.log2(i))]}', end=" - \033[0m")
        print()

def all_sets():
    if not subsets:
        print("\033[33mNo subsets available\033[0m")
        return
    print("\033[34m=== All Subsets ===\033[0m")
    for name in subsets:
        print(f"\033[1;44m{name}\033[0m", end=": - ")
        chosen = dyadic(subsets[name])
        for i in chosen:
            print(f'\033[36m{superset[int(math.log2(i))]}', end=" - \033[0m")
        print()

def all_data():
    if not superset:
        print("\033[33mSuperset is empty\033[0m")
        return
    print("\033[34m=== Superset Items ===\033[0m")
    print("\033[36m- ", end="\033[0m")
    for item in superset:
        print(f'\033[36m{item}', end=" - \033[0m")
    print()

def main():
    menu = [
        "0. Exit",
        "1. Create the superset",
        "2. Create a subset",
        "3. Output a subset",
        "4. Show all subsets",
        "5. Show all items"
    ]

    while True:
        print("\n\033[1;34m=== Menu ===\033[0m")
        for m in menu:
            print(f'\033[34m{m}\033[0m')

        try:
            choice = int(input("\nYour option: "))
        except ValueError:
            print("\033[31mInsert a number\033[0m")
            continue

        print()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            create_superset()
        elif choice == 2:
            create_subset()
        elif choice == 3:
            output_subset()
        elif choice == 4:
            all_sets()
        elif choice == 5:
            all_data()
        else:
            print("\033[31mInvalid option. Choose a number from the menu\033[0m")

if __name__ == "__main__":
    main()