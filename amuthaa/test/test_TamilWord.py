# -*- coding: utf-8 -*-
#!/usr/bin/python


import unittest

# import TamilLetter and TamilWord classes
from amuthaa.TamilLetter import TamilLetter
from amuthaa.TamilWord import TamilWord

WORDS = (
         {
          'text': u"மரம்",
          'len': 3,
          'letters': (u'ம', u'ர', u'ம்'),
          'syllables': (u'ம', u'ரம்')
          },
         {
          'text': u"மாமரம்",
          'len': 4,
          'letters': (u'மா', u'ம', u'ரம்'),
          'syllables': (u'மா', u'ம', u'ரம்')
          },
         {
          'text': u"ஈ",
          'len': 1,
          'letters': (u'ஈ'),
          'syllables': (u'ஈ')
          },
         {
          'text': u"கை",
          'len': 1,
          'letters': (u"கை"),
          'syllables': (u"கை")
          },
         {
          'text': u"",
          'len': 1,
          'letters': (u'வ்'),
          'syllables': (u'வ்')
          },
         {
          'text': u"அரசியல்",
          'len': 5,
          'letters': (u'அ', u'ர', u'சி', u'ய', u'ல்'),
          'syllables': (u'அ', u'ர', u'சி', u'யல்')
          },
         {
          'text': u"பேனை",
          'len': 2,
          'letters': (u'பே', u'னை'),
          'syllables': (u'பே', u'னை')
          }
         )


class TamilWordTest(unittest.TestCase):
    """ A test class for the TamilWord module """

    def setUp(self):
        #TODO: add setup
        pass

    def tearDown(self):
        #TODO: Add tear-down
        pass

    def testSomething(self):
        """docstring"""

        #TODO: implement this


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TamilWordTest))
    return suite


def main():
    runner = unittest.TextTestResult()
    test_suite = suite()
    runner.run(test_suite)


if __name__ == '__main__':
    main()