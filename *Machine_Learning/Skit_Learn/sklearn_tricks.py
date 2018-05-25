from sklearn.model_selection import train_test_split
'''
This stratify parameter makes a split so that the proportion of values in the sample produced will be the same as the proportion of values provided to parameter stratify.
'''

X_train, X_test = train_test_split(data, test_size = 0.2, 
                                   random_state = 1234,
                                   stratify = data['category'])

                                   