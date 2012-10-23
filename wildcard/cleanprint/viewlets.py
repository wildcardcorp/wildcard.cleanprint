from Acquisition import aq_inner
from five import grok
from plone.registry.interfaces import IRegistry
from zope.interface import Interface
from zope.component import getMultiAdapter
from zope.component import getUtility

from plone.app.layout.viewlets.interfaces import IHtmlHead


grok.context(Interface)
grok.templatedir('templates')
class CleanPrintJavascript(grok.Viewlet):
    grok.viewletmanager(IHtmlHead)
    grok.template('viewlet')

    def cleanprinturl(self):
        registry = getUtility(IRegistry)
        registrykey = "wildcard.cleanprint.interfaces.ICleanPrintSettings" \
                      ".script_url"
        registryval = None
        if registrykey in registry.records:
            registryval = registry.records[registrykey].value
        return registryval
