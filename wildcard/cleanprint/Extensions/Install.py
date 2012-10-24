from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility


def install(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
                'profile-wildcard.cleanprint:default')

    return "Ran all import steps"


def uninstall(portal):
    # get rid of the portal_javascripts resource
    registry = getUtility(IRegistry)
    registrykey = "wildcard.cleanprint.interfaces.ICleanPrintSettings" \
                  ".script_url"
    oldscript = None
    if registrykey in registry.records:
        oldscript = registry.records[registrykey].value

    if oldscript is not None:
        jsreg = getToolByName(portal, 'portal_javascripts')
        jsreg.unregisterResource(oldscript)

    # do normal uninstall procedure
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
                'profile-wildcard.cleanprint:uninstall')

    return "Ran all uninstall steps"
