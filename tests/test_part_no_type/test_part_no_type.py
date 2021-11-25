import os
from textx import metamodel_for_language

this_folder = os.path.dirname(__file__)


def test_part_no_type():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(this_folder,
                                            'VehicleExample01a.sysml'))

    assert model.elements[0].name == 'PackageVehicles'
    assert type(model.elements[0]).__name__ == 'Package'

    e = model.elements[0].elements[7]
    assert e.name == 'partnotype1'
    assert e.type is None

    e = model.elements[0].elements[-1].elements[0]
    assert e.name == 'partnotype2'
    assert e.type is None
