# -*- coding: utf-8 -*-

import math
import re

__all__ = ("format",)


class Formatter(object):
    def match(self, numeralfmt, value):
        raise NotImplementedError  # pragma: no cover

    def format(self, numeralfmt, value):
        raise NotImplementedError  # pragma: no cover


class NoneFormatter(Formatter):
    """
    When value is None or format is None
    """

    def match(self, numeralfmt, value):
        return value is None or numeralfmt is None

    def format(self, numeralfmt, value):
        return str(value)


class DurationWithSecondsFormatter(Formatter):
    def match(self, numeralfmt, value):
        return len(numeralfmt.split(":")) == 3

    def format(self, numeralfmt, value):
        hours = int(value / 3600)
        minutes = int((value - hours * 3600) / 60)
        seconds = int(value) % 60
        return "%01d:%02d:%02d" % (hours, minutes, seconds)


class DurationWithoutSecondsFormatter(Formatter):
    def match(self, numeralfmt, value):
        return ":" in numeralfmt

    def format(self, numeralfmt, value):
        hours = int(value / 3600)
        minutes = int((value - hours * 3600) / 60)
        return "%01d:%02d" % (hours, minutes)


class SubstringMatcherMixin(object):
    def match(self, numeralfmt, value):
        return self.pattern in numeralfmt

    def process_suffix(self, numeralfmt, suffix):
        if (" " + self.pattern) in numeralfmt:
            suffix = " " + suffix
        return suffix


class BaseFormatter(Formatter):
    def match(self, numeralfmt, value):
        raise NotImplementedError  # pragma: no cover

    def get_prefix(self, numeralfmt, value):
        prefix = (
            re.match(".*(\\$[ ]?).*0.*", numeralfmt).group(1)
            if re.match(".*(\\$[ ]?).*0.*", numeralfmt)
            else ""
        )
        return prefix, value

    def get_suffix(self, numeralfmt, value):
        suffix = (
            re.match(".*0[^ ]*([ ]?\\$)", numeralfmt).group(1)
            if re.match(".*0[^ ]*([ ]?\\$)", numeralfmt)
            else ""
        )
        return suffix, value

    def get_python_format(self, numeralfmt, value):
        thousand = "," if "," in numeralfmt else ""
        float_or_exp = "e" if "e+0" in numeralfmt else "f"
        if re.match("^0{2,}$", numeralfmt.split(",")[0]):
            fmt = "{:0%s%s}" % (
                len(numeralfmt.split(",")[0])
                + (int(math.log10(abs(value)) / 3) if value != 0 else 0)
                + int(value < 0),
                thousand,
            )
            value = int(value)
        else:
            if "." in numeralfmt:
                decimals = len(
                    list(
                        filter(
                            lambda c: c == "0",
                            numeralfmt.split(".")[1].replace("e+0", ""),
                        )
                    )
                )
            else:
                decimals = 0
            plus = "+" if re.match(".*(^|[^e])\\+.*", numeralfmt) else "-"
            fmt = "{:%s%s.%s%s}" % (plus, thousand, decimals, float_or_exp)
        return fmt, value

    def format(self, numeralfmt, value):
        prefix, value = self.get_prefix(numeralfmt, value)
        suffix, value = self.get_suffix(numeralfmt, value)
        fmt, value = self.get_python_format(numeralfmt, value)
        ret = prefix + fmt.format(value) + suffix
        if numeralfmt.startswith("(") and numeralfmt.endswith(")") and value < 0:
            ret = "(%s)" % ret.replace("-", "")
        if numeralfmt.strip("(").startswith(".") and value > -1 and value < 1:
            ret = ret.replace("0.", ".")
        return ret


class OrderFormatter(SubstringMatcherMixin, BaseFormatter):
    pattern = "o"

    def get_suffix(self, numeralfmt, value):
        if value == 1:
            suffix = "st"
        elif value == 2:
            suffix = "nd"
        elif value == 3:
            suffix = "rd"
        else:
            suffix = "th"
        return self.process_suffix(numeralfmt, suffix), value


class DecimalBytesFormatter(SubstringMatcherMixin, BaseFormatter):
    pattern = "b"

    def get_suffix(self, numeralfmt, value):
        if abs(value) >= 1e12:
            suffix = "TB"
            value /= 1e12
        elif abs(value) >= 1e9:
            suffix = "GB"
            value /= 1e9
        elif abs(value) >= 1e6:
            suffix = "MB"
            value /= 1e6
        elif abs(value) >= 1e3:
            suffix = "KB"
            value /= 1e3
        else:
            suffix = "B"
        return self.process_suffix(numeralfmt, suffix), value


class BinaryBytesFormatter(SubstringMatcherMixin, BaseFormatter):
    pattern = "ib"

    def get_suffix(self, numeralfmt, value):
        if abs(value) >= 1024 ** 4:
            suffix = "TiB"
            value /= 1024 ** 4
        elif abs(value) >= 1024 ** 3:
            suffix = "GiB"
            value /= 1024 ** 3
        elif abs(value) >= 1024 ** 2:
            suffix = "MiB"
            value /= 1024 ** 2
        elif abs(value) >= 1024:
            suffix = "KiB"
            value /= 1024
        else:
            suffix = "B"
        return self.process_suffix(numeralfmt, suffix), value


class PercentageFormatter(SubstringMatcherMixin, BaseFormatter):
    pattern = "%"

    def get_suffix(self, numeralfmt, value):
        suffix = "%"
        return self.process_suffix(numeralfmt, suffix), value

    def format(self, numeralfmt, value):
        return super().format(numeralfmt, 100 * value)


class HumanFormatter(SubstringMatcherMixin, BaseFormatter):
    pattern = "a"

    def get_suffix(self, numeralfmt, value):
        if abs(value) >= 1e12:
            suffix = "t"
            value /= 1e12
        elif abs(value) >= 1e9:
            suffix = "b"
            value /= 1e9
        elif abs(value) >= 1e6:
            suffix = "m"
            value /= 1e6
        elif abs(value) >= 1e3:
            suffix = "k"
            value /= 1e3
        else:
            suffix = ""
        return self.process_suffix(numeralfmt, suffix), value


formatters = [
    NoneFormatter(),
    DurationWithSecondsFormatter(),
    DurationWithoutSecondsFormatter(),
    OrderFormatter(),
    BinaryBytesFormatter(),
    DecimalBytesFormatter(),
    PercentageFormatter(),
    HumanFormatter(),
]

default_formatter = BaseFormatter()


def format(value, numeralfmt):
    for formatter in formatters:
        if formatter.match(numeralfmt, value):
            return formatter.format(numeralfmt, value)
    return default_formatter.format(numeralfmt, value)
