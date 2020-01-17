# https://protips.readthedocs.io/link-roles.html
from docutils import nodes


def setup(app):
    app.add_role('github', autolink('https://github.com/%s'))
    app.add_role('module', autolink('https://github.com/ap--/python-seabreeze/tree/master/src/%s'))
    app.add_role('tree', autolink('https://github.com/ap--/python-seabreeze/tree/master/%s'))


def autolink(pattern):
    def role(name, rawtext, text, lineno, inliner, options={}, content=[]):
        url = pattern % (text,)
        node = nodes.reference(rawtext, text, refuri=url, **options)
        return [node], []
    return role