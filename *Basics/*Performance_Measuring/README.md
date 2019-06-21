# Performance Measuring

Reference: 

- micro_macro_averaging: [https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin](https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin)

Notes 

- *In a multi-class classification setup, micro-average is preferable if you suspect there might be class imbalance.*
- Macro: Simple averaging
- Micro: Weighted averaging


### Error 

- dealing with f1score error: https://stackoverflow.com/questions/43162506/undefinedmetricwarning-f-score-is-ill-defined-and-being-set-to-0-0-in-labels-wi

`UndefinedMetricWarning: No positive samples in y_true, true positive value should be meaningless`