# Group theory basics: orders, homomorphisms, isomorphism invariants

Source lesson: [2026-01-28 classification of groups](../lessons/2026-01-28-classification-of-groups.png)

## Definitions (from the board)

A group $(G,\cdot)$: associative, with an identity $e$ ($ge=eg=g$) and inverses ($g^{-1}g=gg^{-1}=e$). Not necessarily commutative ($ab\ne ba$ may happen).

- **Order of the group** $|G|$: the number of elements.
- **Order of an element** $\operatorname{ord}(g)$: the least $k\ge1$ with $g^k=e$, or $\infty$ if none exists.
- Small examples listed: $\mathbb Z_1,\dots,\mathbb Z_4$ under $+$, with the element orders $(1)$, $(1,2)$, $(1,3,3)$, $(1,4,2,4)$; and $(\mathbb R,+)$, where every non-zero element has order $\infty$.

## Cancellation ("sudoku property")

**Claim.** $gh=gk\Rightarrow h=k$ (and likewise on the right). So every row and column of the multiplication table of a finite group contains each element exactly once.

**Proof.** Multiply on the left by $g^{-1}$. $\blacksquare$

## Every element of a finite group has finite order

**Statement.** If $G$ is finite, every $g\in G$ has $\operatorname{ord}(g)\le|G|$.

**Proof.** Consider $g^1,g^2,\dots,g^{|G|+1}$: $|G|+1$ elements of a set of size $|G|$, so by pigeonhole $g^i=g^j$ for some $1\le i<j\le|G|+1$. Cancelling $g^i$ gives $g^{j-i}=e$ with $1\le j-i\le|G|$. $\blacksquare$

(The board restricts to $g^1..g^{|G|}$ and excludes the identity to get the same conclusion; the version above is the cleanest.)

## Cyclic behaviour

For a fixed $g$ the powers $g^n$ either exhaust $G$ or not.

- **Finite $G$, powers exhaust $G$:** $g^n\leftrightarrow n$ matches $G$ with $(\mathbb Z_{|G|},+)$.
- **Infinite $G$, powers exhaust $G$:** $g^n\leftrightarrow n$ matches $G$ with $(\mathbb Z,+)$ (the board lists $\dots,g^{-2},g^{-1},g^0,g^1,g^2,\dots$).

The matching is a group isomorphism in the sense below, because $g^ig^j=g^{i+j}$.

## Homomorphisms

A **homomorphism** $\varphi:(G,\cdot)\to(H,*)$ is a map with $\varphi(ab)=\varphi(a)*\varphi(b)$ ("preserves structure"; "relabelling" on the board).

**Consequences.**

1. $\varphi(e_G)=e_H$. *Proof.* $\varphi(e_G)=\varphi(e_Ge_G)=\varphi(e_G)\varphi(e_G)$; cancel $\varphi(e_G)$ in $H$. $\blacksquare$
2. $\varphi(g^{-1})=\varphi(g)^{-1}$. *Proof.* $\varphi(g)\varphi(g^{-1})=\varphi(gg^{-1})=\varphi(e_G)=e_H$. $\blacksquare$

An **isomorphism** is a homomorphism with an inverse homomorphism ($\varphi^{-1}\circ\varphi=\mathrm{id}_G$; equivalently, a bijective homomorphism).

## Invariants: orders

**Claim.** If $\varphi:G\to H$ is an isomorphism, then $g$ and $\varphi(g)$ have the same order.

**Proof.** $g^k=e_G\iff\varphi(g^k)=e_H\iff\varphi(g)^k=e_H$. The first "$\Leftarrow$" uses injectivity (only $e_G$ maps to $e_H$), the second equivalence is the homomorphism property. $\blacksquare$

**Consequence (the lesson's strategy for classifying groups).** For a group $G$, compute the multiset $S(G)$ of the orders of its elements. Isomorphic groups have equal $S(G)$, so different multisets prove that two groups are *not* isomorphic. For instance $S(\mathbb Z_3)=\{1,3,3\}\ne S(\mathbb Z_4)=\{1,4,2,4\}$.

## Notes

- The board is a definitions-and-first-lemmas lesson; the pigeonhole proof and the order invariant are the only real proofs, and both are given above.
- The board only claims that element orders are *an* invariant under isomorphism; it does not claim that $S(G)$ determines the group.
