# Ensemble Trees 

## Random Forest 

- https://towardsdatascience.com/random-forest-in-python-24d0893d51c0
- CV and grid search: https://towardsdatascience.com/hyperparameter-tuning-the-random-forest-in-python-using-scikit-learn-28d2aa77dd74

### Cross Validation 

Ref: http://scikit-learn.org/stable/modules/cross_validation.html

```py 


```

### Max Depth 

When you run a random forest with the parameter `maxDepth = None`, how do you figure how how deep the tree was? 

- https://datascience.stackexchange.com/questions/19842/anyway-to-know-all-details-of-trees-grown-using-randomforestclassifier-in-scikit/36228#36228
- https://stackoverflow.com/questions/34214087/how-do-you-access-tree-depth-in-pythons-scikit-learn

```py
def dectree_max_depth(tree):
    n_nodes = tree.node_count
    children_left = tree.children_left
    children_right = tree.children_right

    def walk(node_id):
        if (children_left[node_id] != children_right[node_id]):
            left_max = 1 + walk(children_left[node_id])
            right_max = 1 + walk(children_right[node_id])
            return max(left_max, right_max)
        else: # leaf
            return 1

    root_node_id = 0
    return walk(root_node_id)

[dectree_max_depth(t.tree_) for t in rf.estimators_]
```

```py
[estimator.tree_.max_depth for estimator in forest.estimators_]
```

### Feature Importance 

- https://towardsdatascience.com/running-random-forests-inspect-the-feature-importances-with-this-code-2b00dd72b92e
- https://towardsdatascience.com/running-random-forests-inspect-the-feature-importances-with-this-code-2b00dd72b92e

```py 
import pandas as pd
feature_importances = pd.DataFrame(rf.feature_importances_,
                                   index = X_train.columns,
                                    columns=['importance']).sort_values('importance',                                                                 ascending=False)
```

### Visualize Tree 

[reference](https://medium.com/@rnbrown/creating-and-visualizing-
decision-trees-with-python-f8e8fa394176)

```py
# Import tools needed for visualization
from sklearn.tree import export_graphviz
import pydot
import pydotplus
from IPython.display import display, Image

# grab on the the trees 
tree = rf.estimators_[5]

# Export the image to a dot file
export_graphviz(tree, out_file = 'tree.dot', feature_names = x_train.columns, rounded = True,max_depth=3,filled=True)

# Use dot file to create a graph
graph = pydotplus.graph_from_dot_file('tree.dot')  

# Write graph to a png file
graph.write_png('tree.png')

# display 
Image(graph.create_png())
```

## Gradient-Boosted Trees 

- https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/
- http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html
- XGBOOST: https://www.datacamp.com/community/tutorials/xgboost-in-python

