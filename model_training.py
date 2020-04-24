#####################################################
## Rquirements
import pandas as pd
import numpy as np

import pickle

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold

from sklearn import svm
from sklearn.naive_bayes import BernoulliNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.feature_selection import RFE

from sklearn.linear_model import LogisticRegression


from imblearn.under_sampling import RandomUnderSampler

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#####################################################



#####################################################
## Resampling function
def resample(X, y):
    rus = RandomUnderSampler(random_state=42)
    return rus.fit_resample(X, y)
#####################################################



#####################################################
# Plot confusion matrix
def plot_confusion_matrix(cm, labels, title, cmap=plt.cm.BuGn):
    cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    #show_values_conf_matr(c)
    ax.set_xticklabels([""] + list(labels), rotation=90)
    ax.set_yticklabels([""] + list(labels))
    plt.tight_layout()
    plt.xlabel('Predicted class')
    plt.ylabel('True class')
    plt.title(title)
    ax.tick_params(axis='both', which='both', length=0)

    width, height = cm.shape

    colour_threshold = np.amax(cm) / 2

    for x in range(width):
        for y in range(height):
            if cm[x][y] > 0:
                if cm[x][y] > colour_threshold:
                    color = 'white'
                else:
                    color = 'black'

                ax.text(y,
                        x,
                        str(round(cm[x][y]*100,2))+'%',
                        verticalalignment='center',
                        horizontalalignment='center',
                        color=color,
                        fontsize=15)
#####################################################




#####################################################
# # Initialize dataset
# - load structerd dataset
# - plot class distribution
# - split feature vectors and their targets
data = pd.read_csv('./columns_remover/DATASET.csv')
dataset = data.drop(columns=['Unnamed: 0','Name'])
#####################################################


#####################################################
# plot instances count for each label
sns.countplot(x='Label', data=dataset);
plt.show()
#####################################################


#####################################################
np_dataset = dataset.to_numpy() # Convert pandas dataframe to numpy array for faster computations
# Split the data from the labels
X = np_dataset[:,0:-1] 
y = np_dataset[:,-1] 
#####################################################


#####################################################
# ### the dataset is highly unbalanced (uneven class distribution)
# - resample using a random under sampler
X_res, y_res = resample(X, y)

print(X_res.shape, y_res.shape)
#####################################################


#####################################################
# plot instance count for each label after balancing (Random Undersampling)
sns.countplot(x=y_res)
plt.show()
#####################################################


#####################################################
# ### Split the dataset into disjoint training and testing sets
# - 80% of the samples are used to train the model
# - 20% of the samples are used to evaluate the models performance
X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, train_size=0.80, shuffle=True, stratify=y_res)
#####################################################


#####################################################
# # Initialize the cross-validation
#     - k = 10
#     - shuffle the dataset before splitting to redistribute samples
# # Initialize the models 

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
svm = svm.SVC()
bnb = BernoulliNB()
rndfst = RandomForestClassifier(n_estimators=10)
#####################################################



#####################################################
def sequential_feature_selection(X, y, k):
    sfs = SFS(LinearRegression(),
              k_features=k,
              forward=True,
              floating=False,
              scoring = 'r2',
              cv = 0)
    fit = sfs.fit(X, y)
    return fit

def recursive_feature_elimination(X, y, k):
    select = LogisticRegression()
    rfe = RFE(select, k)
    fit = rfe.fit(X, y)
    return fit
#####################################################


#####################################################
## FEATURE SELECTION BEFORE TRAINING THE CLASSIFIER 
fit = recursive_feature_elimination(X_train, Y_train, 100)
#####################################################



#####################################################
def train(model, X, y, kfold):
    
    predictions = []
    
    for train, validate in kfold.split(X, y):
        X_train = X[train]
        Y_train = y[train]
        X_validate = X[validate]
        Y_validate = y[validate]
        
        print(X_train.shape, Y_train.shape)
        
        ## FEATURE SELECTION BEFORE TRAINING THE CLASSIFIER 
        fit = sequential_feature_selection(X_train, Y_train, 100)
        selections.append(fit) # save the selected features for each fold
    
        X_train_selected = fit.transform(X_train)
        X_validate_selected = fit.transform(X_validate)
        
        # Fit the models --------- TRAINING
        model.fit(X_train_selected, Y_train)
    
    
        # evaluate the model ---- PREDICTIONS
        prediction=model.predict(X_validate_selected)
        
        predictions.append([
            Y_validate, # True labels
            prediction # Model's predictions
        ])
    return [model, predictions]
#####################################################


#####################################################
# ## Initialize the variables to store:
# - Selection models (selections)
# - Predictions ([model_name]_predctions)

selections = []

svm_train = train(svm, X_train, y_train, kfold)
bnb_train = train(bnb, X_train, y_train, kfold)
rndfst_train = train(rndfst, X_train, y_train, kfold)

svm_predictions = svm_train[1]
bnb_predictions = bnb_train[1]
rndfst_predictions = rndfst_train[1]
#####################################################



#####################################################
def test(X, model, selector):
    X_selected = selector.fit(X)
    return model.predict(X_selected)
#####################################################



## Transform the test set to the selected features
X_test_selected = fit.transform(X_test)

# test the model ---- PREDICTIONS
svm_prediction=test(X_test_selected, svm, fit)
bnb_prediction=test(X_test_selected, bnb, fit)
rndfst_prediction=test(X_test_selected, rndfst, fit)

plot_confusion_matrix(svm_current_cm, cm_plot_labels, svm_title)
plot_confusion_matrix(bnb_current_cm, cm_plot_labels, bnb_title, cmap=plt.cm.Blues)
plot_confusion_matrix(rndfst_current_cm, cm_plot_labels, rndfst_title,cmap=plt.cm.Purples)


# # use the predictions and the labels from the test set to compute and plot the confusion matrix



svm_cm = confusion_matrix(y_test, svm_prediction)
bnb_cm = confusion_matrix(y_test, bnb_prediction)
rndfst_cm = confusion_matrix(y_test, rndfst_prediction)

cm_plot_labels = ['Benign', 'Malware']
svm_title = 'SVM Confusion matrix'
bnb_title = 'BernoulliNB Confusion matrix'
rndfst_title = 'Random Forest Confusion matrix'

plot_confusion_matrix(svm_cm, cm_plot_labels, svm_title)
plot_confusion_matrix(bnb_cm, cm_plot_labels, bnb_title, cmap=plt.cm.Blues)
plot_confusion_matrix(rndfst_cm, cm_plot_labels, rndfst_title,cmap=plt.cm.Purples)




def cm_average(predictions):
    avg_cm = [[0,0],[0,0]]
    for prediction in predictions:
        cm = confusion_matrix(
            prediction[0], # true labels
            prediction[1]) # model's predictions
        
        for i in range (0,2):
            for j in range (0,2):
                avg_cm[i][j] = np.rint((avg_cm[i][j] + cm[i][j]) / 2)
    return avg_cm


# # Export the top-performing models to deploy in an app
svm_name = 'models/svm.sav'
bnb_name = 'models/bnb.sav'
rndfst_name = 'models/rndfst.sav'


pickle.dump(svm, open(svm_name, 'wb'))
pickle.dump(bnb, open(bnb_name, 'wb'))
pickle.dump(rndfst, open(rndfst_name, 'wb'))
