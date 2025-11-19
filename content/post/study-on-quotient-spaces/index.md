---
date: 2025-11-18T21:23:25+0800
draft: false
katex: true
obsidian_aliases:
- Study on Quotient Spaces
- Quotient Spaces
tags:
- math
- linear-algebra
title: Study on Quotient Spaces
---

I'm reading *Linear Algebra Done Right* by Axler and found the section on quotient spaces difficult to understand, so I researched and took these notes.

## Definitions

{{< callout type="definition" icon="fas fa-book" title="3.95 notion: $v + U$" fold="" >}}

Suppose `$v \in V$` and `$U \subseteq V$`. Then `$v + U$` is the subset of `$V$` defined by
``` katex
\[v + U = \{v + u : u \in U\}.\]
```

{{< /callout >}}

Also called a translate. **Attention** that a translate is a set.

{{< callout type="definition" icon="fas fa-book" title="3.97 definition: *translate*" fold="" >}}

Suppose `$v \in V$` and `$U \subseteq V$`, the set `$v + U$` is said to be a *translate* of `$U$`.

{{< /callout >}}

Quotient space is a set of all translates (set of sets):

{{< callout type="definition" icon="fas fa-book" title="3.99 definition: *quotient space*, $V/U$" fold="" >}}

Suppose `$U$` is a subspace of `$V$`. Then the *quotient space* `$V/U$` is the set of all translates of `$U$`. Thus
``` katex
\[V/U = \{v + U : v \in V\}.\]
```

{{< /callout >}}

Quotient space is a set of sets. There are duplicates for each `$v \in V$` because for some `$v_1, v_2 \in V$`, `$v_1 + U$` and `$v_2 + U$` can be identical set.

A quotient space `$V/U$` is formed by "collapsing" a subspace `$U$` to zero within a larger vector space `$V$`. This construction is based on an equivalence relation where two vectors `$x, y \in V$` are considered equivalent if their difference lies in `$U$`—that is, `$x \sim y$` if and only if `$x - y \in U$`. [wikipedia](https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra))

## Lemmas

{{< callout type="definition" icon="fas fa-book" title="3.101 *two translates of a subspace are equal or disjoint*" fold="" >}}

Suppose `$U$` is a subspace of `$V$` and `$v, w \in V$`. Then
``` katex
\[
v - w \in U \iff v + U = w + U \iff (v + U) \cap (w + U) \neq \emptyset
\]
```

{{< /callout >}}

If two translates are not disjoint (the union set is not empty), they must be equal. So they are equal or disjoint.

All distinct translates of a subspace are disjoint. Given any `$v \in V$`, it belongs to only one translate.

Since the quotient space `$V/U$` is a set of translates of a subspace, it is like a disjoint partition of values in `$V$`. By using the definition of quotient map

{{< callout type="definition" icon="fas fa-book" title="3.104 definition: *quotient map*, $\\pi$" fold="" >}}

Suppose `$U$` is a subspace of `$V$`. The *quotient map* `$\pi : V \to V/U$` is the linear map defined by
``` katex
\[\pi(v) = v + U\]
```
for each  `$v \in V$`.

{{< /callout >}}

We can write that

``` katex
\[
\pi(v_1) = \pi(v_2) \iff v_1 - v_2 \in U
\]
```

## Quotient Space Is a Vector Space

First define the addition and scalar multiplication operations:

{{< callout type="definition" icon="fas fa-book" title="3.102 definition: *addition and scalar multiplication on* $V/U$" fold="" >}}

Suppose `$U$` is a subspace of `$V$`. Then addition and scalar multiplication are defined on `$V/U$` by
``` katex
\[\begin{align*}
(v + U) + (w + U) &= (v + w) + U \\
\lambda(v + U) &= (\lambda v) + U
\end{align*}\]
```
for all `$v, w \in V$` and `$\lambda \in \mathbf{F}$`.

{{< /callout >}}

`$v+U$` is not the unique way to represent a member in `$V/U$`, because there may exist `$v'\ne v$` that `$u + U = v' + U$`. The operations make sense only when the choice of `$v$` to represent a translate makes no differences.

Specifically, suppose `$v_1, v_2, w_1, w_2 \in V$` such that

``` katex
\[
v_1 + U = v_2 + U \quad\textrm{and}\quad w_1 + U = w_2 + U
\]
```

From the addition definition:

``` katex
\[
\begin{align*}
(v_1+U) + (w_1+U) &= (v_1 + w_1) + U \\
(v_2+U) + (w_2+U) &= (v_2 + w_2) + U
\end{align*}
\]
```

The left side of the two equations indeed are the different representation of the same equation, so we must show that the right side equal: `$(v_1 + w_1)+U=(v2+w2)+U$`.

This applies to scalar multiplication as well:

``` katex
\[
\begin{align*}
\lambda(v_1 + U) &= (\lambda v_1) + U \\
\lambda(v_2 + U) &= (\lambda v_2) + U
\end{align*}
\]
```

We must show that `$(\lambda v_1) + U = (\lambda v_2) + U$`.

## Linear Map from V/(null T) to W

{{< callout type="definition" icon="fas fa-book" title="3.106 notation: $\\widetilde{T}$" fold="" >}}

Suppose `$T \in \mathcal{L}(V, W)$`. Define `$\widetilde{T}: V/(\text{null } T) \to W$` by
``` katex
\[\widetilde{T}(v + \text{null } T) = Tv.\]
```

{{< /callout >}}

Think of merging inputs having the same output. These inputs will be the same input in the quotient space `$V/(\text{null } T)$`.

For any `$v_1, v_2 \in V$` that `$Tv_1 = Tv_2$`, `$v_1 + \mathrm{null}\, T$` and `$v_2 + \mathrm{null}\, T$` are the same value in `$V/(\mathrm{null}\, T)$`. This makes `$\widetilde{T}$` injective. Because `$\mathrm{range}\,\widetilde{T}=\mathrm{range}\, T$`, `$\widetilde{T}$` is also surjective on to `$\mathrm{range}\, T$`.

{{< callout type="definition" icon="fas fa-book" title="3.63 *invertibility* $\\iff$ *injectivity and surjectivity*" fold="" >}}

A linear map is invertible if and only if it is injective and surjective.

{{< /callout >}}

3.63 shows us that `$\widetilde{T}$` is invertible, and according to the definition of isomorphic, `$V/(\mathrm{null}\, T)$` and `$\mathrm{range}\,T$` are isomorphic vector spaces and `$\widetilde{T}$` is their isomorphism.

{{< callout type="definition" icon="fas fa-book" title="definition: *isomorphism, isomorphic*" fold="" >}}

- An *isomorphism* is an invertible linear map.
- Two vector spaces are called isomorphic if there is an isomorphism from one vector space onto the other one.
{{< /callout >}}
