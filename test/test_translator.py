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

    def test_traslate_start_vowel_a_end_y(self):
        # Assign
        translator = PigLatinTranslator("any")

        # Act
        translation = translator.translate()

        # Assert
        self.assertEqual("anynay", translation)

    def test_traslate_start_vowel_e_end_y(self):
        # Assign
        translator = PigLatinTranslator("enemy")

        # Act
        translation = translator.translate()

        # Assert
        self.assertEqual("enemynay", translation)

    def test_traslate_start_vowel_end_vowel(self):
        # Assign
        translator = PigLatinTranslator("apple")

        # Act
        translation = translator.translate()

        # Assert
        self.assertEqual("appleyay", translation)

    def test_traslate_start_vowel_end_consonant(self):
        # Assign
        translator = PigLatinTranslator("ask")

        # Act
        translation = translator.translate()

        # Assert
        self.assertEqual("askay", translation)

    def test_traslate_start_consonant_h(self):
        # Assign
        translator = PigLatinTranslator("hello")

        # Act
        translation = translator.translate()

        # Assert
        self.assertEqual("ellohay", translation)