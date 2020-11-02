
#pip install sklearn


import pandas as pd
from sklearn import tree
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

zoo = pd.read_csv("data/zoo.csv")

feature_cols = ['hair', 'feathers', 'eggs', 'airborne', 'aquatic', 'backbone']
X = zoo[feature_cols] #
y = zoo.ismammal

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=10)

# Train Decision Tree Classifer
clf = clf.fit(X, y)


dot_data = StringIO()

# Visualization  in graph
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True, feature_names = feature_cols, class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('mammal.png')
Image(graph.create_png())

# if the visualization code does not work you may use tree.plot