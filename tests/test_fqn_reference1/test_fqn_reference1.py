import os
from textx import metamodel_for_language

this_folder = os.path.dirname(__file__)


def test_fqn_references():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(this_folder,
                                            'VehicleExample03c.sysml'))

    w = model.elements[0].elements[2].elements[0]

    # Assert that Wheel referenced by w is from the owning package
    assert w.type is model.elements[0].elements[1]
