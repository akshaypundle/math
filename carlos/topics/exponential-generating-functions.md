# Exponential generating functions and labelled structures

Source lessons: [06-13 EGFs and sums of powers](../lessons/2026-06-13-exponential-generating-functions.png) ·
[06-21 EGFs vs. algebraic datatypes](../lessons/2026-06-21-exponential-generating-functions-vs-algebraic-datatypes.png) ·
[07-07 $e^{A(x)}$ and multinomial coefficients](../lessons/2026-07-07-exponential-generating-functions-multinomial-coefficients.png)

## 1. Definition: OGF vs. EGF (06-13)

| | map | $(1,1,1,\dots)\mapsto$ |
|---|---|---|
| ordinary (OGF) | $(a_0,a_1,\dots)\mapsto\sum a_nx^n$ | $\frac1{1-x}$ |
| exponential (EGF) | $(a_0,a_1,\dots)\mapsto\sum a_n\frac{x^n}{n!}$ | $e^x$ |

(The board also recalls $e^x=\lim_{n\to\infty}(1+\frac xn)^n$, $e=\lim(1+\frac1n)^n$.)

## 2. The product rule (06-21) and its meaning

**Claim.** If $A(x)=\sum a_n\frac{x^n}{n!}$ and $B(x)=\sum b_n\frac{x^n}{n!}$ then

$$A(x)B(x)=\sum_{n\ge0}\Bigl(\sum_{k=0}^n\binom nka_kb_{n-k}\Bigr)\frac{x^n}{n!}.$$

**Proof.** $[x^n]A B=\sum_{k=0}^n\frac{a_k}{k!}\cdot\frac{b_{n-k}}{(n-k)!}=\frac1{n!}\sum_k\binom nka_kb_{n-k}$. $\blacksquare$

**Why EGFs count labelled structures.** Suppose $a_n$ = the number of structures of type $A$ on the label set $[n]$ and $b_n$ likewise for $B$. A pair (an $A$-structure, a $B$-structure) on $[n]$ is built by: (1) choose the size $k$ of the label set of the left component; (2) choose *which* $k$ labels go left: $\binom nk$ ways; (3) put an $A$-structure on those labels and a $B$-structure on the remaining $n-k$: $a_kb_{n-k}$ ways. That is exactly the coefficient above. (The board contrasts this with OGFs, where the product counts pairs $(\alpha,\beta)$ with sizes adding, with no relabelling.) Sum $A+B$ counts "an $A$ or a $B$ structure" ("case classes", $T_1\cup T_2$), and $A\cdot B$ counts pairs ($T_1\times T_2$) with $\text{size}(t_1,t_2)=\text{size}(t_1)+\text{size}(t_2)$.

### Application: the binomial theorem (06-21 board)

Take $a_k=\alpha^k$, $b_k=\beta^k$: $A(x)=\sum\frac{(\alpha x)^k}{k!}=e^{\alpha x}$, $B(x)=e^{\beta x}$. Then $A(x)B(x)=e^{(\alpha+\beta)x}$ has $n$-th coefficient $(\alpha+\beta)^n$, while the product rule gives $\sum_k\binom nk\alpha^k\beta^{n-k}$. Hence $(\alpha+\beta)^n=\sum_k\binom nk\alpha^k\beta^{n-k}$. $\blacksquare$ (Compare the combinatorial proof in [counting-and-double-counting.md](counting-and-double-counting.md).)

## 3. Sums of powers via EGFs (06-13)

Let $S_k(n)=\sum_{i=1}^ni^k$ ($k\ge0$), so $S_0(n)=n$ and $S_1(n)=\frac{n(n+1)}2$.

### Elementary (telescoping) derivation

$(i+1)^{k+1}-i^{k+1}=\sum_{\ell=0}^k\binom{k+1}\ell i^\ell$ (binomial theorem). Sum over $i=1..n$; the left side telescopes:

$$(n+1)^{k+1}-1=\sum_{\ell=0}^k\binom{k+1}\ell S_\ell(n).$$

Isolating the $\ell=k$ term ($\binom{k+1}k=k+1$) gives the recursion boxed on the board:

$$S_k(n)=\frac{(n+1)^{k+1}-1-\sum_{\ell=0}^{k-1}\binom{k+1}\ell S_\ell(n)}{k+1}.$$

*Example ($k=2$).* $(n+1)^3-1=\binom30n+\binom31\frac{n(n+1)}2+3S_2(n)$, i.e. $n^3+3n^2+3n=n+\frac32n(n+1)+3S_2$, so $S_2(n)=\frac13n^3+\frac12n^2+\frac16n$. ✓

### EGF derivation (same identity, packaged)

Put $F_n(x)=\sum_{k\ge0}S_k(n)\frac{x^k}{k!}$. Swapping the sums, $F_n(x)=\sum_{i=1}^n\sum_k\frac{(ix)^k}{k!}=\sum_{i=1}^ne^{ix}=\dfrac{e^{(n+1)x}-e^x}{e^x-1}$ (geometric series in $e^x$; the board writes the version summing from $m=0$, $\frac{e^{(n+1)x}-1}{e^x-1}$, which differs only by the $i=0$ term, i.e. it counts $0^0=1$ in $S_0$). Multiply by $e^x-1=\sum_{j\ge1}\frac{x^j}{j!}$:

$$F_n(x)\,(e^x-1)=e^{(n+1)x}-e^x.$$

