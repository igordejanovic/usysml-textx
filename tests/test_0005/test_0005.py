import os
from textx import metamodel_for_language
from usysml.utils import get_element_by_name

this_folder = os.path.dirname(__file__)


def test_usysml():
    mm = metamodel_for_language('usysml')
    model = mm.model_from_file(os.path.join(this_folder,
                                            'test0005.sysml'))

    e = get_element_by_name(model, 'PackageVehicles')
    assert type(model.elements[0]).__name__ == 'Package'

    e = get_element_by_name(model, 'Wheel')
    assert type(e).__name__ == 'PartDef'
