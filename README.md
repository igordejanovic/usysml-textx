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
        
This package also registers a generator that can generate a text file with model structure. To list generator do:

        textx list-generators
        
To run the generator:

        textx generate VehicleExample03b.sysml --target text --overwrite

A file with `.txt` extension will be produced with the model structure.
        

## Running tests

Tests can be found in `tests` folder. pytest is used. These tests should
demonstrate language features and corner cases. You can run tests from the tests
folder by:

        py.test

# Credits

Initial project layout generated with `textx startproject`.
