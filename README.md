# usysml-textx

A minimal implementation of SysML in Python/textX.

## Installation

To install for development:

1. Create Python virtual environment:

        python -m venv venv

2. Install this package in the environment:

        source venv/bin/activate
        ./install-dev.sh

3. For each terminal session activate virtual env. Note: syntax is different for
   Windows.

        source venv/bin/activate

`usysml` language is registered with textX. You can list all registered language
with the following command:

        textx list-languages

This package also registers generators that can generate a text file or graphical visualization with model structure. To list generators do:

        textx list-generators

To run text generator:

        textx generate VehicleExample03b.sysml --target text --overwrite

A file with `.txt` extension will be produced with the model structure.

To run graphical visualization generator:

        textx generate VehicleExample03b.sysml --target dot --overwrite

A file with `.dot` extension will be produced with the model structure. You can
visualize this file using [GraphViz](https://www.graphviz.org/) software package
or any `dot` reader (e.g. [xdot](https://github.com/jrfonseca/xdot.py)).

To convert `dot` file to PNG using GraphViz dot tool run:

        dot -Tpng -O test0001.dot

A file with `.dot.png` extension will be produced.


## Running tests

Tests can be found in `tests` folder. pytest is used. These tests should
demonstrate language features and corner cases. You can run tests from the tests
folder by:

        py.test
        
## Running tests on usysml-test-cases inputs

This project provides tests for `.sysml` files from `usysml-test-cases` projects.

To run set environment variable `USYSML_TEST_CASES` to the folder of the `usysml-test-cases` before running tests.


# Credits

Initial project layout generated with `textx startproject`.
