from bika.traceanalytics.testing import BIKA_TRACEANALYTICS_TESTING
from plone.testing import layered

import robotsuite
import unittest


ROBOT_TESTS = [
    'test_traceanalytics.robot',
]


def test_suite():
    suite = unittest.TestSuite()
    for RT in ROBOT_TESTS:
        suite.addTests([
            layered(robotsuite.RobotTestSuite(RT), layer=BIKA_TRACEANALYTICS_TESTING),
        ])
    return suite
