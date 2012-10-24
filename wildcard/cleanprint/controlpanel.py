from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.statusmessages.interfaces import IStatusMessage
from wildcard.cleanprint import WildcardCleanPrintMessageFactory as _
from wildcard.cleanprint.interfaces import ICleanPrintSettings
from z3c.form.button import buttonAndHandler
from zope.component import getUtility


class CleanPrintSettingsEditForm(controlpanel.RegistryEditForm):
    schema = ICleanPrintSettings
    label = u'Clean Print Settings'

    @buttonAndHandler(_('Save'))
    def handle_save(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        # get old script id
        registry = getUtility(IRegistry)
        registrykey = "wildcard.cleanprint.interfaces.ICleanPrintSettings" \
                      ".script_url"
        oldscript = None
        if registrykey in registry.records:
            oldscript = registry.records[registrykey].value

        # apply changes
        self.applyChanges(data)

        # add new script
        jsreg = getToolByName(self, 'portal_javascripts')
        if data['script_url'] is not None \
                and data['script_url'].strip() != '' \
                and jsreg.getResource(data['script_url']) is None:
            jsreg.registerScript(id=data['script_url'])

        # remove old script if it does not match the currently saved script
        if data['script_url'] != oldscript:
            jsreg.unregisterResource(oldscript)

        # update the status
        IStatusMessage(self.request).addStatusMessage(
            _(u"Changes saved."),
            "info")
        self.request.response.redirect(self.request.getURL())

    @buttonAndHandler(_('Cancel'))
    def handle_cancel(self, action):
        IStatusMessage(self.request).addStatusMessage(
            _(u"Changes canceled."),
            "info")
        self.request.response.redirect("%s/%s" % (
            self.context.absolute_url(),
            self.control_panel_view))


class CleanPrintSettingsConfiglet(controlpanel.ControlPanelFormWrapper):
    form = CleanPrintSettingsEditForm
