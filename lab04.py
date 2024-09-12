!pip install scikit-learn tensorflow keras
import pandas as pd
import keras
import tensorflow

from keras.models import Sequential
from keras.layers import Dense
from scikeras.wrappers import KerasClassifier
from keras.utils import to_categorical
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

dataframe = pd.read_csv("D:/YANSHU/LABORATORIO_04/iris.csv", header = None)
dataset = dataframe.values
dataset
