# Category theory: definition and first examples

Source lesson: [2026-07-22 category theory](../lessons/2026-07-22-category-theory.png)

This lesson is a definitions-and-examples board; there are no long proofs. Below are the definitions and, for each example, the small verification that it really is a category.

## Definition

A **category** consists of

1. a collection of **objects** ($A,B,C,\dots$);
2. a collection of **morphisms (arrows)** $f:A\to B$ between objects;
3. for every object $X$ an **identity** arrow $\mathrm{id}_X:X\to X$;
4. **composition**: for $f:A\to B$ and $g:B\to C$ an arrow $g\circ f:A\to C$;
5. laws: $f\circ\mathrm{id}_A=f$, $\ \mathrm{id}_B\circ f=f$, and composition is associative, $h\circ(g\circ f)=(h\circ g)\circ f$.

(The board's picture: $f:A\to B$, $g:B\to C$, $g\circ f:A\to C$, loops $\mathrm{id}_A,\mathrm{id}_B$; and the check $f(\mathrm{id}_A(t))=f(t)$ for functions.)

## Examples from the board

1. **Set.** Objects: sets. Arrows: functions. Identity: $x\mapsto x$. Composition of functions is associative and has the identity laws, as checked pointwise.

2. **Poset (or preorder) category.** Take a partially ordered set; objects are its elements, and there is *exactly one* arrow $a\to b$ iff $a\le b$. Identities exist by reflexivity ($a\le a$); composition $(b\le c)\circ(a\le b)=(a\le c)$ exists by transitivity; the laws hold automatically since there is at most one arrow between any two objects. Example drawn: $\dots\to-2\to-1\to0\to1\to2\to3\to\cdots$ with identity loops ($1\le3$ is the composite $1\to2\to3$).
   - *Partial order* requires antisymmetry ($a\le b$ and $b\le a\Rightarrow a=b$).
   - *Pre-order* requires only reflexivity and transitivity. The board's example is **divisibility**: $n\mid n$ and $a\mid b,\ b\mid c\Rightarrow a\mid c$. On the positive integers it is a partial order; on $\mathbb Z$ it is only a preorder since $a\mid -a$ and $-a\mid a$ with $a\ne-a$ ("perhaps $a=-b$"). The drawn diagram of $\mathrm{Div}$: $1\to2\to4\to\cdots$, $1\to3\to\cdots$.

3. **Grp.** Objects: groups. Arrows: group homomorphisms $\varphi:G\to H$ with $\varphi(ab)=\varphi(a)\varphi(b)$ (hence $\varphi(e_G)=e_H$, $\varphi(g^{-1})=\varphi(g)^{-1}$; see [group-theory-basics.md](group-theory-basics.md)). The composite of homomorphisms is a homomorphism, so it is a category. Example: $\mathbb Z\xrightarrow{\ \bmod n\ }\mathbb Z_n$ is a homomorphism because $(a+b)\bmod n=(a\bmod n)+(b\bmod n)$ in $\mathbb Z_n$.

4. **Hask** (programming languages with a nice type system, e.g. Haskell, Scala). Objects: types. Arrows: programs (functions) between types. Example: `add : ℤ × ℤ → ℤ`. The board notes the category is **Cartesian closed**: the type of functions $\mathbb Z\times\mathbb Z\to\mathbb Z$ is itself an object, equivalent to $\mathbb Z\to(\mathbb Z\to\mathbb Z)$ (currying).

5. **Board games.** A category for each board game (chess, tic-tac-toe); the board only names it ("board game ->") without defining the arrows, and I leave it undefined too.

6. **Graphs.** Two constructions:
   - **Path($G$)** for a directed graph $G$: objects are vertices, arrows $V\to W$ are *paths* from $V$ to $W$; composition is concatenation of paths, the identity is the empty path.
   - **Grph:** objects are graphs, arrows are graph homomorphisms (maps $f$ with $f(u)\sim f(v)\iff u\sim v$, as written on the board).

7. **Top.** Objects: topological spaces (sets with a notion of "open set"); arrows: continuous functions.

8. **Vect$_\mathbb R$.** Objects: real vector spaces; arrows: linear maps (e.g. $\mathbb R^n\to\mathbb R$).

## Notes

- The theme of the lesson: the *same* abstract definition covers sets, orders, groups, programs, graphs, spaces and vector spaces. A poset is a category with at most one arrow between any two objects; this is the sense in which "arrows generalize $\le$".
- Left of the board a stray "$x\in y$" is written at the top; unrelated to the definitions below it.
