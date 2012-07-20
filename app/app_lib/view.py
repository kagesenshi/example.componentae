import componentae.api as cae
import grokcore.component as grok
from componentae.interfaces import IApplication, IContext

class TestView(cae.View):
    grok.name('index')
    grok.context(IApplication)
    cae.template('index.pt')

class MainTemplate(cae.View):
    grok.name('main_template')
    grok.context(IContext)
    cae.template('main_template.pt')
