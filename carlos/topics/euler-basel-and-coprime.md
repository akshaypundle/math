# Euler, the Basel sum, the Euler product, and coprime probability

Source lessons: [06-07 Euler: $\sum1/n^2$](../lessons/2026-06-07-generating-function-euler-sum-of-1-over-n-squared.png) ·
[06-12 probability two random integers are coprime](../lessons/2026-06-12-generating-function-prob-2-random-chosen-numbers.png)

## 1. The Basel problem: $\sum_{n\ge1}\frac1{n^2}=\frac{\pi^2}6$ (Euler, 1734)

**Euler's idea (board).** Let $f(x)=\dfrac{\sin x}{x}$ (with $f(0):=1$). Its roots are $\pm\pi,\pm2\pi,\pm3\pi,\dots$. Treat $f$ as an "infinite polynomial" with those roots and constant term $1$:

$$\frac{\sin x}x=\Bigl(1-\frac x\pi\Bigr)\Bigl(1+\frac x\pi\Bigr)\Bigl(1-\frac x{2\pi}\Bigr)\Bigl(1+\frac x{2\pi}\Bigr)\cdots=\prod_{n\ge1}\Bigl(1-\frac{x^2}{n^2\pi^2}\Bigr).$$

**Compare coefficients of $x^2$.**

- From the Taylor series $\sin x=x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots$ (valid for all real $x$): $\frac{\sin x}x=1-\frac{x^2}{3!}+\frac{x^4}{5!}-\cdots$, so $[x^2]\frac{\sin x}x=-\frac16$.
- From the product, the $x^2$ coefficient is $-\frac1{\pi^2}\bigl(1+\frac1{2^2}+\frac1{3^2}+\cdots\bigr)$, since only one factor can contribute its $x^2$ term.

Equating: $-\frac16=-\frac1{\pi^2}\sum\frac1{n^2}$, so

$$\boxed{\sum_{n=1}^\infty\frac1{n^2}=\frac{\pi^2}6}.$$

**Caveat.** This is Euler's original *heuristic*: a polynomial is determined by its roots and value at $0$, but an entire function need not be. It is made rigorous by the Weierstrass/Hadamard factorization, or by proofs such as the Fourier-series one; the board treats it intuitively, as Euler did.

Zeta notation on the board: $\zeta(s)=\sum_{n\ge1}n^{-s}$. $\zeta(1)=+\infty$ (harmonic series); $\zeta(r)<\infty$ for every $r>1$; $\zeta(\tfrac12)=\infty$; $\zeta(2)=\pi^2/6$; $\zeta(2k)$ is a rational multiple of $\pi^{2k}$; $\zeta(3)=\sum n^{-3}$ is *not* of that form (no closed form in $\pi$).

## 2. The Euler product

**Statement.** For $s>1$, $\displaystyle\zeta(s)=\prod_{p\text{ prime}}\frac1{1-p^{-s}}$.

