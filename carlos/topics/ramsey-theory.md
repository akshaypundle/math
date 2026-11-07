# Ramsey theory: $R(3,3)=6$, Ramsey's theorem, the binomial bound, $R(4,4)=18$

Source lessons (chronological):
[02-27](../lessons/2026-02-27-ramsey-numbers.png) ·
[03-01](../lessons/2026-03-01-ramsey-theorem.png) ·
[03-06](../lessons/2026-03-06-ramsey-numbers-bounds-4-4.png) ·
[04-10](../lessons/2026-04-10-ramsey-numbers-r44-is-18.png) (+ [alt](../lessons/2026-04-10-ramsey-numbers-r44-is-18-alt.png)) ·
[04-16](../lessons/2026-04-16-ramsey-numbers-r44-is-18.png) (+ [alt](../lessons/2026-04-16-ramsey-numbers-r44-is-18-alt.png)).
Code: [`../code/ramsey-4-4.py`](../code/ramsey-4-4.py).

**Setup.** Colour the edges of the complete graph $K_N$ with two colours. $R(r,s)$ is the least $N$ such that every colouring has a red $K_r$ or a blue $K_s$. (The 02-27 board uses green/purple and writes $R(n,m)$.) Immediate facts: $R(r,s)=R(s,r)$ (swap colours), $R(r,2)=r$ (either some edge is blue, or all edges are red and form a red $K_r$).

## 1. $R(3,3)=6$

**Lower bound, $R(3,3)>5$.** Colour $K_5$ with a red 5-cycle (the outer pentagon) and a blue 5-cycle (the pentagram). Neither colour contains a triangle. This is the 5-vertex picture on the 02-27 and 03-01 boards.

**Upper bound, $R(3,3)\le6$.** Take any colouring of $K_6$ and a vertex $v$. Its 5 edges have two colours, so at least 3 have the same colour, say red to $a,b,c$. If any of $ab,bc,ac$ is red, it forms a red triangle with $v$. Otherwise $abc$ is a blue triangle. $\blacksquare$

**The double-counting attempt on the 02-27 board (reading).** The board counts, for $K_6$, the purple edges $P$ and green edges $G$ via triangles: each edge lies in 4 triangles, so $4P=\sum_{\triangle}P(\triangle)$, $4G=\sum_\triangle G(\triangle)$, and $P(\triangle)+G(\triangle)=3$ gives $4(P+G)=3\binom63=60$, i.e. $P+G=15$. If there were no monochromatic triangle each triangle has 1 or 2 purple edges, so $20\le4P\le40$, i.e. $5\le P,G\le10$. That is consistent with $P+G=15$, so this count alone does **not** yield a contradiction; the pigeonhole argument above is the one that proves $R(3,3)\le6$. (I am reading the faint handwriting; the numbers $15$, $20\le4P\le40$, $5\le P\le10$ are legible.)

## 2. Ramsey's theorem: $R(r,s)$ exists

**Statement.** For all $r,s\ge2$, $R(r,s)$ exists.

