import os
from textx import metamodel_for_language
from usysml.utils import get_element_by_name
from usysml.utils import assert_element_classfr, assert_element_type

test_case = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(test_case,
                                            'test0005.sysml'))

    assert_element_classfr(model, 'PackageVehicles', 'Package')
    assert_element_classfr(model, 'PackageVehicles.Vehicle', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.Wheel', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.WheelAxle', 'PartDef')
    assert_element_classfr(model, 'PackageVehicles.test_vehicle', 'Part')
    assert_element_classfr(model, 'PackageVehicles.vehicle', 'Part')
    assert_element_classfr(model, 'PackageVehicles.vehicle.a', 'Part')
    assert_element_classfr(model, 'PackageVehicles.vehicle.w', 'Part')
    assert_element_classfr(model, 'PackageVehicles.vehicle.w.LugBolt', 'PartDef')
    assert_element_classfr(model, 'SupportComponents', 'Package')
    assert_element_classfr(model, 'SupportComponents.parking_space', 'Part')
    assert_element_classfr(model, 'SupportComponents.vehicle_shed', 'Part')
    assert_element_classfr(model, 'SupportComponents.repair_shop', 'Part')
    assert_element_classfr(model, 'SupportComponents.repair_shop.VehicleLift',
                        'PartDef')

    assert_element_type(model, 'PackageVehicles.test_vehicle',
                        'PackageVehicles.Vehicle')
    assert_element_type(model, 'PackageVehicles.vehicle',
                        'PackageVehicles.Vehicle')
    assert_element_type(model, 'PackageVehicles.vehicle.a',
                        'PackageVehicles.WheelAxle')
    assert_element_type(model, 'PackageVehicles.vehicle.w',
                        'PackageVehicles.Wheel')
    assert_element_type(model, 'SupportComponents.parking_space', 'None')
    assert_element_type(model, 'SupportComponents.vehicle_shed', 'None')
    assert_element_type(model, 'SupportComponents.repair_shop', 'None')