**Proof.** For $|y|<1$, $\sum_{k\ge0}y^k=\frac1{1-y}$ (geometric series; the board's "For $|x|<1$, $\sum x^k=\frac1{1-x}$"). Multiply these over primes $p=2,3,5,\dots$ with $y=p^{-s}$:

$$\Bigl(\sum_{k\ge0}2^{-ks}\Bigr)\Bigl(\sum_{k\ge0}3^{-ks}\Bigr)\Bigl(\sum_{k\ge0}5^{-ks}\Bigr)\cdots=\sum_{(e_2,e_3,e_5,\dots)}(2^{e_2}3^{e_3}5^{e_5}\cdots)^{-s}.$$

By unique prime factorization every $n\ge1$, $n=p_1^{a_1}\cdots p_\ell^{a_\ell}$, appears exactly once as $2^{e_2}3^{e_3}\cdots$. The board expands the first two factors by hand: $\bigl(1+\frac1{2^s}+\frac1{4^s}+\cdots\bigr)\bigl(1+\frac1{3^s}+\frac1{9^s}+\cdots\bigr)$ contains $\frac1{n^s}$ for all $n$ whose only prime factors are $2,3$, etc. So the product equals $\sum n^{-s}$ (for $s>1$ everything converges absolutely, which justifies rearranging). $\blacksquare$

At $s=2$: $\zeta(2)=\Bigl(\frac1{1-2^{-2}}\Bigr)\Bigl(\frac1{1-3^{-2}}\Bigr)\Bigl(\frac1{1-5^{-2}}\Bigr)\cdots=\frac{\pi^2}6$ (the board's circled result; and $\frac{\pi^2}6\notin\mathbb Q$).

## 3. The probability that two random integers are coprime is $6/\pi^2$

The green note on the 06-07 board asks: take two integers $a,b$ "at random" (the board admits "random" is not yet defined). The probability they are coprime is $\frac6{\pi^2}=\frac1{\zeta(2)}$.

### 3a. Heuristic via the Euler product (06-12 board, right side)

1. For a random integer $n$, $P[p\mid n]=P[n\equiv0\ (\mathrm{mod}\ p)]=\frac1p$.
2. $a,b$ are coprime iff no prime divides both. $P[p\mid a\wedge p\mid b]=\frac1{p^2}$, so $P[p\nmid a\vee p\nmid b]=1-\frac1{p^2}$.
3. Treating different primes as independent:

$$P[\gcd(a,b)=1]=\prod_p\Bigl(1-\frac1{p^2}\Bigr)=\frac1{\prod_p(1-p^{-2})^{-1}}=\frac1{\zeta(2)}=\frac6{\pi^2},$$

which is the board's boxed "$\sum\frac1{n^2}=\frac{1}{(1-\frac1{2^2})(1-\frac1{3^2})\cdots}$" combined with §1.

The independence step is informal: there is no uniform probability measure on $\mathbb N$, so it is rigorous only as a statement about limiting frequencies in $[1,n]^2$ (see §3b and the references).

### 3b. Counting via Euler's totient (06-12 board, left side)

Let $P(n)=\dfrac{|\{(a,b)\in[n]^2:\gcd(a,b)=1\}|}{n^2}$. We want $\lim P(n)$.

**Pair count.** Write $\varphi(m)=|\{k\in[m]:\gcd(k,m)=1\}|=\sum_{k=1}^m[\gcd(k,m)=1]$. Pairs with $a\le b$ and $\gcd=1$: for each $b\ge2$ there are $\varphi(b)$ choices of $a$ (and $a=b$ is excluded since $\gcd(b,b)=b>1$); for $b=1$ there is the single pair $(1,1)$. By the symmetry $a\leftrightarrow b$, the total is

$$\#=1+2\sum_{b=2}^n\varphi(b)=2\sum_{b=1}^n\varphi(b)-1\quad(\text{since }\varphi(1)=1).$$

The board shows exactly this ($\frac1{n^2}(1+2\sum_{b=2}^n\varphi(b))$). Check for $n=5$: $\varphi=1,1,2,2,4$, sum $10$, count $19$ — matches a direct count of coprime pairs in $[5]^2$.

**Facts about $\varphi$ (board).**

- $\varphi(p^k)=p^k-p^{k-1}=p^{k-1}(p-1)$ (remove the multiples of $p$).
- $\varphi(ab)=\varphi(a)\varphi(b)$ if $\gcd(a,b)=1$ (Chinese remainder theorem).
- Hence for $n=p_1^{a_1}\cdots p_\ell^{a_\ell}$: $\varphi(n)=n\prod_i\bigl(1-\frac1{p_i}\bigr)$.
- $\sum_{d\mid n}\varphi(d)=n$. *Proof.* Sort $\{1..n\}$ by $g=\gcd(k,n)$. Those $k$ with $\gcd(k,n)=n/d$ correspond to $k/(n/d)\in[d]$ coprime to $d$: there are $\varphi(d)$ of them. Summing over $d\mid n$ counts all $n$ numbers. $\blacksquare$

**The limit** (my completion; the board stops after setting up $S(n)=\sum_{k\le n}\varphi(k)$). Möbius inversion of $\sum_{d\mid n}\varphi(d)=n$ gives $\varphi(k)=\sum_{d\mid k}\mu(d)\,\frac kd$, so

$$S(n)=\sum_{k\le n}\varphi(k)=\sum_{d\le n}\mu(d)\sum_{m\le n/d}m=\sum_{d\le n}\mu(d)\,\frac{\lfloor n/d\rfloor(\lfloor n/d\rfloor+1)}2=\frac{n^2}2\sum_{d\ge1}\frac{\mu(d)}{d^2}+O(n\log n),$$

and $\sum_d\mu(d)d^{-2}=\prod_p(1-p^{-2})=\frac1{\zeta(2)}$ (the Euler product again). So $S(n)\sim\frac{3}{\pi^2}n^2$ and $P(n)=\frac{2S(n)-1}{n^2}\to\frac6{\pi^2}$. Numerically $S(2000)/2000^2=0.3041$ vs. $3/\pi^2=0.3040$. $\blacksquare$

## 4. Asides on these boards

- **$1+2+3+4+\cdots=-\frac1{12}$** appears (crossed out/flagged) on the 06-12 board with $\zeta(k)=S(\infty,-k)=\lim_{n\to\infty}S(n,-k)$ and $S(k,n)=\sum_{i\le n}i^k$: the regularized value $\zeta(-1)=-\frac1{12}$, not a convergent sum.
- The 06-12 board also lists derivative rules for formal series: $(A+B)'=A'+B'$, $(AB)'=A'B+AB'$, $(x_0,x_1,x_2,\dots)'=(x_1,2x_2,3x_3,\dots)$, and $\sum nx^n=\frac x{(1-x)^2}$; and the recurrence $a_{n+1}=2a_n+n$ (solved in [ordinary-generating-functions.md](ordinary-generating-functions.md)).
- The 06-12 board writes $[x^n]\frac x{(1-x)^2}=n$; this is the same series as $(0,1,2,3,\dots)$.

## Sources

- [The probability that two random integers are coprime — Bureaux & Enriquez](https://arxiv.org/pdf/1612.03700) and [On the probability that two random integers are coprime — Lei & Kadane](https://arxiv.org/pdf/1806.00053): precise meaning of "random integer" (no countably additive uniform measure on $\mathbb N$).
- [Probability of Two Integers Being Coprime (cut-the-knot)](https://www.cut-the-knot.org/m/Probability/TwoCoprime.shtml); [Cushing your luck (The Aperiodical)](https://aperiodical.com/2013/06/cushing-your-luck-properties-of-randomly-chosen-numbers/): $1/\zeta(2)$ and the Basel value.
- The totient/Möbius completion in §3b is standard (e.g. Hardy & Wright, Thm. 331 as cited by Lei–Kadane); the numeric checks were run locally.
