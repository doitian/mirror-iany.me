---
tags:
- macOS
title: macOS Time Machine
---

⚡ Test whether a path is excluded

```
tmutil isexcluded .cache
```

⚡ Add a path to the exclusion list

```
sudo tmutil addexclusion -p "$(pwd)/.cache"
```
