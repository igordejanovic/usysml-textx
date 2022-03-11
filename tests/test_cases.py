"""
This set of test will use .sysml and .output files from the
usysml-test-cases project to assert their consistency.

Before run set environment variable
USYSML_TEST_CASE
to the usysml-test-case project folder.

"""
import os
import glob
import pytest
from usysml import generator_text_str
from textx import metamodel_for_language, TextXError

SKIP_TESTS = [
#    'test_02-002',
]


def is_skip(filename):
    for t in SKIP_TESTS:
        if t in filename:
            return True
    return False


sysml_mm = metamodel_for_language('usysml')

USYSML_TEST_CASES = os.getenv('USYSML_TEST_CASES')
if not USYSML_TEST_CASES:
    print('USYSML_TEST_CASES not set. See README file.')
    exit(1)

sysml_files = os.path.join(os.path.realpath(USYSML_TEST_CASES),
                           '**', '*.sysml')
sysml_files_success = sorted([f for f in glob.glob(sysml_files, recursive=True)
                              if 'error' not in f])
sysml_files_error = sorted([f for f in glob.glob(sysml_files, recursive=True)
                            if 'error' in f])


@pytest.mark.parametrize("sysml_file", sysml_files_success)
def test_success(sysml_file, update):
    output_file = os.path.splitext(sysml_file)[0] + '.output'

    if update:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(generator_text_str(
                sysml_mm.model_from_file(sysml_file)))
    else:
        if is_skip(sysml_file):
            pytest.skip('Not implemented yet.')
        with open(output_file, 'r', encoding='utf-8') as f:
            output = generator_text_str(
                sysml_mm.model_from_file(sysml_file))
            assert f.read() == output


@pytest.mark.parametrize("sysml_file", sysml_files_error)
def test_failure(sysml_file, update):
    if update:
        pytest.skip('Not updating error tests cases.')

    if is_skip(sysml_file):
        pytest.skip('Not implemented yet.')

    with pytest.raises(TextXError):
        sysml_mm.model_from_file(sysml_file)
