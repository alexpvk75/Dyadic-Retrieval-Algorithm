# Dyadic Retrieval Algorithm

Let $n \in \mathbb{N}$.

Define $D(n)$ as the set of dyadic components (powers of two) whose sum equals $n$.

We define $D(n)$ recursively as:

```math
D(n) =
\begin{cases}
\emptyset, & \text{if } n = 0, \\
\{ 2^{k} \} \cup D(n - 2^{k}), & \text{if } n > 0,
\end{cases}
```

where

```math
k = \left\lfloor \log_{2}(n) \right\rfloor.
```

Thus, the algorithm repeatedly selects the highest power of two not exceeding $n$, subtracts it, and recurses on the remainder.

---

## Example

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