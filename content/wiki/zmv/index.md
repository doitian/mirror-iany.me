---
tags:
- commandLine
- zsh
title: Zmv
---

Zmv is a zsh utility to rename files in batch.

<!--more-->

```
zmv [ -finqQsvwW ] [ -C | -L | -M | -{p|P} program ] [ -o optstring ]
	srcpat dest
		Move (usually, rename) files matching the pattern srcpat to corresponding files having names of the form given by dest, where srcpat contains parentheses surrounding patterns which will be replaced in turn by $1, $2, ... in dest.
```

§ Enable

```
autoload -U zmv
```

§ Manual

```
man zshcontrib
```

§ Cheatsheet

``` shell
# Rename foo.txt to foo.md
zmv '(*).txt' '$1.md'

# Replace every space by an underscore
zmv -v '(* *)' '${1// /_}'
zmv -v '* *' '${f// /_}'

# Remove digits prefix
zmv -v '[[:digit:]]##(*)' '$1'
```

Zmv uses [Extended Glob](http://zsh.sourceforge.net/Doc/Release/Expansion.html#Glob-Operators) in the pattern.
