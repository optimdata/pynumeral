#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pynumeral` package."""


import pynumeral


def test_all():
    assert pynumeral.format(10000, None) == "10000"
    assert pynumeral.format(10000, "0,0.0000") == "10,000.0000"
    assert pynumeral.format(10000.23, "0,0") == "10,000"
    assert pynumeral.format(10000.23, "+0,0") == "+10,000"
    assert pynumeral.format(-10000, "0,0.0") == "-10,000.0"
    assert pynumeral.format(10000.1234, "0.000") == "10000.123"
    assert pynumeral.format(100.1234, "00000") == "00100"
    assert pynumeral.format(1000.1234, "000000,0") == "001,000"
    assert pynumeral.format(10000.1234, "0[.]00000") == "10000.12340"
    assert pynumeral.format(-10000, "(0,0.0000)") == "(10,000.0000)"
    assert pynumeral.format(-0.23, ".00") == "-.23"
    assert pynumeral.format(-0.23, "(.00)") == "(.23)"
    assert pynumeral.format(0.23, "0.00000") == "0.23000"
    assert pynumeral.format(1230974, "0.0a") == "1.2m"
    assert pynumeral.format(1230974000, "0.0a") == "1.2b"
    assert pynumeral.format(1230974000000, "0.0a") == "1.2t"
    assert pynumeral.format(1460, "0 a") == "1 k"
    assert pynumeral.format(-104000, "0a") == "-104k"
    assert pynumeral.format(1, "0o") == "1st"
    assert pynumeral.format(2, "0o") == "2nd"
    assert pynumeral.format(3, "0o") == "3rd"
    assert pynumeral.format(100, "0o") == "100th"
    assert pynumeral.format(1000.234, "$0,0.00") == "$1,000.23"
    assert pynumeral.format(1000.2, "0,0[.]00 $") == "1,000.20 $"
    assert pynumeral.format(-1000.234, "($0,0)") == "($1,000)"
    assert pynumeral.format(1230974, "($ 0.00 a)") == "$ 1.23 m"
    assert pynumeral.format(100, "0b") == "100B"
    assert pynumeral.format(1024, "0b") == "1KB"
    assert pynumeral.format(2, "0 ib") == "2 B"
    assert pynumeral.format(2048, "0 ib") == "2 KiB"
    assert pynumeral.format(2048000, "0 ib") == "2 MiB"
    assert pynumeral.format(2048000000, "0 ib") == "2 GiB"
    assert pynumeral.format(2048000000000, "0 ib") == "2 TiB"
    assert pynumeral.format(3072, "0.0 b") == "3.1 KB"
    assert pynumeral.format(3072000, "0.0 b") == "3.1 MB"
    assert pynumeral.format(3072000000000, "0.0 b") == "3.1 TB"
    assert pynumeral.format(7884486213, "0.00b") == "7.88GB"
    assert pynumeral.format(3467479682787, "0.000 ib") == "3.154 TiB"
    assert pynumeral.format(1, "0%") == "100%"
    assert pynumeral.format(0.974878234, "0.000%") == "97.488%"
    assert pynumeral.format(-0.43, "0 %") == "-43 %"
    assert pynumeral.format(0.43, "(0.000 %)") == "43.000 %"
    assert pynumeral.format(25, "00:00:00") == "0:00:25"
    assert pynumeral.format(238, "00:00:00") == "0:03:58"
    assert pynumeral.format(63846, "00:00:00") == "17:44:06"
    assert pynumeral.format(63846, "HH:MM:SS") == "17:44:06"
    assert pynumeral.format(63846, "00:00") == "17:44"
    assert pynumeral.format(1123456789, "0,0e+0") == "1e+09"
    assert pynumeral.format(12398734.202, "0.00e+0") == "1.24e+07"
    assert pynumeral.format(0.000123987, "0.000e+0") == "1.240e-04"
    assert pynumeral.format(1, "0 a") == "1 "
    assert pynumeral.format(-1, "00") == "-01"
