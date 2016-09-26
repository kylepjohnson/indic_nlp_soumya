"""Test Indic NLP port to CLTK."""

from cltk.corpus.utils.importer import CorpusImporter
import indic_morph

import os
import unittest

class testing_indic_morph(unittest.TestCase):
    def setUp(self):
        """Install the Indic NLP library, which includes Morfessor files
        for morphology.
        """
        cltk_data_dir = '~/cltk_data/sanskrit/model/sanskrit_models_cltk'
        INDIC_RESOURCES_PATH = os.path.expanduser(cltk_data_dir)

        resources_present = os.path.isdir(INDIC_RESOURCES_PATH)
        if not resources_present:
            corpus_importer = CorpusImporter('sanskrit')
            corpus_importer.import_corpus('sanskrit_models_cltk')

    def test_morph_analyze(self):
        input_str = "प्रेमचन्द"
        current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze(self,input_str, 'hi')
        correct = ['प्रेम', 'चन्द']
        self.assertEqual(current,correct)

    def test_morph_analyze_documents(self):
        input_str = "प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर।"
        current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze_document(self, input_str, 'hi')
        correct = ['प्रेम', 'चन्द', 'का', 'जन्म', '३१', 'जुलाई', 'सन्', '१८८०', 'को', 'बनारस', 'शहर', '।']
        self.assertEqual(current, correct)


if __name__  == '__main__':
    unittest.main()