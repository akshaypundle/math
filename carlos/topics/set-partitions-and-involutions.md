# Set partitions (Bell numbers) and involutions

Source lessons: [07-01 partitions of a set](../lessons/2026-07-01-partitions-of-a-set.png) ·
[07-14 number of partitions](../lessons/2026-07-14-number-of-partitions.png) ·
[07-14 number of involutions](../lessons/2026-07-14-number-of-involutions.png)

Both use the EGF toolkit of [exponential-generating-functions.md](exponential-generating-functions.md): the EGF of a product counts labelled pairs, $e^x$ is "sets", and $e^{A(x)}$ is "a set of $A$-structures".

## 1. Set partitions: $\sum b_n\frac{x^n}{n!}=e^{e^x-1}$

$b_n$ = the number of partitions of $[n]=\{1,\dots,n\}$ into non-empty blocks ("Bell numbers"). Small cases from the 07-01 board: $b_1=1$ ($\{1\}$); $b_2=2$ ($\{1,2\}$; $\{1\}\{2\}$); $b_3=5$ ($\{1,2,3\}$; $\{1,2\}\{3\}$; $\{1\}\{2,3\}$; $\{1,3\}\{2\}$; $\{1\}\{2\}\{3\}$). (The board also draws the 3-vertex graph with all edges and with none, anticipating the interpretation below.)

**Theorem.** $B(x)=\sum_{n\ge0}b_n\frac{x^n}{n!}=e^{e^x-1}$, with $b_0=1$.

**Proof** (07-14 board).

1. A **set** structure has exactly one structure on every label set: its sequence is $(1,1,1,\dots)$, EGF $\sum_{n\ge0}\frac{x^n}{n!}=e^x$. **Non-empty** sets: exclude $n=0$, EGF $e^x-1$.
2. A partition into exactly $n$ blocks is $n$ non-empty sets with distinct label sets. $(e^x-1)^n$ counts them as an ordered $n$-tuple (product rule: labelled pairs of non-empty sets, repeatedly), and since the label sets are disjoint and non-empty the $n!$ orderings are different, so $\dfrac{(e^x-1)^n}{n!}$ counts **unordered** collections of $n$ non-empty blocks (the board: "$n$ nonempty sets (unordered)").
3. Summing over the number of blocks:

$$B(x)=\sum_{n\ge0}\frac{(e^x-1)^n}{n!}=e^{e^x-1}.\ \blacksquare$$

**Equivalent graph picture (07-01).** $b_n$ is also the number of graphs on vertex set $[n]$ whose connected components are cliques (the components of such a graph form a partition of $[n]$, and conversely a partition determines the graph). The board's triangle and three isolated vertices are the two extreme cases for $n=3$.

### Consequences (derived from the theorem)

- **Recurrence.** $B'(x)=e^xB(x)$ (chain rule), so comparing $[x^n]$ with the EGF product rule: $b_{n+1}=\sum_{k=0}^n\binom nkb_k$. (Combinatorially: the block containing element $n+1$ has $n-k$ other elements, chosen in $\binom n{n-k}$ ways, and the other $k$ elements are partitioned freely.) Gives $1,1,2,5,15,52,203,877,\dots$ ✓.
- **Dobiński's formula.** $e^{e^x-1}=e^{-1}\sum_{k\ge0}\frac{e^{kx}}{k!}$, and $[x^n/n!]e^{kx}=k^n$, so $b_n=\frac1e\sum_{k\ge0}\frac{k^n}{k!}$. This is probably what the "$\sum\frac{k^n}{k!}$" scribbles on the 07-01 board are reaching for (the board writes $b_n=\sum_{k=1}^n\frac{k^n}{k!}$, which is not correct as written: it is missing the factor $1/e$ and the sum runs to $\infty$; its first terms $1,\ 1+2=3,\ \dots$ do not give $1,2,5$). Also on the board: the attempted recurrence "$b_n=b_{n-1}+\sum_kk\,b(n-1,k)$" where $b(n,k)$ is the number of partitions of $[n]$ into $k$ blocks: element $n$ is either a new singleton block ($b_{n-1}$ ways) or joins one of the $k$ blocks of a partition of $[n-1]$ with $k$ blocks ($k\,b(n-1,k)$ ways). That recurrence is correct; the next line on the board, "$b_n=b_{n-1}+b_{n-1}$" with a "??", looks like a stalled step: $\sum_kk\,b(n-1,k)$ is not equal to $b_{n-1}$ in general (e.g. $n=3$: $b(2,1)\cdot1+b(2,2)\cdot2=3\ne b_2=2$), so that line should not be read as a valid identity.

