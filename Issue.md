
##Issue

Problem still persists in test functions, but I have narrowed down it's scope. 
It's because of a function called _morfessor_model, whose aim is to tokenize and return the viterbi segment of the phrase. While this function works perfectly from inside the indic_morph.py file, it throws an error when the language extension is given from the test function test_indian_morph.py. 


```python
    def _morfessor_model(self, word, lang):
        print ("**")
        io = morfessor.MorfessorIO()
        morfessor_model=io.read_any_model(INDIC_RESOURCES_PATH+'/morph/morfessor/{}.model'.format(lang))
        print ("*")
        return morfessor_model.viterbi_segment(word)

```

When I test it, it returns this error:


```python
    def test_morph_analyze(self):
        analyzer = indic_morph.UnsupervisedMorphAnalyzer(add_marker='false')
        input_str =  "शास्त्रीयभाषा"
        current = analyzer.morph_analyze(input_str, 'hi')
        correct = ['शास्त्रीय', 'भाषा']
        self.assertEqual(current,correct)
```


```python
**

Error
Traceback (most recent call last):
  File "/home/soumya/indic_nlp_soumya/test_indian_morph.py", line 59, in test_morph_analyze
    current = analyzer.morph_analyze(input_str, 'hi')
  File "/home/soumya/indic_nlp_soumya/indic_morph.py", line 100, in morph_analyze
    val=UnsupervisedMorphAnalyzer._morfessor_model(self, word, lang)
  File "/home/soumya/indic_nlp_soumya/indic_morph.py", line 73, in _morfessor_model
    morfessor_model=io.read_any_model(INDIC_RESOURCES_PATH+'/morph/morfessor/{}.model'.format(lang))
  File "/home/soumya/anaconda3/lib/python3.5/site-packages/morfessor/io.py", line 203, in read_any_model
    model.load_segmentations(self.read_segmentation_file(file_name))
  File "/home/soumya/anaconda3/lib/python3.5/site-packages/morfessor/baseline.py", line 487, in load_segmentations
    for count, segmentation in segmentations:
  File "/home/soumya/anaconda3/lib/python3.5/site-packages/morfessor/io.py", line 53, in read_segmentation_file
    for line in self._read_text_file(file_name):
  File "/home/soumya/anaconda3/lib/python3.5/site-packages/morfessor/io.py", line 240, in _read_text_file
    encoding = self._find_encoding(file_name)
  File "/home/soumya/anaconda3/lib/python3.5/site-packages/morfessor/io.py", line 309, in _find_encoding
    file_obj = open(f, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/morph/morfessor/hi.model'

```

I don't inderstand what the problem is. 
All the arguments called to the function are of the same type. But the call to the morfessor model is not going through. 
