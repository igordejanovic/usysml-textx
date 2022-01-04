"""
This module implements usysml semantics checks.
"""
from textx import TextXSemanticError, get_location


class USysMLErrorScopeNamesMustBeUnique(TextXSemanticError):
    def __init__(self, line=None, col=None, err_type=None, filename=None,
                 context=None):
        super().__init__('Scope names must be unique', line, col, err_type,
                         filename, context)


def check_namespace_unique_name(scope):
    """
    Each scope/namespace names should be unuque.
    See test_01-001.
    """
    names = set()
    for e in scope.elements:
        if hasattr(e, 'name'):
            if e.name in names:
                raise USysMLErrorScopeNamesMustBeUnique(**get_location(e))
            names.add(e.name)
