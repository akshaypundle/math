# Finite calculus: summation by parts, and the Euclidean algorithm

Source image (undated, filed in `misc/`): [finite calculus + Euclid's GCD](../misc/finite-calculus-summation-by-parts-and-euclid-gcd.png).
The file's timestamp is 2026-04-16; the content matches the first chapters of Concrete Mathematics (difference calculus) and the Euclidean algorithm.

## 1. Difference operator and product rule

Let $\Delta f(x)=f(x+1)-f(x)$ and let $E$ be the shift, $Ef(x)=f(x+1)$.

**Product rule.** $\Delta(fg)=(\Delta f)\,g+E(f)\,(\Delta g)$.

**Proof.**

$$f(x{+}1)g(x{+}1)-f(x)g(x)=\bigl(f(x{+}1)-f(x)\bigr)g(x)+f(x{+}1)\bigl(g(x{+}1)-g(x)\bigr).\ \blacksquare$$

Summing (telescoping) both sides over a range gives **summation by parts**:

$$\sum(\Delta f)\,g\ \delta x=fg-\sum E(f)\,(\Delta g)\ \delta x$$

(the board writes the indefinite sums as $\sum\dots\delta x$, the boxed line).

## 2. Exponentials, and an example

$\Delta(b^x)=b^{x+1}-b^x=(b-1)\,b^x$. In particular $\Delta(2^x)=2^x$, so $2^x$ plays the role of $e^x$ ("is its own difference").

**Example: $\sum k\,2^k\,\delta k$.** Take $f=2^k$ (so $\Delta f=2^k$) and $g=k$ (so $\Delta g=1$):

$$\sum k\,2^k\,\delta k=k\,2^k-\sum2^{k+1}\cdot1\,\delta k=k\,2^k-2\cdot2^k=(k-2)\,2^k$$

(the board's chain: $\ k\cdot2^k-\sum2^{k+1}$, then $k\cdot2^k-2\sum2^k$, then $k\cdot2^k-2^{k+1}$). So $\sum_{k=0}^{n-1}k\,2^k=(n-2)2^n+2$; check $n=2$: $0+2=2$, formula $0+2=2$ ✓; $n=3$: $0+2+8=10$, formula $(3-2)\cdot8+2=10$ ✓.

## 3. The Euclidean algorithm (lower half of the board)

Let $D(a,b)=\gcd(a,b)$.

**Observation.** $D(a,b)=D(a-b,\,b)=D(a,\,b-a)$, and more generally $D(a,b)=D(a,\,b-qa)$ for every integer $q$.

**Proof.** The pairs $(a,b)$ and $(a,b-qa)$ have the same set of common divisors: a number dividing $a$ and $b$ divides $b-qa$, and a number dividing $a$ and $b-qa$ divides $(b-qa)+qa=b$. Same common divisors, same greatest one. $\blacksquare$

In particular $D(a,b)=D(a,\,b\bmod a)$ with $0\le b\bmod a\le a-1$ (the board's "note").

**Algorithm (board's steps).** 1. We have $D(a,b)$. 2. If $a>b$ go to $D(a\bmod b,\ b)$, else to $D(a,\ b\bmod a)$. Each step replaces the larger number by its remainder modulo the smaller, so the pair strictly decreases; the process stops at $D(0,m)=m$. The last board line unrolls two steps: $a<b$: $D(a,b)=D(a,b\bmod a)=D\bigl(a\bmod(b\bmod a),\,b\bmod a\bigr)$.

## Notes

- A small yellow box (blank) and a teal tick in the middle of the image are leftover marks; nothing is written in them.
