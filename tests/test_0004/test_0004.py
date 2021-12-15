import os
from textx import metamodel_for_language
from usysml.utils import get_element_by_name
from usysml.utils import assert_element_name, assert_element_type

test_case = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(test_case,
                                            'test0004.sysml'))

    assert_element_name(model, 'PackageVehicles', 'Package')
    assert_element_name(model, 'PackageVehicles.Vehicle', 'PartDef')
    assert_element_name(model, 'PackageVehicles.Wheel', 'PartDef')
    assert_element_name(model, 'PackageVehicles.vehicle', 'Part')
    assert_element_name(model, 'PackageVehicles.vehicle.c', 'Part')
    assert_element_name(model, 'PackageVehicles.vehicle.w', 'Part')

    assert_element_type(model, 'PackageVehicles.vehicle.w',
                        'PackageVehicles.Wheel')
    assert_element_type(model, 'PackageVehicles.vehicle.c',
                        'None')
