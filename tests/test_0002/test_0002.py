import os
from textx import metamodel_for_language

this_folder = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(this_folder,
                                            'test0002.sysml'))

    assert model.elements[0].name == 'PackageVehicles'
    assert type(model.elements[0]).__name__ == 'Package'

    e = model.elements[0].elements[1]
    assert e.name == 'Wheel'
    assert type(e).__name__ == 'PartDef'
