# Permutation Function

Author: Michael Trossbach

Contact: mptrossbach@gmail.com

## Overview

Custom Python function that permutes a sequence.

My motivation here was curiosity. I was trying to improve my understanding of recursion.

## Usage

```python
from permute import permute

seq = [1, 2, 3]
print(list(permute(seq)))
```
```python
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```
