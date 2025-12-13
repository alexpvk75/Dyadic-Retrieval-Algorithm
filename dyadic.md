# Dyadic Decomposition Algorithm

Let $n \in \mathbb{N}$<br> 
Define $D(n)$ as the set of dyadic components (powers of two) whose sum equals $n$.

<br>We define $D(n)$ recursively as:

$$
D(n) =
\begin{cases}
\emptyset, & \text{if } n = 0, \\[10pt]
\{ 2^{k} \} \cup D(n - 2^{k}), & \text{if } n > 0,
\end{cases}
$$

where

$$
k = \left\lfloor \log_{2}(n) \right\rfloor.
$$

Thus, the algorithm repeatedly selects the highest power of two not exceeding $n$, subtracts it, and recurses on the remainder.

---

## Example

For \( n = 13 \):

$$
\begin{aligned}
D(13) &= \{2^{\lfloor \log_2 13 \rfloor}\} \cup D(13 - 8)
      = \{8\} \cup D(5), \\[8pt]
D(5)  &= \{2^{\lfloor \log_2 5 \rfloor}\} \cup D(5 - 4)
      = \{4\} \cup D(1), \\[8pt]
D(1)  &= \{1\} \cup D(0), \\[8pt]
D(0)  &= \emptyset.
\end{aligned}
$$

Therefore:

$$
D(13) = \{8, 4, 1\}.
$$