## 2. Involutions: $\sum i_n\frac{x^n}{n!}=e^{x+x^2/2}$

A **permutation** of $[n]$ is a bijection $\pi:[n]\to[n]$; an **involution** is a permutation with $\pi\circ\pi=\mathrm{id}$ (e.g. the swap $1\leftrightarrow2$ on $\{1,2\}$; the identity). $i_n$ = the number of involutions of $[n]$.

**Structure.** Draw the functional graph $x\to\pi(x)$. If $\pi\circ\pi=\mathrm{id}$ then for each $x$: either $\pi(x)=x$ (a fixed point, a singleton), or $\pi(x)=y\ne x$ and $\pi(y)=\pi(\pi(x))=x$ (the pair $\{x,y\}$ swapped). Conversely any partition of $[n]$ into singletons and pairs defines an involution (fix the singletons, swap the pairs). So

$$\text{involution of }[n]\ \longleftrightarrow\ \text{set of singletons and pairs partitioning }[n]\ (\text{"graphs on }[n]\text{ with this structure"}).$$

**Theorem.** $I(x)=\sum_{n\ge0}i_n\frac{x^n}{n!}=\exp\!\Bigl(x+\frac{x^2}2\Bigr)$.

**Proof.** The block structure ("a single block, which is a singleton or a pair") has exactly one structure on a label set of size 1 and one on a label set of size 2, none otherwise. Its EGF is $\frac{x}{1!}+\frac{x^2}{2!}=x+\frac{x^2}2$. An involution is a *set* of such blocks, so by the $e^{A(x)}$ principle $I(x)=e^{x+x^2/2}$. $\blacksquare$

*Note on the board:* it circles $e^{x+x^2}$ and expands $\sum\frac{(x+x^2)^n}{n!}$; the pair term should be $\frac{x^2}{2!}$, since a pair $\{x,y\}$ is one unordered structure on 2 labels. Check with $n=2$: $[x^2]e^{x+x^2/2}=\frac12+\frac12=1$, so $i_2=2!\cdot1=2$ ✓ (identity and the swap); with $x^2$ in place of $x^2/2$ one would get $i_2=3$, which is wrong.

### Consequences (derived)

- $I'(x)=(1+x)I(x)$, so $i_{n+1}=i_n+n\,i_{n-1}$ (element $n+1$ is fixed, or swapped with one of $n$ others).
- Explicit count: choose $k$ disjoint pairs: $i_n=\sum_{k=0}^{\lfloor n/2\rfloor}\dfrac{n!}{2^kk!(n-2k)!}$.
- Values: $1,1,2,4,10,26,76,232,764,2620$ ✓ (checked with both formulas).

## Related pattern

All three (sets, partitions, involutions) are instances of one picture: "structure on a label set $\to$ EGF $A(x)$; a **set** of such structures $\to e^{A(x)}$". Permutations as sets of cycles are the same with $A(x)=-\ln(1-x)$ (cycle EGF $\frac{(n-1)!x^n}{n!}$), giving $e^{-\ln(1-x)}=\frac1{1-x}$, i.e. $n!$ permutations — not on these boards but a good sanity check of the principle.
