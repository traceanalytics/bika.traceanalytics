from bika.lims.browser.analysisrequest.publish import \
    AnalysisRequestPublishView as _AnalysisRequestPublishView
from bika.lims import bikaMessageFactory as _
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import glob, os, sys, traceback

class AnalysisRequestPublishView(_AnalysisRequestPublishView):

    def __call__(self):
        return super(AnalysisRequestPublishView, self).__call__()
