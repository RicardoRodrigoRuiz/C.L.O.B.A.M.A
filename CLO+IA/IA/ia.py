
##########################################
# ALGORITHM  FOR CLOUD AND BIG DATA      #
# Authors: Carlos Bilbao, Álvaro Ortiz   #
##########################################

import pandas as pd
import numpy
#import significance
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC

############################
# 1 PREPARATION		       #
############################

ddbb_wars = pd.read_csv("result.csv", na_values='')
#print(ddbb_wars)

# Feature names
headers_wars = list(ddbb_wars)

############################
# 2 DATA EXPLORATION       #
############################

# Column names
print("Wars Features:")
print(headers_wars,'\n')
print("Columns in Wars = ", len(headers_wars))

# Unique elements of column Country
countries = set(ddbb_wars["country"])
print("Unique elems in column Country for wars = ", countries)

############################
# 3 PREPROCESSING          #
############################

# Feature matrix
x = []

# Label Array
y = []

le = preprocessing.LabelEncoder()
le = le.fit(ddbb_wars['country'].unique())

# We prepare the matrix with the data
for index, row in ddbb_wars.iterrows():

	vector = [le.transform([row['country']])[0],
			  row['year'],
			  #le2.transform(row['allies'])[0],
			  #row['borderCountries'], # MISMO PROBLEMA QUE ALLIES
			  row['inversion'],
			  row['gdp']]
	x.append(vector)
	y.append(row['war'])

x = numpy.asarray(x)

############################
# 4 CLASSIFICATION         #
############################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 1)

print("x train shape = ",x_train.shape)
print("y train shape = ",x_test.shape)

# (1) Create the model
# Possible future work -> Find optimal parameters for here 
#SGDclf = SGDClassifier()
SVCclf = LinearSVC()

# (2) Fit the model
#SGDclf.fit(x_train, y_train)
SVCclf.fit(x_train, y_train)

# (3) Predict
SVCy_pred = SVCclf.predict(x_test)
print(SVCy_pred)
#SGDy_pred = SGDclf.predict(x_test)
#print(SGDy_pred)

# Prints most important features for SGD
# sort the features by feature weight and show the first 10 (for news)
#top_feats_n = numpy.argsort(SGDclf.coef_[0])[-10:]

# Creates column for signifance test (p-value)
# significance.columns('bagging_column', SGDy_pred,y_test)

# (4) Report results
#print("SGD REPORT:")
#print(classification_report(y_test, SGDy_pred))
print("")
print("SVC REPORT:")
print(classification_report(y_test, SVCy_pred))

# Possible future work -> McNemar Significance Test (alternative to R)
# Un segundo modelo igual para testearlo aqui con p-value!! Queda bien en reportes.
# tb = mcnemar_table(y_target=numpy.array(y_test), y_model1=SGDy_pred, y_model2=MNBy_pred)
# Test using McNemar
#chi2, p = mcnemar(ary=tb, exact=True)
#print('chi-squared:', chi2)
#print('p-value:', p)
#alpha = 0.5
#if p > alpha:
#print("No significant difference!")
