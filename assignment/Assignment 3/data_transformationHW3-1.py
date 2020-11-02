#Load data from sp500_cmpny_all_stocks_5yr and sp500indexdaily
import pandas as pd
import numpy as np
import statsmodels.api as sm
sp500=pd.read_csv("data/sp500indexdaily.csv")
sp500['Date']= pd.to_datetime(sp500['Date'])

sp500company=pd.read_csv("data/sp500_cmpny_all_stocks_5yr.csv")
sp500company['date']= pd.to_datetime(sp500company['date'])

#Transform company data
cmpnyls=sp500company['Name'].unique()

cmpnydata={}
price_close = np.array([])
ncol=0
selectcmpny=[]

for cmpny in ['AMZN', 'AAPL', 'JNJ', 'BRK.B', 'MSFT', 'JPM']:
    if ((len(sp500company[sp500company['Name']==cmpny]['close'])==1259) and (not np.isnan(sp500company[sp500company['Name'] == cmpny].sort_values('date')['close']).any())):
        if ncol==0:
            price_close=sp500company[sp500company['Name'] == cmpny].sort_values('date')['close']
        else:
            price_close = np.vstack((price_close, sp500company[sp500company['Name'] == cmpny].sort_values('date')['close']))
        ncol=ncol+1
        selectcmpny.append(cmpny)

price_close=pd.DataFrame.from_records(price_close.transpose())
price_close.columns=selectcmpny

# construct the target variable and predictors
startdate = pd.Timestamp(2013, 2, 8)
enddate = pd.Timestamp(2018, 2, 7)
y=sp500[(sp500['Date']>=startdate) & (sp500['Date']<=enddate)]['Close'].values
X_cmpny=sm.add_constant(price_close[['AMZN', 'AAPL', 'JNJ', 'BRK.B', 'MSFT', 'JPM']])