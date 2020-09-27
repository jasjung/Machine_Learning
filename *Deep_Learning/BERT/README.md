# BERT 

- https://github.com/google-research/bert/blob/master/predicting_movie_reviews_with_bert_on_tf_hub.ipynb
- https://towardsml.com/2019/09/17/bert-explained-a-complete-guide-with-theory-and-tutorial/
- Attention Youtube Tutorial in Korean: https://www.youtube.com/watch?v=mxGCEWOxfe8
- https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270


Key points 

- Masked Language Model 
- a language model which is bidirectionally trained can have a deeper sense of language context and flow. 
- goal is to learn a language model, aka encoder only. 
- Q&A, Next sentence prediction, CLS, SEP 


## Attention 

https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/

To understand BERT, first understand Attention 

Attention key points from the article.: 

- Attention allows the model to focus on the relevant parts of the input sequence as needed.
- An attention model differs from a classic sequence-to-sequence model in two main ways: First, the encoder passes a lot more data to the decoder. Instead of passing the last hidden state of the encoding stage, the encoder passes all the hidden states to the decoder:
- Second, an attention decoder does an extra step before producing its output. In order to focus on the parts of the input that are relevant to this decoding time step, the decoder does the following:
	1. Look at the set of encoder hidden states it received – each encoder hidden states is most associated with a certain word in the input sentence
	2. Give each hidden states a score (let’s ignore how the scoring is done for now)
	3. Multiply each hidden states by its softmaxed score, thus amplifying hidden states with high scores, and drowning out hidden states with low scores

## Transformer 

- http://jalammar.github.io/illustrated-transformer/
- https://colab.research.google.com/github/tensorflow/tensor2tensor/blob/master/tensor2tensor/notebooks/hello_t2t.ipynb#scrollTo=WkFUEs7ZOA79
- https://www.tensorflow.org/tutorials/text/transformer

Key points:

- The biggest benefit, however, comes from how The Transformer lends itself to parallelization.
- From Attention is All You Need.
- Part of Tensor2Tensor package. 
- the word in each position flows through its own path in the encoder. 
- When the model is processing the word “it”, self-attention allows it to associate “it” with “animal”. As the model processes each word (each position in the input sequence), self attention allows it to look at other positions in the input sequence for clues that can help lead to a better encoding for this word.
- Self attention: for each word, we create a Query vector, a Key vector, and a Value vector. 
-  “multi-headed” attention
- with multi-headed attention we have not only one, but multiple sets of Query/Key/Value weight matrices (the Transformer uses eight attention heads, so we end up with eight sets for each encoder/decoder).


## Bert 

http://jalammar.github.io/a-visual-guide-to-using-bert-for-the-first-time/

