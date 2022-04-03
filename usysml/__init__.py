import os
from functools import partial
from textx import language, metamodel_from_file
from textx.generators import generator, gen_file, get_output_filename
from usysml.utils import elem_fqn
from .semantics import check_namespace_unique_name

__version__ = "0.1.0.dev"


@language('usysml', '*.sysml')
def usysml_language():
    "uSysML language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'usysml.tx'))

    obj_processors = {
        'uSysML': check_namespace_unique_name,
        'Package': check_namespace_unique_name,
        'Part': check_namespace_unique_name,
        'PartDef': check_namespace_unique_name,
        'AttributeDef': check_namespace_unique_name,
    }
    mm.register_obj_processors(obj_processors)

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm


@generator('usysml', 'text')
def usysml_generate_text(metamodel, model, output_path, overwrite, debug, **custom_args):
    "Generator for producing textual file of the model structure."

    output_file = get_output_filename(model._tx_filename, output_path, 'txt')
    gen_file(model._tx_filename, output_file,
             partial(text_generator_callback, model, output_file),
             overwrite,
             success_message='Successfuly generated file "{}"'
             .format(os.path.basename(output_file)))


def text_generator_callback(model, output_file):
    """
    A generator function that produce output_file from model.
    """

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(generator_text_str(model))


def generator_text_str(model):
    output = []

    def write_elements(owner, indent=0):
        for elem in owner.elements:
            write_element(elem, indent)

    def write_element(elem, indent):
        output.append('{}{} [{}]'
                      .format(' ' * indent,
                              elem_fqn(elem),
                              elem._tx_fqn.split('.')[-1]))
        indent += 1
        ind_str = '  ' * indent
        if hasattr(elem, 'mult') and elem.mult:
            output.append('{}multiplicity={}{}'
                          .format(ind_str,
                                  elem.mult.lower_bound,
                                  '-{}'.format(elem.mult.upper_bound)
                                  if elem.mult and elem.mult.upper_bound else ''))
        if hasattr(elem, 'type'):
            output.append('{}typed by={}'.format(ind_str, elem_fqn(elem.type)))
        if hasattr(elem, 'elements'):
            write_elements(elem, indent)

    write_elements(model)
    output.append('')
    return '\n'.join(output)


@generator('usysml', 'dot')
def usysml_generate_dot(metamodel, model, output_path, overwrite, debug, **custom_args):
    "Generator for producing graphical dot file of the model structure."

    output_file = get_output_filename(model._tx_filename, output_path, 'dot')
    gen_file(model._tx_filename, output_file,
             partial(dot_generator_callback, model, output_file),
             overwrite,
             success_message='Successfuly generated file "{}"'
             .format(os.path.basename(output_file)))


def dot_generator_callback(model, output_file):
    """
    Generates dot visualizing the structure of the given model.
    """
    ranks = {}
    with open(output_file, 'w', encoding='utf-8') as output_file:
        def write_elements(owner):
            for elem in owner.elements:
                write_element(elem_fqn_dot(owner), elem)

        def write_element(owner, elem):
            fqn = elem_fqn_dot(elem)
            rank = elem_rank(elem)

            mult = ""
            if hasattr(elem, 'mult') and elem.mult:
                mult = "{}{}".format(elem.mult.lower_bound,
                                    '..{}'.format(elem.mult.upper_bound)
                                    if elem.mult and elem.mult.upper_bound else '')
            output_file.write('{} [label="{}: {}"]\n'.format(fqn, elem.name,
                                                             elem._tx_fqn.split('.')[-1]))
            output_file.write('{} -> {} [{}]\n'.format(
                owner, fqn, ', {}'.format(mult) if mult else ''))
            if hasattr(elem, 'type'):
                output_file.write('{} -> {} [style=dashed, headlabel="type"]\n'
                                  .format(fqn, elem_fqn_dot(elem.type)))

            if hasattr(elem, 'elements'):
                write_elements(elem)

            ranks.setdefault(rank, set()).add(elem)

        output_file.write(DOT_HEADER)
        write_elements(model)
        for rank in ranks.values():
            output_file.write(
                '{{rank=same; {}}}\n'
                .format(', '.join([elem_fqn_dot(e) for e in rank])))

        output_file.write('\n}\n')


def elem_fqn_dot(elem):
    return elem_fqn(elem).replace('.', '__')


def elem_rank(elem):
    rank = 0
    while hasattr(elem, 'parent'):
        elem = elem.parent
        rank += 1
    return rank


DOT_HEADER = r'''
digraph uSysML {
    fontname = "Bitstream Vera Sans"
    fontsize = 8
    node[
        shape=box
    ]
    nodesep = 0.7
    edge[dir=black,arrowtail=empty]

'''
