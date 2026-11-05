from unittest import TestCase


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        #Assign
        translator = PigLatinTranslator("hello world")

        #Act
        phrase = translator.get_phrase()

        #Assert
        self.assertEqual("hello world", phrase)