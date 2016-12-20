
##API Usage

This function can be used to break down into morphemes all the words present in the input text, it works by using a third library called morfessor (which will have to be specifically downloaded to run this feature). Input is:




```python
if __name__ == '__main__':
    INDIC_RESOURCES_PATH = os.path.expanduser('~/cltk_data/sanskrit/model/sanskrit_models_cltk')

    resources_present = os.path.isdir(INDIC_RESOURCES_PATH)

    if not resources_present:
        from cltk.corpus.utils.importer import CorpusImporter
        c = CorpusImporter('sanskrit')
        c.import_corpus('sanskrit_models_cltk')

    language='hindi'
    add_marker=False

    language = LANGUAGE_NAME_TO_CODE[language]
    #print (language, type(language))
    analyzer = UnsupervisedMorphAnalyzer(add_marker)
    input_str = "शास्त्रीयभाषा"
```
Output:

```python
/home/soumya/anaconda3/bin/python /home/soumya/indic_nlp_soumya/indic_morph.py
**
*
['शास्त्रीय', 'भाषा']

Process finished with exit code 0

```