**Proof** (induction on $r+s$, the board's $Q(N)$). Base: $R(r,2)=r$, $R(2,s)=s$ exist; in particular $R(2,2)=2$ (the case $r+s=4$).

Step: assume $R(r-1,s)$ and $R(r,s-1)$ exist. **Claim:** $R(r,s)\le R(r-1,s)+R(r,s-1)$.

Take a colouring of $K_N$ with $N=R(r-1,s)+R(r,s-1)$ and a vertex $v$. Let $R_v$ be its red neighbours and $B_v$ its blue neighbours; $|R_v|+|B_v|=N-1=R(r-1,s)+R(r,s-1)-1$. If both $|R_v|\le R(r-1,s)-1$ and $|B_v|\le R(r,s-1)-1$, the sum would be at most $N-2$, so either $|R_v|\ge R(r-1,s)$ or $|B_v|\ge R(r,s-1)$.

- *Case $|R_v|\ge R(r-1,s)$.* Inside $R_v$ there is a red $K_{r-1}$ or a blue $K_s$. A red $K_{r-1}$ plus $v$ is a red $K_r$.
- *Case $|B_v|\ge R(r,s-1)$.* Symmetric: a blue $K_{s-1}$ plus $v$ is a blue $K_s$, or $B_v$ already holds a red $K_r$.

Either way the colouring has a red $K_r$ or a blue $K_s$. $\blacksquare$

## 3. The explicit bound $R(r,s)\le\binom{r+s-2}{r-1}$

The 03-01 board turns the inequality into the recurrence $U(r,2)=r$, $U(2,s)=s$, $U(r,s)=U(r-1,s)+U(r,s-1)$, so $R(r,s)\le U(r,s)$ by induction. The 03-06 board then solves it with Pascal's identity.

**Proof** (induction on $r+s$). Base: $\binom{r}{r-1}=r$ and $\binom{s}{1}=s$. Step:

$$R(r,s)\le R(r-1,s)+R(r,s-1)\le\binom{r+s-3}{r-2}+\binom{r+s-3}{r-1}=\binom{r+s-2}{r-1}.\ \blacksquare$$

Sample consequences: $R(3,3)\le\binom42=6$, $R(4,4)\le\binom63=20$ (the board also tabulates the binomials in a grid). It also lists $43\le R(5,5)\le46$; further bounds for $R(6,6)$ and $R(10,10)$ are on that board but the handwriting is too small for me to transcribe them reliably.

## 4. $R(4,4)=18$

Notation on the 04-10 board: "$n\to(b,r)$" means every colouring of $K_n$ (blue/red) has a blue $K_b$ or red $K_r$; so $R(b,r)$ is the least such $n$. Known: $6\to(3,3)$, $4\to(2,4)$.

### Upper bound: $18\to(4,4)$

**Lemma (parity improvement).** Let $n_1\to(b,r-1)$ and $n_2\to(b-1,r)$. Then $n_1+n_2\to(b,r)$, and if $n_1,n_2$ are both even then already $n_1+n_2-1\to(b,r)$.

*Proof.* Take a colouring of $K_N$, $N=n_1+n_2-1$ (the weaker claim with $N=n_1+n_2$ is the argument of §2). Each vertex $v$ has $N-1=n_1+n_2-2$ neighbours.

- If $\deg_R(v)\ge n_1$: the red neighbourhood has $\ge n_1\to(b,r-1)$, so it contains a blue $K_b$ (done) or a red $K_{r-1}$ (add $v$: a red $K_r$).
- If $\deg_B(v)\ge n_2$: symmetrically, a blue $K_{b-1}$ plus $v$ is a blue $K_b$, or a red $K_r$ appears.

So if the colouring has no blue $K_b$ and no red $K_r$, no vertex can satisfy either condition: $\deg_R(v)\le n_1-1$ and $\deg_B(v)\le n_2-1$ for all $v$. Their sum is $n_1+n_2-2$, so both are equalities: $\deg_R(v)=n_1-1$ for every $v$. If $n_1$ is even, $n_1-1$ is **odd**, and $N=n_1+n_2-1$ is odd. So the graph has an odd number of vertices, each with odd red degree, and $\sum_v\deg_R(v)$ is odd. But by the [handshake lemma](counting-and-double-counting.md) it equals $2|E_R|$, which is even. Contradiction. $\blacksquare$

**Applications.**

- $R(3,4)\le9$: take $b=3,r=4$, $n_1=R(3,3)=6$, $n_2=R(2,4)=4$, both even, so $6+4-1=9$. (Known: $R(3,4)=9$.)
- $R(4,4)\le R(4,3)+R(3,4)=9+9=18$.

### Lower bound: $17\not\to(4,4)$ (Paley graph on $\mathbb Z_{17}$)

Vertices $0,1,\dots,16$. Let $Q=\{x^2\bmod17\}=\{1,2,4,8,9,13,15,16\}$ be the non-zero quadratic residues (squares $1,4,9,16,25\equiv8,36\equiv2,49\equiv15,64\equiv13$). Colour $\{x,y\}$ red if $x-y\in Q$, blue otherwise. This is well defined since $-1\equiv4^2\in Q$ (the board checks $x>y$ and $x-y\in\{1,2,4,8,9,13,15,16\}$). Each vertex has red degree 8 and blue degree 8.

**Facts about $Q$** (via a primitive root $g=3$, $\mathbb Z_{17}^\times=\{g^0,\dots,g^{15}\}$, $g^{16}=1$): $Q$ is exactly the set of even powers of $g$. *Proof:* $(g^t)^2=g^{2t}$ is even. Conversely if $g^m=(g^t)^2$ with $m$ odd then $g^{m-2t}=1$ forces $16\mid m-2t$, impossible by parity. Hence:

- $Q\cdot Q=Q$, $N\cdot N=Q$, $Q\cdot N=N$ ($N$ = non-residues = odd powers), as in the board's multiplication table.
- **Symmetry.** Multiplying all vertices by $q\in Q$ maps red edges to red edges (since $q(x-y)\in Q\iff x-y\in Q$); multiplying by a non-residue swaps the colours (the board writes $nx - ny$, $n^{-1}x-n^{-1}y$). So the graph is isomorphic to its complement, and translations $x\mapsto x+r$ are also symmetries.

**No red $K_4$.** Suppose $\{a,b,c,d\}$ is a red $K_4$. Translate by $-a$ and scale by $(b-a)^{-1}\in Q$ (allowed since $b-a\in Q$): we may assume the clique is $\{0,1,p,q\}$. Red edges to $0$ and $1$ require $p,q\in Q$ and $p-1,q-1\in Q$. Checking $Q$:

| $p\in Q$ | 1 | 2 | 4 | 8 | 9 | 13 | 15 | 16 |
|---|---|---|---|---|---|---|---|---|
| $p-1\in Q$ ? | no ($0$) | yes | no ($3$) | no ($7$) | yes | no ($12$) | no ($14$) | yes |

So $p,q\in\{2,9,16\}$ (the board boxes exactly these three). But $2-9\equiv10$, $2-16\equiv3$, $9-16\equiv10$, none in $Q$, so no two of them are red-adjacent. Contradiction. (Checked by brute force over all $\binom{17}{4}$ subsets.)

**No blue $K_4$.** Multiplication by a non-residue (say 3) maps a blue $K_4$ to a red $K_4$. $\blacksquare$

So $R(4,4)\ge18$, and with the upper bound, $R(4,4)=18$.

## Notes

- The "Theory-builders vs. problem-solvers" remark in the top-right of the 03-06 board (Euler/Gauss/Grothendieck vs. Erdős) and the van der Waerden question beside it are asides; the latter is picked up in [van-der-waerden.md](van-der-waerden.md).
- The `-alt` images are slightly different exports of the 04-10 and 04-16 boards with the same content.
- References: Greenwood–Gleason (1955) first showed the 17-vertex lower bound; see e.g. [Proving that R(4,4)>17 (Plus Magazine)](https://plus.maths.org/proving-r4417). The web sources I found did not spell out the parity argument for the upper bound, so §4's lemma is my write-up of what the 04-10 board sketches (the board's own labels: $n_1\to(b,r-1)$, $n_2\to(b-1,r)$, odd/even degrees, "$\sum\deg v=2|E|$ even!").
