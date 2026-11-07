# Ordinary generating functions: formal power series, recurrences, Fibonacci, Catalan

Source lessons: [05-09](../lessons/2026-05-09-generating-function-1.png) ·
[05-21 Fibonacci](../lessons/2026-05-21-generating-function-fibonacci.png) ·
[05-27 Catalan](../lessons/2026-05-27-generating-function-catalan.png) ·
[06-06 Catalan (cont.)](../lessons/2026-06-06-generating-function-catalan-cont.png) ·
[06-13 recurrence example (left of board)](../lessons/2026-06-13-exponential-generating-functions.png)

## 1. Formal power series (05-09, 05-21)

Goals (05-09): find closed forms for recurrences; even without a closed form, read off asymptotics. Convergence is a nuisance, so treat a power series **formally**: an infinite sequence $(a_n)_{n\ge0}=(a_0,a_1,\dots)$ written $\sum a_nx^n$.

- Sum: $(a_n)+(b_n)=(a_n+b_n)$. Product (convolution): $(a_n)(b_n)=\bigl(\sum_{k=0}^na_kb_{n-k}\bigr)_n=(a_0b_0,\ a_1b_0+a_0b_1,\ \dots)$. Identities: $0=(0,0,\dots)$, $1=(1,0,0,\dots)$. $x^n=(0,\dots,0,1,0,\dots)$ with the $1$ in position $n$; $k=(k,0,0,\dots)$. These form the ring $\mathbb R[[x]]$. Sequences that are eventually $0$ behave like polynomials.
- Combinatorial reading: if $A$ counts structures "a" of size $n$ and $B$ counts structures "b" of size $n$, then $A+B$ counts "a or b" and $AB$ counts pairs $(a,b)$ with total size $n$.

**Geometric series.** $(1-x)(1+x+x^2+\cdots)=(1,-1,0,\dots)(1,1,1,\dots)=(1,0,0,\dots)=1$. So $1+x+x^2+\dots=\dfrac1{1-x}$ (meaning: it is the inverse of $1-x$ in the ring). Replace $x\to tx$: $\dfrac1{1-tx}=(1,t,t^2,\dots)$.

**Inverses.** *Claim:* $(a_n)$ has a multiplicative inverse iff $a_0\ne0$; the inverse is then unique.
*Proof.* Want $b$ with $\sum_{k\le n}a_kb_{n-k}=[n=0]$. For $n=0$: $a_0b_0=1$, which needs $a_0\ne0$ ($b_0=1/a_0$). For $n\ge1$: $b_n=-\frac1{a_0}\sum_{k=1}^na_kb_{n-k}$ is forced, so $b$ exists and is unique. Conversely if $a_0=0$ then every product has $0$-th term $0\ne1$. $\blacksquare$
Hence $1/x$ is *not* defined ($x=(0,1,0,\dots)$ has $a_0=0$), as the board notes.

## 2. Solving a recurrence: $a_0=1,\ a_{n+1}=2a_n+n$ (left of the 06-13 board)

Let $A(x)=\sum a_nx^n$. Multiply the recurrence by $x^{n+1}$ and sum over $n\ge0$:

$$A(x)-1=2xA(x)+\sum_{n\ge0}nx^{n+1}=2xA(x)+\frac{x^2}{(1-x)^2},$$

using $\sum nx^n=\frac{x}{(1-x)^2}$ (the sequence $(0,1,2,\dots)$ on the board). So $A(x)=\dfrac1{1-2x}+\dfrac{x^2}{(1-2x)(1-x)^2}$. Partial fractions give $A(x)=\dfrac2{1-2x}-\dfrac1{1-x}-\dfrac x{(1-x)^2}$, and reading off coefficients,

$$a_n=2^{n+1}-1-n.$$

