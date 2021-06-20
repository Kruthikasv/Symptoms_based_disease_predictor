import pandas as pd
import pickle
df=pd.read_csv("Training.csv")
df = df.sample(frac=1).reset_index(drop=True)
x_train=df.drop("prognosis",axis=1)
y_train=df["prognosis"]
df1=pd.read_csv("Testing.csv")
x_test=df1.drop("prognosis",axis=1)
y_test=df1["prognosis"]

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb = gnb.fit(x_train,y_train)

'''y_pred=gnb.predict(x_test)
gnb.score(x_test,y_test)*100'''

pickle.dump(gnb,open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))