# Support Vector Machine 

- sklearn: https://scikit-learn.org/stable/modules/svm.html
- stat quest: https://www.youtube.com/watch?v=efR1C6CvhmE


## SVM Regression 

- [https://www.saedsayad.com/support_vector_machine_reg.htm](https://www.saedsayad.com/support_vector_machine_reg.htm)
- [https://www.analyticsvidhya.com/blog/2020/03/support-vector-regression-tutorial-for-machine-learning/](https://www.analyticsvidhya.com/blog/2020/03/support-vector-regression-tutorial-for-machine-learning/)



## Clasification 

```py 
from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)

clf.predict([[2., 2.]])

# get support vectors
clf.support_vectors_

# get indices of support vectors
clf.support_

# get number of support vectors for each class
clf.n_support_

```