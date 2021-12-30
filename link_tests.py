"""link_tests.py

Links test *sysml fles from the folder from USYSML_TEST_CASES/tests
to ./tests. Requires that the environment variable 'USYSML_TEST_CASES'
is set.
"""

import os

# 'USYSML_TEST_CASES' env variable must be set
USYSML_TEST_CASES_PATH = os.getenv('USYSML_TEST_CASES')

if USYSML_TEST_CASES_PATH is None:
    raise RuntimeError("'USYSML_TEST_CASES' variable not set")

# define locations
USYSML_TEST_CASES = os.path.join(USYSML_TEST_CASES_PATH, "test_cases")
TEXTX_TEST_CASES = "./tests"

# get the list of 'textx' test cases
textx_test_cases = os.listdir(TEXTX_TEST_CASES)

# loop over 'textx' test cases
for textx_test_case in textx_test_cases:

    textx_path = os.path.join(TEXTX_TEST_CASES, textx_test_case)
    usysml_path = os.path.join(USYSML_TEST_CASES, textx_test_case)

    #
    # check if everything is in place in 'usysml-test-cases'
    #

    # 1. the corresponding usysml-test-cases folder must exist
    if not os.path.isdir(usysml_path):
        raise RuntimeError("usysml-test-cases doesn't have '{:s}'"
                           .format(usysml_path))

    # 2. the sysml file must exist in the usysml-test-cases folder
    sysml_file_path = os.path.join(usysml_path, textx_test_case + ".sysml")
    if not os.path.isfile(sysml_file_path):
        raise RuntimeError("sysml file doesn't exist: '{:s}'"
                           .format(sysml_file_path))

    #
    # create symlinks from 'usysml-test-cases' to 'usysml-textx' test cases
    #

    # if the 'textx' *.sysml file exist, remove it
    textx_file_path = os.path.join(textx_path, textx_test_case + ".sysml")
    if os.path.isfile(textx_file_path):
        print(" [ removing {:s} ]".format(textx_file_path))
        os.remove(textx_file_path)

    # create symbolic link
    print(" -> Creating symlink for '{:s}'".format(textx_test_case))
    os.symlink(sysml_file_path, textx_file_path)

print("\n All done.\n")
