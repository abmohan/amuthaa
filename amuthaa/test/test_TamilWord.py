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
          'letters': [u'ம', u'ர', u'ம்'],
          'syllables': [u'ம', u'ரம்']
          },
         {
          'text': u"மாமரம்",
          'len': 4,
          'letters': [u'மா', u'ம', u'ர', u'ம்'],
          'syllables': [u'மா', u'ம', u'ரம்']
          },
         {
          'text': u"ஈ",
          'len': 1,
          'letters': [u'ஈ'],
          'syllables': [u'ஈ']
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
          'letters': [u'வ்'],
          'syllables': [u'வ்']
          },
         {
          'text': u"அரசியல்",
          'len': 5,
          'letters': [u'அ', u'ர', u'சி', u'ய', u'ல்'],
          'syllables': [u'அ', u'ர', u'சி', u'யல்']
          },
         {
          'text': u"பேனை",
          'len': 2,
          'letters': [u'பே', u'னை'],
          'syllables': [u'பே', u'னை']
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

    def test_split_letters(self):
        """ Tests the static split_letters() function

        Compare each of the dictionaries in the WORDS tuple to ensure that
        the split_letters() function, when applied to the 'text' value,
        produces the 'letters' value (which is also a tuple)
        """

        print """Testing TamilWord.split_letters()""",

        for word in WORDS:

            expected = word['letters']
            received = TamilWord.split_letters(word['text'])

            self.assertEquals(expected, received, """Expected tuple \'%s\',
                but received tuple \'%s\'""" % (expected, received))

        print ".... pass"

    def test_split_syllables(self):
        """ Tests the static split_syllables() function

        Compare each of the dictionaries in the WORDS tuple to ensure that
        the split_syllables() function, when applied to the 'text' value,
        produces the 'syllables' value (which is also a tuple)
        """

        print """Testing TamilWord.split_syllables()""",

        for word in WORDS:

            expected = word['syllables']
            received = TamilWord.split_syllables(word['text'])

            self.assertEquals(expected, received, """Expected tuple \'%s\',
                but received tuple \'%s\'""" % (expected, received))

        print ".... pass"


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