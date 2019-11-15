# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

## Run tests

To run a subset of tests:

```
$ pytest
```

## Deploying

```
$> rm -rf dist/
$> python setup.py sdist
$> python setup.py bdist_wheel
$> twine upload dist/*
