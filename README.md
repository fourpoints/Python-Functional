# Python-Functional
Collection of functional piping operators

## Examples

```python
import numpy as np

3 | Attr.__ror__ | Apply(print)

A = np.identity(3)

a = A |\
    Map(lambda x: x**2) |\
    Filter(lambda x: x[0] == 0) |\
    Reduce(lambda x, y: x + y, initial=0)

a | Apply(print)

([1, 2, 3], [4, 5, 6]) | Zip() | Map(print) | Eval()
zipped = ([1, 2, 3], [4, 5, 6]) | Zip() | Apply(list)
zipped | Apply(print)

{"a": 1, "b": 2} | Get["a"] | Apply(print)

2 | Apply(lambda x: x**2) | Apply(print)

2 | Chain(lambda x: x**2, print)
```
