from zope import schema
from zope.interface import Interface


class ILayer(Interface):
    pass


class ICleanPrintSettings(Interface):
    script_url = schema.TextLine(
                    title=u"Script URL",
                    required=True,
                    description=
                         u'Visit <a href="http://www.formatdynamics.com/diyhub/" '
                         u'target="_blank">www.formatdynamics.com/diypub</a> '
                         u'and Generate CleanPrint Tag. Copy the <em>src</em> '
                         u'parameter value from the <em>&lt;script&gt;</em> '
                         u'tag and paste it here.')
