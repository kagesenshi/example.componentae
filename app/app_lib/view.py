from componentae.view import View
import grokcore.component as grok
from componentae.interfaces import IApplication, IContext

class TestView(View):
    grok.name('index')
    grok.context(IApplication)
    template = 'index.pt'

class MainTemplate(View):
    grok.name('main_template')
    grok.context(IContext)
    template = 'main_template.pt'
