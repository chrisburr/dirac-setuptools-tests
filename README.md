# Experiments with DIRAC packaging

This repository contains a toy example of how DIRAC and its extensions could be packaged.
It is expected that these solutions will be used whenever DIRAC is installed with DIRACOS2 and these will enable good quality support of alternative installation methods such as `pip` and `conda`.

## Cheatsheet for using this test repository

### Create a local PyPI server for testing

To allow `pip install` commands to be tested it's useful to have a local PyPI server running:

```bash
mamba create --name pypi-server python python-build
conda activate pypi-server
pip install pypiserver
mkdir .packages/
pypi-server -p 8080 $PWD/.packages &
```

### Create an environment in which to run tests

```bash
mamba create --name test python m2crypto python-build
conda activate test
```

### Changing a package's version

Go to the `PACKAGE/src/PACKAGE/__init__.py` file and edit the version number.

### "Uploading" packages to the locally running PyPI server

```bash
./build-and-upload-to-pypi-test.sh
```

### Resetting the local PyPI server and build caches

```bash
./clean-builds-and-pypi.sh
```

### Installing from the local server

```bash
pip install --extra-index-url http://localhost:8080 --use-feature=2020-resolver DIRAC
```

### Bumping all version numbers

We can exploit that fact that all versions currently end in `.0.0` to do a quick version bump:

```bash
rg --files-with-matches '\.0\.0' | xargs -I _ sed -i 's@.0.0@.1.0@g' _
```
