import componentae.api as cae
import grokcore.component as grok
from componentae.interfaces import IApplication, IContext
from zope.component import createObject, getUtilitiesFor
from zope.component.interfaces import IFactory
from zope.component.hooks import getSite

class Index(cae.View):
    grok.name('index')
    grok.context(IContext)
    cae.template('index.pt')


class MainTemplate(cae.View):
    grok.name('main_template')
    grok.context(IContext)
    cae.template('main_template.pt')

class NavigationBar(cae.View):
    grok.name('navigation-bar')
    grok.context(IContext)

    def values(self):
        app = getSite()
        return app.values()

