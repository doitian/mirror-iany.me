---
tags:
- programming
title: Shell
---

## Tips

### How to get the source directory of a Bash script from within the script itself?

[※ source](https://stackoverflow.com/a/246128/667158)

``` shell
#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
```
### How to obtain the first letter in a Bash variable?


[※ source](https://stackoverflow.com/questions/10218474/how-to-obtain-the-first-letter-in-a-bash-variable)

``` shell
word='tiger'
echo "${word::1}"
echo "${word}" | cut -c 1
echo "${word:0:1}"
```

### Printing a sequence of letters or numbers in shell

[※ source](https://www.shell-tips.com/2008/01/14/printing-a-sequence-of-letters-or-numbers/)

Print a sequence of number

``` shell-session
$ seq 1 10
1 2 3 4 5 6 7 8 9 10

$ seq 0 2 10
0 2 4 6 8 10

$ echo {1..10}
1 2 3 4 5 6 7 8 9 10
```

Print a sequence of letters

``` shell-session
$ echo {a..g}
a b c d e f g
```
