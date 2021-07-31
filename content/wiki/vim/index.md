---
tags:
- software-usage
title: Vim
---

## Tips

⚡ [Making a list of numbers](https://vim.fandom.com/wiki/Making_a_list_of_numbers)

* `:put =range(11,15)`
* <kbd>g CTRL-A</kbd>

⚡ TextExpand in Vim

> Expand when just switching to the insert mode, type CTRL-v first then type the snippet abbreviation.

⚡ Fix Visual Highlight

```
hi Visual ctermfg=255 ctermbg=31 guibg=LightGrey
```

⚡ Remove Duplicated Lines

```
:sort u
```

⚡ Terminal

```
Special in the terminal window:			*t_CTRL-W_.*  *t_CTRL-W_N*
	CTRL-W .	send a CTRL-W to the job in the terminal
	CTRL-W CTRL-\	send a CTRL-\ to the job in the terminal
	CTRL-W N	go to Terminal-Normal mode, see |Terminal-mode|
	CTRL-\ CTRL-N   go to Terminal-Normal mode, see |Terminal-mode|
	CTRL-W " {reg}  paste register {reg}		*t_CTRL-W_quote*
			Also works with the = register to insert the result of
			evaluating an expression.
	CTRL-W CTRL-C	ends the job, see below |t_CTRL-W_CTRL-C|
	CTRL-W gt	go to next tabpage, same as `gt`	*t_CTRL-W_gt*
	CTRL-W gT	go to previous tabpage, same as `gT`	*t_CTRL-W_gT*
```

⚡ Vim, Disable Automatic Newline At End Of File

[※source](http://stackoverflow.com/questions/1050640/vim-disable-automatic-newline-at-end-of-file)

```
set nofixendofline
```

or

```
set bin noeol
```

⚡️ Vim, Load Tags in Location List

```
:ltag
```
