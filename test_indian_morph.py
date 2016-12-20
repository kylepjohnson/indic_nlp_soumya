"""Test Indic NLP port to CLTK."""

from cltk.corpus.utils.importer import CorpusImporter
import indic_morph
import os
import unittest

INDIC_RESOURCES_PATH =''

class testing_indic_morph(unittest.TestCase):
    def setUp(self):
        """Install the Indic NLP library, which includes Morfessor files
        for morphology.
        """
        INDIC_RESOURCES_PATH = os.path.expanduser('~/cltk_data/sanskrit/model/sanskrit_models_cltk')
        resources_present = os.path.isdir(INDIC_RESOURCES_PATH)

        if not resources_present:
            from cltk.corpus.utils.importer import CorpusImporter
            c = CorpusImporter('sanskrit')
            c.import_corpus('sanskrit_models_cltk')

    def test_indian_tokenize(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीय भाषा!"
        current = analyzer.indian_punctuation_tokenize_regex(input_str)
        correct = ['शास्त्रीय', 'भाषा', '!']
        self.assertEqual(current,correct)

    def test_script_check_re(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीय"
        current = analyzer._script_check_re(input_str, 'hi')
        correct = "शास्त्रीय"
        self.assertEqual(current.string, correct)

    def test_contains_number(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीय"
        current = analyzer._contains_number(input_str, 'hi')
        self. assertFalse(current)

    def test_morphanalysis_needed(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीय"
        current = analyzer._morphanalysis_needed(input_str, 'hi')
        self.assertTrue(current)

    def test_morfessor_model(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीयभाषा"
        current = analyzer._morfessor_model(input_str, 'hi')
        correct = 21.595908967854903
        self.assertEqual(current[1], correct)

    def test_morph_analyze(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str =  "शास्त्रीयभाषा"
        current = analyzer.morph_analyze(input_str, 'hi')
        correct = ['शास्त्रीय', 'भाषा']
        self.assertEqual(current,correct)

    def test_morph_analyze_document(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str = "शास्त्रीयभाषा"
        current = analyzer.morph_analyze_document(input_str, 'hi')
        correct = ['शास्त्रीय', 'भाषा']
        self.assertEqual(current, correct)


if __name__  == '__main__':

    unittest.main()