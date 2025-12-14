# Dyadic Retrieval Algorithm - CLI v.2.1.0

A **simple Python terminal program** to manage a list of items (superset) and create smaller groups (subsets) using a clever math trick called **dyadic retrieval algorithm**. Each item in a subset can only appear once, and the program keeps everything saved for later.

---

## Features

- Add items to a **superset** (your master list)  
- Create **subsets** from items in the superset  
- Show any subset or all subsets  
- Show all items in the superset  
- Friendly **colored terminal output**  

---

## Requirements

- Python 3.10+ (should work on most Python 3 versions)  
- Terminal (Linux, macOS, Windows Terminal, or VS Code terminal)  
- No extra Python packages required  

> ⚠ On old Windows `cmd.exe`, colors may not work. Use **Windows Terminal** or **VS Code** terminal for full experience.

---

## Getting Started

1. **Download the code** to a folder on your computer.  
2. Open a terminal and navigate to that folder.  
3. Run the program:

```bash
python main.py
```
You’ll see a menu like this:
```bash
=== Menu ===
0. Exit
1. Form the superset
2. Show the superset
3. Create a subset
4. Output a subset
5. Show all subsets
```

---

### How to Use

---
1. **Form the superset**
- Choose option 1
- Type items you want in your master list, one at a time
- Type X when you’re done
> You will get colored messages:
>   - <span style="color: green;">Green</span> = item added<br>
>   - <span style="color: yellow;">Yellow</span> = item already exists
2. **Show the superset**
- Choose option 2
- See all items you have in your superset

3. **Create a subset**
- Choose option 3
- Give your subset a name
- Add items from your superset, one by one
- Type X to finish the subset
> Messages:
>   - <span style="color: green;">Green</span> = item added<br>
>   - <span style="color: yellow;">Yellow</span> = item already in subset<br>
>   - <span style="color: red;">Red</span> = item not in superset<br>

> You cannot create a subset until you have at least one item in the superset.

4. **Output a subset**
- Choose option 4
- Type the name of a subset
- See all items in that subset
- Type X to stop

5. **Show all subsets**
- Choose option 5
- Shows all your subsets and their items at once

0. **Exit**
- Choose option 0 to safely exit the program

---

### Notes

---
> Subsets are saved automatically in `subsets.json`

> Superset items are saved in `superset.txt`

> The program prevents duplicates in subsets

---

### The Math behind it all

---
In this program, each subset is represented by a single number, called the **sum identifier**. This number, denoted as $n$, is obtained by adding powers of two corresponding to the elements present in the subset. For example, if a superset has items ["Apple", "Banana", "Cherry"], we can assign $2^0$ to "Apple", $2^1$ to "Banana", and $2^2$ to "Cherry". Then the subset {"Apple", "Cherry"} has a sum identifier $n = 2^0 + 2^2 = 5$.

This sum identifier is unique for each subset because every combination of powers of two produces a different sum — this is why the algorithm is called **dyadic** (dyadic = “based on powers of two”). The function $D(n)$ recovers the original elements from the sum by repeatedly picking the largest power of two not exceeding $n$, subtracting it, and recursing on the remainder. This guarantees that every element in the subset appears only once.

We define $D(n)$ as:

```math
D(n) =
\begin{cases}
\emptyset, & \text{if } n = 0, \\
\{ 2^{k} \} \cup D(n - 2^{k}), & \text{if } n > 0,
\end{cases}
```

>Note: unlike formulas using $k = \left\lfloor \log_{2}(n) \right\rfloor$ here we select $k$ iteratively: starting from 0, we increase $k$ until $2^{k+1} > n$ then pick $2^k$

### Example

For $n = 13$:

```math
\begin{aligned}
D(13) &= \{2^{\lfloor \log_2 13 \rfloor}\} \cup D(13 - 8)
      = \{8\} \cup D(5), \\
D(5)  &= \{2^{\lfloor \log_2 5 \rfloor}\} \cup D(5 - 4)
      = \{4\} \cup D(1), \\
D(1)  &= \{1\} \cup D(0), \\
D(0)  &= \emptyset.
\end{aligned}
```

Therefore:

```math
D(13) = \{8, 4, 1\}.
```

Verifying:

```math
8+4+1=13
```