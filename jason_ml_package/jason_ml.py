import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydot
import pydotplus
import seaborn as sns
from IPython.display import Image, display
from sklearn.metrics import (accuracy_score, auc, average_precision_score,
                             confusion_matrix, f1_score, ndcg_score,
                             precision_recall_curve, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz


def jj_binary_score(y_test, y_pred, threshold=0.5):
    '''
    y_test: list of 1s and 0s 
    y_pred: list of predictions between 0 and 1 
    '''
    # convert prob to class
    y_pred_class = y_pred > threshold
    print(f'Scoring {len(y_test):,d} observations.')
    print('---------------------------')
    print('Accuracy :', round(accuracy_score(y_test, y_pred_class), 3))
    print('ROC AUC  :', round(roc_auc_score(y_test, y_pred), 3))
    print('PR AUC   :', round(average_precision_score(y_test, y_pred), 3))
    print('F1 Score :', round(f1_score(y_test, y_pred_class), 3))
    print('Precision:', round(precision_score(y_test, y_pred_class), 3))
    print('Recall   :', round(recall_score(y_test, y_pred_class), 3))
    print('NDCG     :', round(ndcg_score([y_test], [y_pred]), 3))
# jj_binary_score(y_test,y_pred)


def find_null_cols(df):
    '''
    df: pandas dataframe 
    '''
    df_na = pd.DataFrame(df.isnull().sum().sort_values(
        ascending=False), columns=['total'])
    df_na['percent'] = df_na.total/len(df)
    df_na.head()

    return df_na[df_na.total > 0]
# find_null_cols(df)


def find_string_cols(df):
    '''
    df: pandas dataframe 
    '''
    str_col = []
    for i in df.columns:
        check = str(type(df[i].values[0]))
        if 'str' in check:
            str_col.append(i)

    print('number of columns with strings', len(str_col))

    return str_col


def find_num_cols(df):
    '''
    df: pandas dataframe 
    '''
    str_col = []
    for i in df.columns:
        check = str(type(df[i].values[0]))
        if 'str' in check:
            str_col.append(i)

    print('number of columns with strings', len(str_col))

    return str_col


def rf_features(rf_model, features, top_n=10, plot=True):
    '''Prints top random forest features 
    rf_model: sklearn random forest model object 
    features: list of features in the order presented to the model training 
    '''
    feature_df = pd.DataFrame(rf_model.feature_importances_,
                              index=features,
                              columns=['importance'])
    feature_df = feature_df.sort_values('importance', ascending=False)
    feature_df = feature_df.head(top_n)

    if plot:
        feature_df.plot.bar()

    return feature_df


def corr_matrix(df, target_name, top_n=8, fig_size=(13, 5)):
    '''
    df: pandas dataframe
    target_name: target_name in string 
    fig_size: 
    '''
    # selects numerical columns only
    num_cols = list(df.select_dtypes(include='number').columns)
    # select boolean columns only
    bool_cols = list(df.select_dtypes(include='bool').columns)
    # compute corr
    corr = df[num_cols+bool_cols].corr()
    # plot the heatmap
    plt.figure(figsize=fig_size)

    sns.heatmap(corr,
                xticklabels=corr.columns,
                yticklabels=corr.columns,
                annot=True,)
    # get corr features
    corr_df = pd.DataFrame(corr[target_name]).sort_values(
        by=target_name, ascending=0, key=lambda x: np.abs(x))

    # feature plot #########################################################################

    top_df = corr_df[1:top_n].apply(abs)

    plt.figure(figsize=(top_n, 5))
    # plt.plot(x)
    plt.bar(top_df.index, top_df.responded)

    plt.xticks(rotation=70)
    plt.title('Top features by correlation score')
    plt.ylabel('probability')
    plt.xlabel('features')

    return corr_df
# corr_matrix(df,y)


def detect_outliers(df, std_threshold=3):
    '''
    df: full pandas dataframe 
    std_threshold: how many standard deviations away do you have to be to be considered an outlier 
    '''
    out_df = pd.DataFrame(df.select_dtypes(include='number')
                          .apply(lambda x: np.abs(x-np.mean(x))/np.std(x) > std_threshold).sum(),
                          columns=['total']).sort_values('total', ascending=False)

    out_df['percent'] = out_df.total/len(df)*100

    return out_df[out_df.total > 0]


def plot_history(history, file_unique_name, directory):
    '''
    history: model.fit object 
    file_unique_name: name to save the image 
    directory: directory to save the image 
    '''
    # plot accuracy and loss curve
    # summarize history for accuracy
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model accuracy: %s' % file_unique_name)
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')

    save_path = os.path.join(directory, '%s_accuracy.png' % (file_unique_name))

    #     save_path = '%s' % (directory,file_unique_name,)
    plt.savefig(save_path)
    plt.show()
    plt.close()
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss: %s' % file_unique_name)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'val'], loc='upper left')
    save_path = os.path.join(directory, '%s_loss.png' % (file_unique_name))
    plt.savefig(save_path)
    #     plt.savefig('3_Model_Training/results/figs/%s_loss.png' % (file_unique_name))
    plt.show()
    plt.close()
# plot_history(history,'test','')


def plot_rf_tree(model, features, max_depth, tree_index=0, save=False):
    '''
    tree: random forest classifier object 
    features: feature names 
    '''
    tree = model.estimators_[tree_index]
    export_graphviz(tree,
                    out_file='tree.dot',
                    feature_names=features,
                    class_names=['0', '1'],
                    rounded=True,
                    max_depth=max_depth,
                    filled=True)
    graph = pydotplus.graph_from_dot_file('tree.dot')

    if save:
        graph.write_png('rf_tree.png')

    display(Image(graph.create_png()))


def plot_pr_auc_binary(y_test, y_pred, model_name):
    # calculate the no skill line as the proportion of the positive class
    no_skill = sum(y_test) / len(y_test)
    # plot the no skill precision-recall curve
    # precision, recall, threshold = precision_recall_curve(y_test, [random.random()/10 for i in range(len(y_test))])
    plt.plot([0, 1], [no_skill, no_skill], linestyle='--', label='No Skill')
    precision, recall, threshold = precision_recall_curve(y_test, y_pred)
    plt.plot(recall, precision, marker='.', label=model_name)
    plt.title('PR AUC Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    # show the legend
    plt.legend()
    # show the plot
    plt.show()


def decile(y_test, y_pred, N=10):
    '''
    args: 
        y_test (list): 1s and 0s values. 
        y_pred (list): 1-D array of probabilities between 0 and 1. 
        N (int): size of the bucket to divide by
    '''
    y = y_test
    result = pd.DataFrame(data={'y_original': y, 'y_prob': y_pred}).sort_values(
        by=['y_prob'], ascending=False).reset_index(drop=True)
    len(result)

    # Create N Tile Segments
    last_chunk_size = len(result) - int(len(result)/N)*(N-1)
    L = []
    for j in range(N):
        for i in range(int(len(result)/N)):
            if j == N-1:
                # [j+1]*last_chunk_size
                L = L + ([N-j]*last_chunk_size)
                break
            else:
                L.append(N-j)

    ntile = pd.Series(L).reset_index(drop=True)
    result = pd.concat([result, ntile], axis=1)
    result.columns = ['y_orig', 'y_prob', 'ntile']

    final = result.groupby(['ntile']).mean(
    ).reset_index().sort_values('ntile', ascending=False)
    final.columns = ['ntile', 'avg_y', 'avg_yhat']

    print('*** Decile Summary ***')

    #############################################
    # total population in a validation set
    pop_size = len(y_test)  # x.shape[0]
    print(' total size:', pop_size)
    # avg size in each bucket
    bucket_size = int(pop_size/N)
    print(' bucket_size:', bucket_size)
    # y=1 in our set
    total_y = sum(y)
    print(' total number of y\'s:', total_y)
    #############################################

    final['no_respose_captured'] = final.avg_y * bucket_size
    final['perc_of_all_ys'] = final.no_respose_captured/total_y
    final['cumm_sum'] = np.cumsum(final.perc_of_all_ys)*100
    final = final.reset_index(drop=True)

    print()
    print(' Model captures %.1f%%, %.1f%%, %.1f%% of all targets (Y) in the top 10, 20, 30%% 100-Tile Buckets'
          % (final.cumm_sum[0], final.cumm_sum[1], final.cumm_sum[2]))
    print(f' For top {bucket_size} candidates, {int(final.no_respose_captured[0])} of them are likely to respond.')

    # plot d
    plt.plot(final.perc_of_all_ys*100)
    plt.xticks(range(10), [str(i) for i in range(10, -1, -1)])
    plt.title('Percent of Target Captured by Decile')
    plt.ylabel('Percentage')
    plt.xlabel('Decile Group')

    return final
# final = decile(y_test, y_pred[:,1].flatten())
