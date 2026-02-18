import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df=pd.read_csv("promoters.data", header=None)
df.head()
df.columns=["label","id","sequence"]
df["label"]=df["label"].map({"+" : 1, "-" : 0})


df.head()
def encode_sequence(seq):
    mapping={"A":0, "C":1, "G":2, "T":3}
    seq=str(seq).strip()
    return [mapping[char.upper()]for char in seq]

X=df["sequence"].apply(encode_sequence).tolist()
y=df["label"]
X_train, X_test,y_train,y_test= train_test_split(X,y,test_size=0.2,random_state=42)
model = LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print("Accuracy:", accuracy_score(y_test,pred))
plt.figure(figsize=(7,5))
sns.countplot(x="label", data=df)

plt.xlabel("Promoter (1) vs Non-Promoter (0)")
plt.ylabel("Count")
plt.title("Class Distribution")

plt.show()
