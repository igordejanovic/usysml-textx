from textx import get_children


def get_element_by_name(model, name):
    """
    Returns model element by the provided name.
    """
    elements = get_children(lambda x: hasattr(x, 'name') and x.name == name,
                            root=model)
    if not elements:
        return None
    elif len(elements) > 1:
        raise Exception(f'Multiple elements with name "{name}"')

    return elements[0]
