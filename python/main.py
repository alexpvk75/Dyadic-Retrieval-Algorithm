import math, json, os

base_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(base_dir, "..", "data", "superset.txt"), "r") as file:
    superset = [line.strip() for line in file]
with open(os.path.join(base_dir, "..", "data", "subsets.json"), "r") as file:
    subsets = json.load(file)

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

def create_subset():
    while True: 
        subset = input("Create a set named (type X to terminate): ") 
        if subset.strip().upper() == "X": 
            break 
        else: 
            subsets.update({subset: 0})
            while True: 
                insert = input("Adding element (type X to terminate): ") 
                if insert.strip().upper() == "X": 
                    break 
                elif insert in superset: 
                    subsets[subset] += 2**(superset.index(insert))
                    print("Element successfully added ") 
                else: 
                    print("Element doesn't exist")
            with open(os.path.join(base_dir, "..", "data", "subsets.json"), 'w') as f:
                json.dump(subsets, f, indent=4)
def output():
    while subsets:
        subset = input("Which group to output? (type X to terminate): ")
        if subset.strip().upper() == "X":
            break
        elif subset in subsets:
            print(f'{subset}: ', end="- ")
            chosen = dyadic(subsets[subset])
            for i in chosen:
                print((superset[int(math.log2(i))]).strip(), end=" - ")
            print("")
        else:
            print("Group not present in the file")
def all_sets():
    for subset in subsets:
        print(f'{subset}: ', end="- ")
        chosen = dyadic(subsets[subset])
        for i in chosen:
            print((superset[int(math.log2(i))]).strip(), end=" - ")
        print("")
def all_data():
    print('All items: ', end="- ")
    for item in superset:
        print(item, end = " - ")

# Main Program
def main():
    while True:
        for i in ["\nMenu","0. Exit","1. Create a subset",
                "2. Output a subset", "3. Show all subsets", "4. Show all items"]:
            print(i)
        scelta = int(input("\nYour option: "))
        print("")
        if scelta == 0:
            break
        elif scelta == 1:
            create_subset()
        elif scelta == 2:
            output()
        elif scelta == 3:
            all_sets()
        elif scelta == 4:
            all_data()
        else:
            print("Insert a valid value")
        print("")
if __name__ == "__main__":
    main()