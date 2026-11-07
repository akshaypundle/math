# Shannon (1948): capacity of a discrete noiseless channel

Source lesson: [2026-08-14 Shannon's paper, part 1](../lessons/2026-08-14-shannons-paper-1.png). Also see `~/repos/books/entropy.pdf` (the paper), Part I, Section 1 ("The discrete noiseless channel").

## Setting and definition

A channel transmits sequences of symbols $S_1,\dots,S_n$ with durations $t_1,\dots,t_n$ (for example telegraph dots/dashes/spaces). Let $N(T)$ be the number of distinct allowed signals of duration $T$.

**Capacity** (board, with units): 

$$C=\lim_{T\to\infty}\frac{\log N(T)}{T}.$$

With $\log_2$ the unit is **bits** ($\log_2N$: if there are 32 messages, $\log_232=5$ bits), and $C$ is in bits per second (the board's "bits/second", "$\#$ of length $t$").

## Case 1: free choice of symbols

**Recurrence.** Condition on the last symbol: a signal of duration $T$ ends with some $S_i$ (duration $t_i$) preceded by an arbitrary signal of duration $T-t_i$:

$$N(T)=N(T-t_1)+N(T-t_2)+\dots+N(T-t_n).$$

This is a linear recurrence with constant coefficients ("has const. coeff."), so its solutions are combinations $c_1\lambda_1^T+\dots+c_n\lambda_n^T$ where the $\lambda_i$ are roots of the characteristic equation. For large $T$ the term with the largest real root $\lambda_0$ dominates: $N(T)=\Theta(\lambda_0^T)$ (board: "$\Theta(\lambda^t)$").

Substituting $N(T)=\lambda^T$ into the recurrence and dividing by $\lambda^T$:

$$1=\lambda^{-t_1}+\dots+\lambda^{-t_n}.$$

So $\lambda_0$ is the largest real root of this equation and

$$C=\lim\frac{\log N(T)}T=\log\lambda_0.$$

*Shannon's telegraph example* (four symbols: dot $=2$, dash $=4$, letter space $=3$, word space $=6$ time units, with two spaces never adjacent, so the effective "symbols" are dot, dash, dot+letter space, dash+letter space, dot+word space, dash+word space, of durations $2,4,5,7,8,10$): the equation is $\lambda^{-2}+\lambda^{-4}+\lambda^{-5}+\lambda^{-7}+\lambda^{-8}+\lambda^{-10}=1$, with largest root $\lambda_0\approx1.4529$, so $C=\log_2\lambda_0\approx0.539$ bits per time unit (computed locally).

## Case 2: a finite-state channel (the DFA on the board)

Now only some symbol sequences are allowed. Model it as a finite automaton with states $1,\dots,p$; in state $i$ the allowed symbols are indexed by $s$, the $s$-th one takes duration $b_{ij}^{(s)}$ and leads to state $j$ (board: the DFA with states $\{\cdot,-,\,\}$ and $\{\cdot,-,1,11\}$ and the durations $b_{12}^{(1)},b_{12}^{(2)},\dots$).

Let $N_j(T)$ = the number of signals of duration $T$ that **end in state $j$**. Condition on the last transition:

$$N_j(T)=\sum_{i=1}^p\sum_sN_i\bigl(T-b_{ij}^{(s)}\bigr),\qquad j=1,\dots,p,$$

and $N(T)=N_1(T)+\dots+N_p(T)$.

**Ansatz.** For large $T$, $N_j(T)\sim k_j\lambda^T$ with the *same* growth rate $\lambda$ for every $j$ (the board: "$\lambda$ independent of $j$"). Substituting and dividing by $\lambda^T$:

$$k_j=\sum_{i}\sum_sk_i\lambda^{-b_{ij}^{(s)}},\qquad j=1,\dots,p.$$

In matrix form, with $M(\lambda)_{ij}=\sum_s\lambda^{-b_{ij}^{(s)}}$ (the board's $\bigl[\sum_s\lambda^{-b^{(s)}_{ij}}\bigr]_{i,j}$), this reads $\vec k=M(\lambda)^{\mathsf T}\vec k$, i.e. $\bigl(M(\lambda)^{\mathsf T}-I_p\bigr)\vec k=\vec0$. A **non-trivial** solution $\vec k\ne0$ exists iff the matrix is **not invertible** (the board's remark "$M\vec v=\vec 0$ has a non-trivial solution iff $M$ is not invertible"), i.e.

$$\det\Bigl(\Bigl[\sum_s\lambda^{-b_{ij}^{(s)}}\Bigr]_{ij}-I_p\Bigr)=0$$

(transposing does not change the determinant). The growth rate $\lambda_0$ is the **largest real root** of this determinant equation, and then $N(T)=\Theta(\lambda_0^T)$, so

$$\boxed{C=\log\lambda_0}.$$

This is Shannon's Theorem 1: *"the channel capacity $C$ is $\log W$, where $W$ is the largest real root of the determinant equation $\bigl|\sum_sW^{-b_{ij}^{(s)}}-\delta_{ij}\bigr|=0$"* ($\delta_{ij}$ is the Kronecker delta, i.e. $I_p$). Case 1 is the special case of a single state.

## Notes and gaps

- **What is not proved on the board:** that $N_j(T)\sim k_j\lambda^T$ at all, and that the dominant root is real and the right one. The rigorous argument is Perron–Frobenius for the non-negative matrix $M(\lambda)$ (for an irreducible channel). The board, like Shannon, uses the ansatz.
- Shannon's own treatment is in Part I, Section 1 of the paper. Confirmed by search: he defines $C=\lim_{T\to\infty}\frac{\log N(T)}T$, derives $N(T)=N(T-t_1)+\dots+N(T-t_n)$, and states that for large $T$ the count is dominated by $X_0^T$ where $X_0$ is the largest real root of $X^{-t_1}+\dots+X^{-t_n}=1$, giving $C=\log X_0$.
- Sources: [Shannon 1948 (UVM copy)](https://www.uvm.edu/~cvincen1/files/teaching/spring2018-math382/shannon.pdf), [Yale copy](https://www.cs.yale.edu/homes/yry/readings/general/shannon1948.pdf), [reading notes](https://vvkahpm.github.io/notes/Information%20Theory/Reading_Shannon_1948/).
- The top of the board ($L_1][L_2$, "$2^{L_1+L_2}$" crossed out) is a scratch comparison of concatenated messages: lengths add under concatenation but the *count* of messages multiplies, which is why one takes $\log N$ to get something additive ($\log_2$ of a product is the sum of the logs).
