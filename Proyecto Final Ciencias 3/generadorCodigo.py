"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from prueba import get_entity_mm


def main(debug=False):

    this_folder = dirname(__file__)

    entity_mm = get_entity_mm(debug)

    # Build Person model from person.ent file
    person_model = entity_mm.model_from_file(join(this_folder, 'universidad.ent'))

    def is_entity(n):
        """
        Test to prove if some type is an entity
        """
        if n.type in person_model.entities:
            return True
        else:
            return False

    def cSharptype(s):
        """
        Maps type names from PrimitiveType to python.
        """
        return {
                'integer': 'int',
                'string': 'string'
        }.get(s.name, s.name)

    # Create output folder
    srcgen_folder = join(this_folder, 'Codigo Generado en C')
    if not exists(srcgen_folder):
        mkdir(srcgen_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Python type names.

    jinja_env.tests['entity'] = is_entity

    jinja_env.filters['cSharptype'] = cSharptype

    # Load template
    template = jinja_env.get_template('cSharpClass.template')

    for entity in person_model.entities:
        # For each entity generate python file crea los archivos
        #Direccion.py
        #Persona.py
        #Telefono.py
        with open(join(srcgen_folder,"%s.cs" % entity.name.capitalize()), 'w') as f:
            f.write(template.render(entity=entity))


if __name__ == "__main__":
    main()
