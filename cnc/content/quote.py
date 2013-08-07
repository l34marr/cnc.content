from five import grok
from plone.directives import dexterity, form

from zope import schema

from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

from cnc.content import MessageFactory as _

testaments = SimpleVocabulary([
    SimpleTerm(value=u'new', title=_(u'New Testament')),
    SimpleTerm(value=u'old', title=_(u'Old Testament'))
])

# Interface class; used to define content-type schema.

class IQuote(form.Schema):
    """
    ChiNan Quote Type
    """
    
    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/jury.xml to define the content type
    # and add directives here as necessary.
    
    #form.model("models/quote.xml")

    title = schema.Text(
        title=_(u"Quotation"),
    )

    description = schema.TextLine(
        title=_(u"Citation"),
        required=False,
    )

    testament = schema.Choice(
        title=_(u"Testament"),
        vocabulary=testaments,
        required=False,
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Quote(dexterity.Item):
    grok.implements(IQuote)
    
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
    grok.context(IQuote)
    grok.require('zope2.View')
    grok.name('view')

