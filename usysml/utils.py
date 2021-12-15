from textx import get_children
from textx.scoping.rrel import find


def assert_element_type(model, elem_fqn, elem_type_fqn):
    """Asserts that the element 'elem_fqn' is of type 'elem_type_fqn'
    """

    e1 = get_element_by_name(model, elem_type_fqn)
    e = get_element_by_name(model, elem_fqn)
    assert e.type is e1


def assert_element_classfr(model, elem_fqn, classfr):
    """Asserts that the parent classifier of element 'elem_fqn' is 'classfr'
    """

    e = get_element_by_name(model, elem_fqn)
    assert type(e).__name__ == classfr


def get_element_by_name(model, name):
    """Returns model element by the provided name. Name can be a simple name or a
    Fully Qualified Name (FQN) separated by a dot.

    """
    if '.' in name:
        # FQN
        return find(model, name, 'elements*')
    else:
        # If simple name is provided search whole model
        elements = get_children(lambda x: hasattr(x, 'name') and x.name == name,
                                root=model)
        if not elements:
            return None
        elif len(elements) > 1:
            raise Exception(f'Multiple elements with name "{name}"')

        return elements[0]


def elem_fqn(elem):
    """
    For the given model element returns its FQN.
    """
    if elem is None:
        return 'None'

    if not hasattr(elem, 'parent'):
        # Top level element is Root
        return 'Root'

    names = []
    while hasattr(elem, 'parent'):
        if hasattr(elem, 'name'):
            names.append(elem.name)
        elem = elem.parent
    return 'Root.{}'.format('.'.join(reversed(names)))
