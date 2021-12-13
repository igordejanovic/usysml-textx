import os
from textx import metamodel_for_language
from usysml.utils import get_element_by_name

this_folder = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(this_folder,
                                            'test0001.sysml'))

    e = get_element_by_name(model, 'PackageVehicles')
    assert type(e).__name__ == 'Package'

    e = get_element_by_name(model, 'PackageVehicles.Vehicle')
    assert type(e).__name__ == 'PartDef'

    e1 = get_element_by_name(model, 'PackageVehicles.Wheel')
    assert type(e1).__name__ == 'PartDef'

    e = get_element_by_name(model, 'PackageVehicles.vehicle')
    assert type(e).__name__ == 'Part'

    e = get_element_by_name(model, 'PackageVehicles.vehicle.w')
    assert type(e).__name__ == 'Part'
    assert e.type is e1
