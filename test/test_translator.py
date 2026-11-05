from unittest import TestCase

from translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        #Assign
        translator = PigLatinTranslator("hello world")

        #Act
        phrase = translator.get_phrase()

        #Assert
        self.assertEqual("hello world", phrase)

    def test_traslate_empty_phrase(self):
        #Assign
        translator = PigLatinTranslator("")

        #Act
        translation = translator.translate()

        #Assert
        self.assertEqual("nil", translation)