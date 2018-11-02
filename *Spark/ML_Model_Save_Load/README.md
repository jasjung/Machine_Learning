# ML Model Save and Load 

Example: Saving Random Forest model and loading it. 

```py 
from pyspark.ml.classification import RandomForestClassifier ,RandomForestClassificationModel

# given rfclassifier model saved as model 
model.save('rf_model') 

# to load 
model = RandomForestClassificationModel.load('rf_model')
```
