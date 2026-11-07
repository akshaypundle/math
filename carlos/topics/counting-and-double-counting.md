# Counting and double counting

Source lessons: [2026-02-11 proving bijections](../lessons/2026-02-11-proving-bijections.png), pigeonhole fragment at left of [2026-02-27 Ramsey numbers](../lessons/2026-02-27-ramsey-numbers.png).

## Iverson bracket

For a proposition $P$, $[P]=1$ if $P$ is true and $0$ otherwise. Rules (check by truth table):

1. $[P \wedge Q]=[P][Q]$
2. $[P \vee Q]=[P]+[Q]-[P][Q]$
3. $[\neg P]=1-[P]$

Cardinality as a sum: for finite $X$ and $S\subseteq X$, $|S|=\sum_{x\in X}[x\in S]$.
Hence $n-|S|=\sum_{t\in[n]}\bigl(1-[t\in S]\bigr)=\sum_{t\in[n]}[t\notin S]$ (used below).

The technique of the whole lesson: write a count as a double sum of brackets, swap the order of summation, and evaluate the other way.

## Handshake lemma

**Statement.** For a finite undirected graph $G=(V,E)$ (edges are 2-element subsets of $V$), $\sum_{v\in V}\deg(v)=2|E|$.

**Proof.** $\deg(v)=|\{e\in E: v\in e\}|=\sum_{e\in E}[v\in e]$. So

$$\sum_{v}\deg(v)=\sum_{v}\sum_{e}[v\in e]=\sum_{e}\sum_{v}[v\in e]=\sum_{e}|\{v: v\in e\}|=\sum_{e}2=2|E|.$$

The swap is legal because both sums are finite. The set being double counted is $\{(v,e)\in V\times E : v\in e\}$. $\blacksquare$

**Corollary** (used in [Ramsey theory](ramsey-theory.md)): the number of odd-degree vertices is even; in particular a graph on an odd number of vertices cannot have all degrees odd.

## $\sum_k \binom nk = 2^n$

**Proof.** $\binom nk=|\{S\subseteq[n]:|S|=k\}|=\sum_{S\subseteq[n]}[|S|=k]$. Sum over $k=0..n$ and swap:

$$\sum_{k=0}^n\binom nk=\sum_{S\subseteq[n]}\sum_{k=0}^n[|S|=k]=\sum_{S\subseteq[n]}1=|\mathcal P([n])|=2^n,$$

since for each $S$ exactly one $k$ (namely $|S|$) makes the bracket $1$. $\blacksquare$

## Binomial theorem

**Statement.** $(x+y)^n=\sum_{k=0}^n\binom nk x^ky^{n-k}$.

**Proof.** Expand the product $\prod_{t=1}^n(x+y)$: choosing $x$ or $y$ from each factor $t$ corresponds to choosing the set $S\subseteq[n]$ of factors that give $x$. So

$$(x+y)^n=\sum_{S\subseteq[n]}\prod_{t\in[n]}x^{[t\in S]}y^{[t\notin S]}=\sum_{S\subseteq[n]}x^{|S|}y^{\,n-|S|}.$$

Group the $S$ by size $k=|S|$; there are $\binom nk$ of each size. $\blacksquare$

(The board example: $n=3$, $S=\{1,3\}$ picks $x\cdot y\cdot x$.)
A second proof, via exponential generating functions, is in [exponential-generating-functions.md](exponential-generating-functions.md).

## Pigeonhole: a block of terms divisible by $N$ (fragment)

The left margin of the 02-27 board poses: given $a_1,\dots,a_N\in\mathbb N$, is there a nonempty $S$ with $N\mid\sum_{k\in S}a_k$? It lists the prefix sums $a_1,\ a_1+a_2,\ \dots,\ a_1+\dots+a_N$, which is the standard proof:

**Claim.** Some nonempty block of *consecutive* terms has sum divisible by $N$.

**Proof.** Let $s_j=a_1+\dots+a_j \bmod N$ for $j=1..N$. If some $s_j=0$, the block $a_1..a_j$ works. Otherwise the $N$ values lie in $\{1,\dots,N-1\}$, so two coincide, $s_i=s_j$ with $i<j$, and $a_{i+1}+\dots+a_j\equiv 0\pmod N$. $\blacksquare$

## Notes

- The file name of the lesson says "bijections", but what is on the board is the Iverson-bracket / double-counting toolkit; no explicit bijection is proved there.
- The right-hand scrawl of the board (the $\prod x^{[t\in S]}y^{[t\notin S]}$ expansion and the "$S=\{1,3\}$" example) is the binomial-theorem proof above.
