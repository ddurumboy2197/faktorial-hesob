def ekuk(a, b):
    return abs(a - b)

def ekuk_sonlar(a, b):
    kichik = min(a, b)
    katta = max(a, b)
    ekuk = kichik
    while kichik * 2 <= katta:
        kichik *= 2
    while katta % kichik != 0:
        kichik += 1
    return kichik

def ekuk_sonlar_optimal(a, b):
    return 2 ** (a.bit_length() + b.bit_length() - 2)
```

```python
print(ekuk_sonlar(10, 20))
print(ekuk_sonlar_optimal(10, 20))
