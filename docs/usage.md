# Usage

`pynumeral` provides one api: `format`. Below you can find many examples. For more informations about format tokens, please read [numeraljs documentation](http://numeraljs.com/#format).

```python

import pynumeral

pynumeral.format(3.141592653589793, "0.00")
# 3.14
```

## Formatting

### Numbers

```python

import pynumeral

pynumeral.format(10000, None)
# "10000"
pynumeral.format(10000, "0,0.0000")
# "10,000.0000"
pynumeral.format(10000.23, "0,0")
# "10,000"
pynumeral.format(10000.23, "+0,0")
# "+10,000"
pynumeral.format(-10000, "0,0.0")
# "-10,000.0"
pynumeral.format(10000.1234, "0.000")
# "10000.123"
pynumeral.format(100.1234, "00000")
# "00100"
pynumeral.format(1000.1234, "000000,0")
# "001,000"
pynumeral.format(10000.1234, "0[.]00000")
# "10000.12340"
pynumeral.format(-10000, "(0,0.0000)")
# "(10,000.0000)"
pynumeral.format(-0.23, ".00")
# "-.23"
pynumeral.format(-0.23, "(.00)")
# "(.23)"
pynumeral.format(0.23, "0.00000")
# "0.23000"
pynumeral.format(1123456789, "0,0e+0")
#"1e+09"
pynumeral.format(12398734.202, "0.00e+0")
#"1.24e+07"
pynumeral.format(0.000123987, "0.000e+0")
#"1.240e-04"

```

### Humanize

```python
import pynumeral

pynumeral.format(1230974, "0.0a")
# "1.2m"
pynumeral.format(1230974000, "0.0a")
# "1.2b"
pynumeral.format(1230974000000, "0.0a")
# "1.2t"
pynumeral.format(1460, "0 a")
# "1 k"
pynumeral.format(-104000, "0a")
# "-104k"
pynumeral.format(1, "0o")
# "1st"
pynumeral.format(2, "0o")
# "2nd"
pynumeral.format(3, "0o")
# "3rd"
pynumeral.format(100, "0o")
# "100th"
```

### Currencies

```python
import pynumeral

pynumeral.format(1000.234, "$0,0.00")
# "$1,000.23"
pynumeral.format(1000.2, "0,0[.]00 $")
# "1,000.20 $"
pynumeral.format(-1000.234, "($0,0)")
# "($1,000)"
pynumeral.format(1230974, "($ 0.00 a)")
# "$ 1.23 m"
```

### Bytes

```python
import pynumeral

pynumeral.format(100, "0b")
# "100B"
pynumeral.format(1024, "0b")
# "1KB"
pynumeral.format(2, "0 ib")
# "2 B"
pynumeral.format(2048, "0 ib")
# "2 KiB"
pynumeral.format(2048000, "0 ib")
# "2 MiB"
pynumeral.format(2048000000, "0 ib")
# "2 GiB"
pynumeral.format(2048000000000, "0 ib")
# "2 TiB"
pynumeral.format(3072, "0.0 b")
# "3.1 KB"
pynumeral.format(3072000, "0.0 b")
# "3.1 MB"
pynumeral.format(3072000000000, "0.0 b")
# "3.1 TB"
pynumeral.format(7884486213, "0.00b")
# "7.88GB"
pynumeral.format(3467479682787, "0.000 ib")
# "3.154 TiB"
```

### Percentage

```python
import pynumeral

pynumeral.format(1, "0%")
# "100%"
pynumeral.format(0.974878234, "0.000%")
# "97.488%"
pynumeral.format(-0.43, "0 %")
# "-43 %"
pynumeral.format(0.43, "(0.000 %)")
# "43.000 %"
```

### Duration

```python
import pynumeral

pynumeral.format(25, "00:00:00")
# "0:00:25"
pynumeral.format(238, "00:00:00")
# "0:03:58"
pynumeral.format(63846, "00:00:00")
# "17:44:06"
pynumeral.format(63846, "HH:MM:SS")
# "17:44:06"
pynumeral.format(63846, "00:00")
# "17:44"
```
