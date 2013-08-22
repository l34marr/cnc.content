from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder

from plone.app.textfield import RichText

from plone.namedfile.field import NamedFile
from plone.formwidget.multifile import MultiFileFieldWidget

from cnc.content import MessageFactory as _

# Interface class; used to define content-type schema.

class ITestimony(form.Schema):
    """
    ChiNan Testimony Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/jury.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/testimony.xml")

    title = schema.TextLine(
        title=_(u"Title"),
    )

    testimony = schema.TextLine(
        title=_(u"Testimony"),
        required=False,
    )

    date = schema.TextLine(
        title=_(u"Date"),
        required=False,
    )

    text = RichText(
        title=_(u"Body Text"),
        required=False,
    )

    form.widget(files=MultiFileFieldWidget)
    files = schema.List(
        title=_(u"Attached Files"),
        value_type=NamedFile()
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Testimony(dexterity.Item):
    grok.implements(ITestimony)
    
    # Add your class methods and properties here


# View class
# The view will automatically use a similarly named template in
# jury_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    grok.context(ITestimony)
    grok.require('zope2.View')
    grok.name('view')

