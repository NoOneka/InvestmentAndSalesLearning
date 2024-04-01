import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

#Importing sales base
base = pd.read_excel(r'Archive')


#Linear relationship between investment and sales 
#plt.scatter(base["investimento em marketing"], base["Venda Qtd"])
#plt.show()

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(base["Investimento em marketing"].values.reshape(-1, 1), base["Venda Qtd"])

reg.coef_
reg.intercept_

#Linear Regression graphic predict 
reg.predict([[75]])
plt.scatter(base["investimento em marketing"], base["Venda Qtd"])
plt.scatter(75, reg.predict([[75]])[0], color="k")
x=np.array(base["investimento em marketing"])
y=reg.intercept_ + x*reg.coef_
plt.plot(x,y,"r")
plt.show()
print(base)


