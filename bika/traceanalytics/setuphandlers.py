""" Bika setup handlers. """

from Products.CMFCore.utils import getToolByName
from bika.lims import logger


class Empty:
    pass


class BikatraceanalyticsGenerator:
    def setupCatalogs(self, portal):
        # an item should belong to only one catalog.
        # that way looking it up means first looking up *the* catalog
        # in which it is indexed, as well as making it cheaper to index.

        def addIndex(cat, *args):
            try:
                cat.addIndex(*args)
            except:
                logger.warning("Could not create index %s in catalog %s" %
                               (args, cat))

        def addColumn(cat, col):
            try:
                cat.addColumn(col)
            except:
                logger.warning("Could not create metadata %s in catalog %s" %
                               (col, cat))

        bsc = getToolByName(portal, 'bika_setup_catalog', None)
        if bsc is None:
            logger.warning('Could not find the setup catalog tool.')
            return

        addIndex(bsc, 'ERP_Keyword', 'FieldIndex')
        addColumn(bsc, 'ERP_Keyword')


def setuptraceanalyticsVarious(context):
    """ Setup Bika site structure """

    if context.readDataFile('bika.traceanalytics.txt') is None:
        return

    portal = context.getSite()

    gen = BikatraceanalyticsGenerator()
    gen.setupCatalogs(portal)

