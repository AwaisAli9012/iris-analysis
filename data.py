import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Iris.csv")

print("The shape is",df.shape)
print("The columns are",df.columns)
print("The head of this dataset is",df.head())
print("The info is")
df.info()
print("The description is",df.describe())
fig,axes=plt.subplots(2,2,figsize=(12,10))
a1=axes[0,0]
a2=axes[0,1]
a3=axes[1,0]
a4=axes[1,1]
sns.scatterplot(data=df,x='SepalLengthCm',y='SepalWidthCm',color='green',ax=a1)
a1.set_xlabel('SepalLengthCm')
a1.set_ylabel('SepalWidthCm')
a1.set_title("Sepal Length vs Sepal Width")


sns.histplot(data=df['SepalLengthCm'],color='green',ax=a2)
a2.set_xlabel('SepalLengthCm')
a2.set_ylabel("Frequency")


sns.boxplot(data=df.iloc[:,1:5],ax=a3)
a3.set_xticklabels(df.columns[1:5],rotation=45)
a3.set_title("Boxplot of all the features")

axes[1,1].axis('off')
plt.show()
