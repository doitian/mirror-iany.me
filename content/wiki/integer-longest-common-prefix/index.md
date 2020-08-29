---
tags:
- algorithm
title: Integer Longest Common Prefix
---

```
lcp(m, n) = w - 1 - msb(m xor n)
```

where w is the number of bits in a word, and `msb` is [♯ Most-Significant Bit]({{< relref path="/wiki/most-significant-bit.md" lang="en" >}}).