Check: $a=1,2,5,12,\dots$; formula gives $1,2,5,12$. ✓ (The board's final line is $2^{n+1}-n-1$.)

The 05-27 board does a simpler version: $\dfrac1{(1-x)(1-2x)}=\dfrac{-1}{1-x}+\dfrac2{1-2x}$ (solving $A+B=1,\ -2A-B=0\Rightarrow A=-1,B=2$) so the coefficients are $2^{n+1}-1$ (the solution of $T_n=2T_{n-1}+1$, $T_0=1$; I could not tell if the board's $T_0$ was $0$ or $1$).

## 3. Fibonacci (05-21)

$F_0=0,F_1=1,F_{n+1}=F_n+F_{n-1}$; let $f=(F_0,F_1,\dots)$. The board's key observation: multiplying by $x^n$ shifts the sequence right by $n$ places.

$$f=(0,1,1,2,\dots),\quad xf=(0,0,1,1,\dots),\quad x^2f=(0,0,0,1,\dots)\ \Rightarrow\ (x+x^2)f=(0,0,F_2,F_3,\dots)=f-x,$$

because $F_{n+1}=F_n+F_{n-1}$ makes $(x+x^2)f$ agree with $f$ from index $2$ onward, while $f$ itself has $F_0=0$, $F_1=1$ at the front. Hence $x=(1-x-x^2)f$ and

$$\boxed{f=\frac{x}{1-x-x^2}}.$$

**Closed form.** $1-x-x^2=(1-\varphi x)(1-\psi x)$ with $\varphi=\frac{1+\sqrt5}2,\ \psi=\frac{1-\sqrt5}2$ (so $\varphi+\psi=1,\ \varphi\psi=-1$; these are $-1/r_{1,2}$ for the roots $r_{1,2}=\frac{-1\mp\sqrt5}2$ of $1-x-x^2$, as the board writes with $r_1=-\varphi$, $r_2=-\varphi^{-1}$). Partial fractions:

$$\frac x{(1-\varphi x)(1-\psi x)}=\frac1{\sqrt5}\Bigl(\frac1{1-\varphi x}-\frac1{1-\psi x}\Bigr),$$

and $\frac1{1-tx}=(1,t,t^2,\dots)$ (the board's "final step"), so

$$\boxed{F_n=\frac{\varphi^n-\psi^n}{\sqrt5}}.$$

(The board does the partial fractions in the form $\frac{1}{(x-r_1)(x-r_2)}=\frac{A}{x-r_1}+\frac B{x-r_2}$ with $A=-\frac1{\sqrt5},B=\frac1{\sqrt5}$ and rewrites $\frac1{x-t}=-\frac1t\cdot\frac1{1-x/t}$.) Verified numerically for $n<20$.

## 4. Catalan numbers (05-27, 06-06)

**Recurrence.** $C_0=1,\ C_{n+1}=\sum_{k=0}^nC_kC_{n-k}$ ($n\ge0$). Let $C(x)=\sum C_nx^n$ and write $[x^n]A(x)$ for the $n$-th coefficient. Two coefficient rules from the board: $[x^n](A+B)=[x^n]A+[x^n]B$, and $[x^n]AB=\sum_{k=0}^n[x^k]A\cdot[x^{n-k}]B$; also $[x^n](xP)=[x^{n-1}]P$.

**Functional equation.** $[x^{n+1}]C=\sum_kC_kC_{n-k}=[x^n]C^2=[x^{n+1}](xC^2)$ for $n\ge0$, and $[x^0]C=1$. Therefore

$$C(x)=1+x\,C(x)^2,\quad\text{i.e.}\quad xC^2-C+1=0.$$

**Solving.** Quadratic formula (in the region where the series converges): $C(x)=\dfrac{1\pm\sqrt{1-4x}}{2x}$. Which sign? Since $C(0)=C_0=1$, i.e. $\lim_{x\to0}C(x)=1$ (the continuity argument noted on the 06-06 board: "$C(x)$ must converge to a continuous function wherever it converges"):

- "$+$": $\dfrac{1+\sqrt{1-4x}}{2x}\to\pm\infty$ as $x\to0^+$. Rejected.
- "$-$": $\dfrac{1-\sqrt{1-4x}}{2x}=\dfrac{4x}{2x(1+\sqrt{1-4x})}\to1$. ✓

So $C(x)=\dfrac{1-\sqrt{1-4x}}{2x}$.

**Coefficients via the binomial series.** For any real $r$, $(1+x)^r=\sum_{k\ge0}\binom rkx^k$ with $\binom rk=\dfrac{r(r-1)\cdots(r-k+1)}{k!}$. (The board motivates this as: for $n\in\mathbb N$ this is the usual binomial theorem, and the falling-factorial form makes sense for $r=\tfrac12$: "a power series for $\sqrt{1+x}$".) Then

$$\sqrt{1-4x}=\sum_{k\ge0}\binom{1/2}k(-4x)^k,\qquad C(x)=-\frac1{2x}\sum_{k\ge1}\binom{1/2}k(-4)^kx^k=\sum_{k\ge0}2\binom{1/2}{k+1}(-4)^kx^k,$$

the boxed expression on the board. Simplifying (my step; the board stops here) gives $C_n=\dfrac1{n+1}\binom{2n}n$: e.g. $n=1$: $2\cdot\binom{1/2}2\cdot(-4)=2\cdot(-\tfrac18)(-4)=1$; $n=2$: $2\cdot\tfrac1{16}\cdot16=2$. Numerically $1,1,2,5,14,42,132,429,\dots$ ✓.

**Convergence remarks (06-06).** The series $\sum C_nx^n$ cannot converge for $x>\tfrac14$ because the square root $\sqrt{1-4x}$ is non-real there; the radius of convergence is $\tfrac14$. The board also writes out $C(\tfrac14)=C_0+\tfrac14C_1+\tfrac1{16}C_2+\dots>1$ while probing the boundary of the region. (Independently, $C_n\sim4^n/(\sqrt\pi\,n^{3/2})$ confirms radius $\tfrac14$.) The trailing "$\sum 1/n^2=?$" at the bottom of the board leads into the next lesson: [euler-basel-and-coprime.md](euler-basel-and-coprime.md).

## Notes

- 06-06's heading says "catalan.cont": it is the continuation of the 05-27 board (the explicit/implicit forms "$C=\frac{1-\sqrt{1-4x}}{2x}$, $C^2-C+1=0$" in the top-right corner). I dated it June 6 because it ends on the Basel question that opens the June 7 lesson; the original filename read "june-67".
- Binary trees with $B=x+xB^2$ (counted by Catalan numbers) appear in [exponential-generating-functions.md](exponential-generating-functions.md).
