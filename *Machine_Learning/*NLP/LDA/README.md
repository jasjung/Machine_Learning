# Latent Dirichlet Allocation (LDA) 

**A topic modeling algorithm.**

### General Reference: 

- wiki: [https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)
- article: [https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d](https://medium.com/@lettier/how-does-lda-work-ill-explain-using-emoji-108abf40fa7d)
- concept: [http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/](http://blog.echen.me/2011/08/22/introduction-to-latent-dirichlet-allocation/)

### Two methods available: 

1. [Gensim package](https://radimrehurek.com/gensim/)
2. [LDA package](https://pythonhosted.org/lda/) 


## 1. Gensim links 

- [https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24](https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24)
- tutorial: [http://brandonrose.org/clustering](http://brandonrose.org/clustering)
- LDA\_specific_tutorial: [https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)
- [https://markroxor.github.io/gensim/static/notebooks/lda_training_tips.html](https://markroxor.github.io/gensim/static/notebooks/lda_training_tips.html)
- Tips: [https://miningthedetails.com/blog/python/lda/GensimLDA/](https://miningthedetails.com/blog/python/lda/GensimLDA/)
- Coloring: [https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/topic_methods.ipynb](https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/topic_methods.ipynb)

### Code 

```
# The function `get_term_topics` returns the odds of that particular word belonging to a particular topic. 
model.get_term_topics('water')

# top_topics: Get the topics with the highest coherence score the coherence for each topic.
lda_model.top_topics(corpus)

lda_model.print_topics((num_topics=20, num_words=10)
```

### ETC 

```py 
# Set up log to external log file
import logging
logging.basicConfig(filename='lda_model.log', format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
```