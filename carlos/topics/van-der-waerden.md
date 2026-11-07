# Van der Waerden's theorem

Source lesson: [2026-04-23 van der Waerden](../lessons/2026-04-23-van-der-waerden.png)

**Question on the board.** If we colour $1,2,\dots,N$ with $c$ colours, can we force a long monochromatic arithmetic progression (AP)? $W(c,L)$ is the least $N$ such that every $c$-colouring of $\{1..N\}$ contains a monochromatic AP of length $L$.

**Theorem (van der Waerden).** $W(c,L)$ exists for all $c,L$.

## $W(2,3)=9$

**Lower bound ($W(2,3)>8$).** Colour $1..8$ as R R B B R R B B. Red is $\{1,2,5,6\}$, blue $\{3,4,7,8\}$. No three elements of $\{1,2,5,6\}$ form an AP (check the four triples $\{1,2,5\},\{1,2,6\},\{1,5,6\},\{2,5,6\}$: the gaps are $1,3$ / $1,4$ / $4,1$ / $3,1$, never equal), and $\{3,4,7,8\}$ is the same set shifted by $2$. So there is no monochromatic 3-AP. (The board's "Part 1"; verified by brute force.)

**Upper bound ($W(2,3)\le9$).** Every 2-colouring of $1..9$ has a monochromatic 3-AP (board's "Part 2").

*Proof (case analysis).* Suppose not. By symmetry of colours let $5$ be red. Each of $\{4,6\},\{3,7\},\{2,8\},\{1,9\}$ then contains a blue element (else a red 3-AP centred at 5). Consider $4$ and $6$:

1. *Both blue.* $(2,4,6)$ and $(4,6,8)$ force $2$ and $8$ red; then $(2,5,8)$ is a red AP. Contradiction.
2. *Both red.* $(4,5,6)$ is red. Contradiction.
3. *Exactly one blue.* The reflection $x\mapsto10-x$ preserves APs and fixes $5$, so assume $4$ blue, $6$ red.
   - $(5,6,7)$: $5,6$ red, so $7$ is blue.
   - $(1,4,7)$: $4,7$ blue, so $1$ is red.
   - $(1,5,9)$: $1,5$ red, so $9$ is blue.
   - $(7,8,9)$: $7,9$ blue, so $8$ is red.
   - $(2,5,8)$: $5,8$ red, so $2$ is blue.
   - $(2,3,4)$: $2,4$ blue, so $3$ is red.
   - Now $1,3,5$ are all red: an AP. Contradiction. $\blacksquare$

## Why $W(c,L)$ exists (the lesson's idea, and the full proof)

**What the board does.** It sketches the "columns" idea: cut $\{1..N\}$ into blocks of length $m$; a block of length $m$ has one of $c^m$ colourings, so if $N/m\ge W(c^m,L)$ the blocks themselves, viewed as $c^m$ "super-colours", contain an AP of $L$ *identical* blocks ("an arithmetic sequence of identical columns"). For $W(2,3)$ the board uses blocks of length $5$ ($2^5=32$ colourings, so any $33$ blocks contain two equal ones; the third block of the AP is the next in the progression). It then tries to turn an AP of length $L$ into one of length $L+1$ and writes a bound involving $W(2,L)$ and $W(2^{W(2,L)},L)$. I could not read that final inequality reliably, and it is stated for $c=2$ only, so I give the standard complete argument instead.

**Full proof** (double induction; the "colour-focusing" argument, as in Graham–Rothschild–Spencer; see sources). Induct on $L$: $L=1,2$ are trivial. Assume $W(c,L-1)$ exists for *all* $c$. Fix $c$.

*Colour-focused APs.* APs $A_i=\{a_i+jd_i: 0\le j\le L-2\}$, $i=1..r$, are **colour-focused at $f$** if each $A_i$ is monochromatic, the colours are pairwise distinct, and $a_i+(L-1)d_i=f$ for all $i$.

**Claim($r$).** For each $r\le c$ there is $M(r)$ such that every $c$-colouring of $[1,M(r)]$ contains a monochromatic $L$-AP or $r$ colour-focused $(L-1)$-APs with focus $f\le M(r)$.

- *Claim($c$) finishes the proof.* The focus $f$ has one of the $c$ colours, which equals the colour of some $A_i$, and then $A_i\cup\{f\}$ is a monochromatic $L$-AP.
- *Claim(1).* By the induction hypothesis $[1,W(c,L-1)]$ contains a monochromatic $(L-1)$-AP $A_1=\{a_1+jd_1\}$ with $a_1+(L-2)d_1\le W(c,L-1)$, hence $d_1\le W(c,L-1)$ and its focus $a_1+(L-1)d_1\le2W(c,L-1)=:M(1)$. One colour-focused AP is just a monochromatic $(L-1)$-AP.
- *Claim($r-1$)$\Rightarrow$Claim($r$).* Let $M=M(r-1)$, $m=M$, and $N=W(c^{m},L-1)$. Cut $[1,(2N+1)m]$ into blocks of length $m$; give each block the "super-colour" given by its colouring pattern, one of $c^m$ values. By the induction hypothesis on $L$, among the first $N$ blocks there are blocks $B_0,B_1,\dots,B_{L-2}$ with indices $s,s+t,\dots,s+(L-2)t$ ($t\ge1$) that are *identically coloured*. Inside $B_0$ apply Claim($r-1$) to the relative positions $1..m$: either a monochromatic $L$-AP (done), or $r-1$ colour-focused $(L-1)$-APs with relative starts $a_i$, steps $d_i$, and common relative focus $f=a_i+(L-1)d_i\le m$. Since no monochromatic $L$-AP arose, $f$'s colour differs from every $A_i$'s colour.
  Define, in absolute positions, for $i<r$: $A_i'=\{sm+a_i+k(d_i+tm):0\le k\le L-2\}$. Its $k$-th element is the relative position $a_i+kd_i$ inside block $B_k$ (block $B_k$ starts at $(s+kt)m$), and $B_k$ is coloured like $B_0$, so $A_i'$ is monochromatic in the colour of $A_i$. Define $A_r'=\{sm+f+ktm:0\le k\le L-2\}$, the position $f$ in each $B_k$: monochromatic in the colour of $f$. The $r$ colours are distinct, and each $A_i'$ has focus $sm+f+(L-1)tm$ (for $i<r$ because $a_i+(L-1)d_i=f$). That focus is at most $(s+(L-1)t+1)m\le(2N+1)m=:M(r)$. So Claim($r$) holds. $\blacksquare$

## Aside on the same board: the IMO-1988 Vieta-jumping problem

The red box at the very top of the board is an unrelated problem (I read it as the numerator/denominator written with the roles swapped, but it is surely this one): *if $a,b$ are positive integers and $k=\frac{a^2+b^2}{ab+1}$ is an integer, then $k$ is a perfect square* (IMO 1988, Problem 6).

*Proof (Vieta jumping).* Suppose $k$ is not a square. Among all positive-integer solutions of $a^2-kab+b^2=k$ take one with $a+b$ minimal, $a\ge b$. As a quadratic in $a$ it has roots $a$ and $a'=kb-a=\dfrac{b^2-k}{a}$. $a'$ is an integer. If $a'=0$ then $b^2=k$, a square. If $a'\le-1$ then $a'^2-ka'b+b^2\ge1+k+1>k$, contradicting the equation. So $a'\ge1$, and $a'=\frac{b^2-k}{a}<\frac{b^2}{a}\le b\le a$. Then $(a',b)$ is a solution with smaller sum. Contradiction. $\blacksquare$

## Sources

- [Van der Waerden's theorem (Wikipedia)](https://en.wikipedia.org/wiki/Van_der_Waerden%27s_theorem): value $W(2,3)=9$ and the double-induction outline.
- [Proof of van der Waerden's theorem (opentext.uleth.ca)](https://opentext.uleth.ca/Ramsey/sec_proof_vdW.html) and Blondal–Jungić, *Proof of van der Waerden's Theorem in Nine Figures*: colour-focusing proof. The $W(2,3)$ case analysis above is my own and was checked by brute force (the unique-up-to-symmetry extremal colouring of $1..8$ is RRBBRRBB / BBRRBBRR).
