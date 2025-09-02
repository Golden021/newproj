
from .basic import BASIC_TEMPLATE
from .pygame_template import PYGAME_TEMPLATE

TEMPLATES = {
    "basic": BASIC_TEMPLATE,
    "pygame": PYGAME_TEMPLATE,
}

def get_template(name):
    return TEMPLATES.get(name)

def list_templates():
    return list(TEMPLATES.keys())
