import os
import shutil
import ConfigParser
import StringIO
from subprocess import Popen, call, STDOUT, PIPE

from paste.util.template import paste_script_template_renderer
from paste.script.templates import Template, var

def sh(cmd):
    return Popen(cmd,shell=True,stdout=PIPE,stderr=PIPE).communicate()[0]

def get_git_user():
    # @@ also can just do sh('git config --get user.name')
    # os.path.expanduser(path)
    path = '/Users/preston/.gitconfig'
    fixed_string = '\n'.join([x.lstrip() for x in open(path)])
    stringobj = StringIO.StringIO(fixed_string)
    config = ConfigParser.SafeConfigParser()
    config.readfp(stringobj)
    return dict(config.items('user'))['name']

class DjangoAppTemplate(Template):
    _template_dir = 'templates/app_package'
    summary = 'template for a distributable django app'
    vars = [
        var('version', 'Version (like 0.1)', default='0.1'),
        var('description', 'One-line description of the package'),
        var('long_description', 'Multi-line description (in reST)'),
        var('keywords', 'Space-separated keywords/tags'),
        var('author', 'Author name', default=get_git_user()),
        var('author_email', 'Author email'),
        var('url', 'URL of homepage'),
        var('license_name', 'License name', default="BSD"),
        # var('zip_safe', 'True/False: if the package can be distributed as a .zip file',
            # default=False),
    ]

    template_renderer = staticmethod(paste_script_template_renderer)

    use_cheetah = False
    required_templates = []

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoAppTemplate, self).check_vars(vars, command)

