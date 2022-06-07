from py4web import action, Field, HTTP, URL
from py4web.utils.form import Form
from yatl.helpers import A

import os
import yaml

with open(os.path.join(os.path.dirname(__file__), 'pages.yaml')) as stream:
    pages = yaml.load(stream, Loader=yaml.Loader)

@action('page')
@action('page/<name>')
@action.uses('page.html')
def page(name='index'):
    if not name in pages:
        raise HTTP(404)
    return pages[name]

@action('component1')
def comp1():
    return 'hello world'

@action('component2')
def comp2():
    return A('just a link',_href=URL('page/other')).xml()

@action('component3', method=['GET','POST'])
def comp3():
    return Form([Field('name')]).xml()
