import os
from textx import metamodel_for_language
from usysml.utils import get_element_by_name
from usysml.utils import assert_element_classfr, assert_element_type

test_case = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(test_case,
                                            'test_01-006.sysml'))

    assert_element_classfr(model, 'PackageVehicles', 'Package')
    assert_element_classfr(model, 'PackageVehicles.Vehicle', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.Wheel', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.vehicle', 'Part')
    assert_element_classfr(model, 'PackageVehicles.vehicle.Wheel', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.vehicle.w', 'Part')

    assert_element_type(model, 'PackageVehicles.vehicle.w',
                        'PackageVehicles.vehicle.Wheel')
