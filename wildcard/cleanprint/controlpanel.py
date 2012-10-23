from plone.app.registry.browser import controlpanel
from wildcard.cleanprint.interfaces import ICleanPrintSettings


class CleanPrintSettingsEditForm(controlpanel.RegistryEditForm):
    schema = ICleanPrintSettings
    label = u'Clean Print Settings'


class CleanPrintSettingsConfiglet(controlpanel.ControlPanelFormWrapper):
    form = CleanPrintSettingsEditForm
