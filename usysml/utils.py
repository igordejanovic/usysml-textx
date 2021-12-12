from textx import get_children
from textx.scoping.rrel import find


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
