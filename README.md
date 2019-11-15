# Pynumeral

![](https://img.shields.io/badge/python-3.6-brightgreen.svg) ![](https://img.shields.io/badge/python-3.7-brightgreen.svg) ![](https://img.shields.io/badge/code%20style-black-000000.svg) [![Build Status](https://travis-ci.org/optimdata/pynumeral.svg?branch=master)](https://travis-ci.org/optimdata/pynumeral)

`pynumeral` is a python implementation of number formatting using [numeraljs format](http://numeraljs.com/#format). This project was motivated when we had to render numbers backend-side (which is written in python) while keep using formats defined by users. It has been coded regardless of the javascript implementation. It has been tested on a fairly large amount of formats but there are not any guarantees that it covers all the cases. Since unit testing is pretty simple, contributions are more than welcome.

It only provides a simple api `pynumeral.format(value, format)`. 


* License: [MIT license](https://github.com/optimdata/pynumeral/blob/master/LICENSE)
* Source: https://github.com/optimdata/pynumeral
* Issues: https://github.com/optimdata/pynumeral/issues
