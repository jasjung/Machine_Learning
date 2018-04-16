# POS

Resources: 

- http://www.nltk.org/book/ch05.html
- https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/
- http://textminingonline.com/dive-into-nltk-part-iii-part-of-speech-tagging-and-pos-tagger

```py
import nltk
nltk.pos_tag(['go'])
# out: [('go', 'VB')]

nltk.help.upenn_tagset('NN')
```