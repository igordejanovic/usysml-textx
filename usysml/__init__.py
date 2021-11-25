import os
from functools import partial
from textx import language, metamodel_from_file
from textx.generators import generator, gen_file, get_output_filename

__version__ = "0.1.0.dev"


@language('usysml', '*.sysml')
def usysml_language():
    "uSysML language"
    current_dir = os.path.dirname(__file__)
    mm = metamodel_from_file(os.path.join(current_dir, 'usysml.tx'))

    # Here if necessary register object processors or scope providers
    # http://textx.github.io/textX/stable/metamodel/#object-processors
    # http://textx.github.io/textX/stable/scoping/

    return mm


@generator('usysml', 'text')
def usysml_generate_text(metamodel, model, output_path, overwrite, debug, **custom_args):
    "Generator for producing textual file of the model structure."

    output_file = get_output_filename(model._tx_filename, output_path, 'txt')
    gen_file(model._tx_filename, output_file,
             partial(generator_callback, model, output_file),
             overwrite,
             success_message='Successfuly generated file "{}"'
             .format(os.path.basename(output_file)))


def generator_callback(model, output_file):
    """
    A generator function that produce output_file from model.
    """

    def elem_fqn(elem):
        if elem is None:
            return 'None'
        names = []
        while hasattr(elem, 'parent'):
            if hasattr(elem, 'name'):
                names.append(elem.name)
            elem = elem.parent
        return 'Root.{}'.format('.'.join(reversed(names)))

    def write_elements(output_file, owner, indent=0):
        for elem in owner.elements:
            write_element(output_file, elem, indent)

    def write_element(output_file, elem, indent):
        output_file.write('{}{} [{}]\n'
                          .format(' ' * indent,
                                  elem_fqn(elem),
                                  elem._tx_fqn.split('.')[-1]))
        indent += 1
        ind_str = '  ' * indent
        if hasattr(elem, 'mult') and elem.mult:
            output_file.write('{}multiplicity={}{}\n'
                              .format(ind_str,
                                      elem.mult.lower_bound,
                                      '-{}'.format(elem.mult.upper_bound)
                                      if elem.mult and elem.mult.upper_bound else ''))
        if hasattr(elem, 'type'):
            output_file.write('{}type={}\n'.format(ind_str, elem_fqn(elem.type)))
        # if hasattr(elem, 'parent'):
        #     output_file.write('{}parent={}\n'.format(ind_str, elem_fqn(elem.parent)))
        if hasattr(elem, 'elements'):
            write_elements(output_file, elem, indent)

    with open(output_file, 'w') as output_file:
        write_elements(output_file, model)
