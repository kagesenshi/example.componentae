import grokcore.component as grok
from componentae.interfaces import IContext, ISession, IApplication
from zope.component.interfaces import IFactory
import componentae.api as cae
from zope.component import getUtility, createObject
from zope.interface import implementedBy
from app_lib.interfaces import IPage
from google.appengine.ext import db

class AppAnnotation(db.Model):
    node = db.ReferenceProperty(cae.Node, required=True)
    bodytext = db.TextProperty()

cae.Application.annotation_model = AppAnnotation

class EditApplication(cae.View):
    cae.require('cae.Edit')
    grok.context(IApplication)
    grok.name('edit')
    cae.template('templates/edit_application.pt')

    def update(self):
        if self.request.method == 'POST':
            self.context.title = self.request.get('title')
            self.context.bodytext = self.request.get('bodytext')


class PageAnnotation(db.Model):
    node = db.ReferenceProperty(cae.Node, required=True)
    bodytext = db.TextProperty()

class Page(cae.Context):
    grok.context(cae.Node)
    grok.implements(IPage)
    grok.provides(IPage)
    annotation_model = PageAnnotation

class PageFactory(cae.Factory):
    grok.name('Page')
    iface = IPage

class AddPage(cae.View):
    cae.require('cae.Edit')
    grok.name('++add++page')
    grok.context(IContext)
    cae.template('templates/add_page.pt')

    def update(self):
        if self.request.method == 'POST':
            name = self.request.POST['name']
            if name in self.context.keys():
                return
            node = createObject('Page', 
                name = name
            )
            for k, v in self.request.POST.items():
                setattr(node, k, v)
            self.context[name] = node
            self.redirect(node.absolute_url())