Take $\ [x^{k+1}]\cdot(k+1)!$: the left side is the EGF product of $(S_\ell(n))_\ell$ with $(1,1,1,\dots)$ restricted to $j\ge1$, i.e. $\sum_{\ell=0}^{k}\binom{k+1}\ell S_\ell(n)$, and the right side is $(n+1)^{k+1}-1$. This is the identity above. ✓ (This is the board's chain: $E\bigl((n+1)^{k+1}-1\bigr)=-\sum\binom{k+1}\ell S_\ell(n)$ rewritten via the product rule with the EGF $e^x-1$ of $(0,1,1,1,\dots)$.)

## 4. Algebraic datatypes as generating-function equations (06-21)

A recursive datatype defines a combinatorial class; sum types become $+$, product types become $\times$, and the size of a value is the sum of the sizes of its parts. Translate directly to an OGF equation (sizes only, no relabelling needed):

- **FibList.** `FibList = [] | 1 (FibList) | 2 (FibList)` where the value $1$ or $2$ contributes size $1$ or $2$ (the board: "finite list consisting of 1s and 2s, size $=\ell_1+\dots+\ell_k$"). Then
  $$F=1+xF+x^2F\ \Rightarrow\ F=\frac1{1-x-x^2},$$
  so the number of lists of total size $n$ is $[x^n]F=F_{n+1}$ (Fibonacci), equivalently the number of ways to climb $n$ steps taking 1 or 2 at a time (the staircase pictures on the board, and the $s_1+\dots+s_k=n$, $s_i\in\{1,2\}$ definition of $F_n$). Compare [ordinary-generating-functions.md](ordinary-generating-functions.md).
- **BinaryTree.** `BinaryTree = Node Int | Tree BinaryTree Int BinaryTree` with each `Int` of size $1$:
  $$B(x)=x+x\,B(x)^2.$$
  With $B=x\,C(x^2)$ where $C=1+yC^2$ is the Catalan series ($y=x^2$): indeed $x+x\cdot x^2C^2=x(1+x^2C^2)=xC$. So $B(x)=\dfrac{1-\sqrt{1-4x^2}}{2x}=\sum_kC_kx^{2k+1}$: the number of such trees with $2k+1$ nodes is the Catalan number $C_k$. (The board's tree pictures show the size-5 case.)

## 5. $e^{A(x)}$: sets of structures (07-07)

Given an EGF $A(x)=\sum_{k\ge1}a_k\frac{x^k}{k!}$ with $a_0=0$, the board studies the function $e^{A(x)}=\sum_{n\ge0}\frac{A(x)^n}{n!}$ and extracts its coefficients with two rules:

1. $[x^i]A(x)^n=\sum_{i_1+\dots+i_n=i}[x^{i_1}]A\cdots[x^{i_n}]A$ (expand the product),
2. $[x^i]C(x)D(x)=\sum_{s_1+s_2=i}[x^{s_1}]C\,[x^{s_2}]D$.

Therefore

$$[x^i]e^{A(x)}=\sum_{n\ge0}\frac1{n!}\sum_{i_1+\dots+i_n=i}\frac{a_{i_1}\cdots a_{i_n}}{i_1!\cdots i_n!}.$$

**Combinatorial meaning.** $A(x)^n$ counts ordered $n$-tuples of $A$-structures on a labelled set partitioned into $n$ non-empty blocks. The blocks have *distinct* label sets, so reordering produces $n!$ different ordered tuples of the same unordered collection: dividing by $n!$ counts **sets** of $n$ structures. So $e^{A(x)}$ is the EGF of "a set of $A$-structures" (no restriction on how many).

The board's picture of the same principle:
- $A=(1,1,1,\dots)$ has EGF $e^x$ ("sets": one structure on each label set), and $e^x-1$ is "non-empty sets".
- Two applications are in [set-partitions-and-involutions.md](set-partitions-and-involutions.md): $e^{e^x-1}$ (set partitions) and $e^{x+x^2/2}$ (involutions).

## 6. Binomial and multinomial coefficients (07-07, right side)

- $\binom nk=\#\{k\text{-subsets of }\{1..n\}\}=\binom n{k,\,n-k}$ ("$A$ and its complement").
- **Multinomial.** $\binom n{k_1,\dots,k_p}$ (with $k_1+\dots+k_p=n$) counts the ordered partitions of $\{1..n\}$ into blocks of sizes $k_1,\dots,k_p$.
  *Proof.* Choose the first block, then the second from what remains, and so on:
  $$\binom n{k_1}\binom{n-k_1}{k_2}\binom{n-k_1-k_2}{k_3}\cdots\binom{k_p}{k_p}=\frac{n!}{k_1!(n-k_1)!}\cdot\frac{(n-k_1)!}{k_2!(n-k_1-k_2)!}\cdots=\frac{n!}{k_1!\cdots k_p!},$$
  because the intermediate factorials cancel (the slash marks on the board) and $\binom{k_p}{k_p}=1$. $\blacksquare$

## Notes

- The right half of the 06-13 board also lists $\sum_n\frac{(e^{(n-1)x}-1)}{e^x-1}$ as an alternative form of $F_n(x)$ (consistent up to index shift) and the product/EGF rewriting $E(a_k)\cdot E(b_k)=\sum\frac{x^n}{n!}\sum_k\binom nka_kb_{n-k}$.
- The large grid sketch at upper left of the 06-21 board (curves and a staircase between $n$ and $h$) is a staircase/lattice picture that I could not interpret with confidence; I have only transcribed the algebra beside it.
