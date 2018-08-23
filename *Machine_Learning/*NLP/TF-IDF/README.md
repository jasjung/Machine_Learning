# TF-IDF

Reference

- `show_top_n_gram`: https://stackoverflow.com/questions/25217510/how-to-see-top-n-entries-of-term-document-matrix-after-tfidf-in-scikit-learn


```py 
vocab = sorted(tfidf.vocabulary_, key=tfidf.vocabulary_.get, reverse=False)

# extract top words from a given document 
top10 =[]

for i, blob in enumerate(df):
    print('completed: %s' % (i/len(df_nonull)*100),flush=True,end='\r')      
    #     print("Top words in document {}".format(i + 1))

    zipped = zip(vocab,X[i].toarray()[0])
    sorted_words = sorted(zipped,key = lambda t: t[1],reverse=True)
    temp = []
    for word, score in sorted_words[:10]:
        # do not include score = 0 
        if score == 0: 
            continue 
            #print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))        
        temp.append(word)

    top10.append(temp)
```

Show Top Features 

```py
indices = np.argsort(tfidf.idf_)[::-1]
features = tfidf.get_feature_names()
top_n = 100
top_features = [features[i] for i in indices[:top_n]]
print (top_features)
```