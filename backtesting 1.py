import pandas_datareader.data as pdr
import datetime as dt
import pandas as pd
import numpy as np
start_date = dt.date.today() - dt.timedelta(3650)
end_date = dt.date.today()
tickers  = ['MSFT']
ohlcv = pdr.get_data_yahoo(tickers[0],start_date,end_date)
df = ohlcv.copy()
BollBnd(ohlcv,20).iloc[-200:,[6,7,8]].plot()
RSI(ohlcv,14)['RSI'].plot()

def MACD(Df,a,b,c):
    df = Df.copy()
    df['MA_Fast'] = df['Adj Close'].ewm(span = a , min_periods = a).mean()
    df['MA_Slow'] = df['Adj Close'].ewm(span = b , min_periods = b).mean()
    df['MACD'] = df['MA_Fast'] - df['MA_Slow']
    df['Signal'] = df['MACD'].ewm(span = c ,min_periods = c).mean()
    df.dropna(inplace=True)
    return df

def BollBnd(Df,n):
    df = Df.copy()
    df['MA'] = df['Adj Close'].rolling(n).mean()
    df['BB_up'] = df['Adj Close'].rolling(n).mean() + 2*df['MA'].rolling(n).std()
    df['BB_dn'] = df['Adj Close'].rolling(n).mean() - 2*df['MA'].rolling(n).std()
    df['BB_Width'] = df['BB_up'] - df['BB_dn']
    df.dropna(inplace=True)
    return df

def RSI(Df,n):
    df = Df.copy()
    df['delta'] = df['Adj Close'] - df['Adj Close'].shift(1)
    df['gain'] = np.where(df['delta']>=0,df['delta'],0)
    df['loss'] = np.where(df['delta']<0,abs(df['delta']),0)
    avg_gain = []
    avg_loss = []
    gain = df['gain'].tolist()
    loss = df['loss'].tolist()
    for i in range(len(df)):
        if i < n:
            avg_gain.append(np.NaN)
            avg_loss.append(np.NaN)
        elif i == n:
            avg_gain.append(df['gain'].rolling(n).mean().tolist()[n])
            avg_loss.append(df['loss'].rolling(n).mean().tolist()[n])
        elif i > n:
            avg_gain.append(((n-1)*avg_gain[i-1] + gain[i])/n)
            avg_loss.append(((n-1)*avg_loss[i-1] + loss[i])/n)

    df['avg_gain'] = np.array(avg_gain)
    df['avg_loss'] = np.array(avg_loss)
    df['RS'] = df['avg_gain']/df['avg_loss']
    df['RSI'] = 100 - (100/(1+df['RS']))
    return df
#setup for starting the backtesting
portfolio = 500
days = 70
stock_list = ['RELIANCE.NS']
prices = read_data(stock_list, days)
#nav dataframe has two columns leftover cash in hand, and stock which is value of stock that we own
nav = pd.DataFrame(index = prices.tail(days-14).index)
nav = nav.assign(leftover = np.zeros(days-14), stock = np.zeros(days-14))
nav.iloc[0,0] = portfolio

signal = 0
prev_signal = 0
for index, row in nav.iloc[1:].iterrows():
    signal = np.sign(signal + RSI(prices.loc[:index].tail(14)))
    leftover = nav.loc[:index].tail(2).head(1).iloc[0,0]

    if(signal == -1):
        nav.loc[index, 'leftover'] = leftover
        nav.loc[index, 'stock'] = 0
        continue

    if(prev_signal == 0 and signal == 1):
        #buy
            nav.loc[index, 'leftover'] = leftover - prices.loc[index][0]
            nav.loc[index, 'stock'] = prices.loc[index][0]


    if(prev_signal == 1 and signal == 1):
            #hold
                nav.loc[index, 'leftover'] = leftover
                nav.loc[index, 'stock'] = prices.loc[index][0]

    if(prev_signal == 1 and signal == 0):
                #sell
                    nav.loc[index, 'leftover'] = leftover + prices.loc[index][0]
                    nav.loc[index, 'stock'] = 0

    if(prev_signal == 0 and signal == 0):
            #wait
                nav.loc[index, 'leftover'] = leftover
                nav.loc[index, 'stock'] = prices.loc[index][0]

    prev_signal = signal

nav.sum(axis =1).plot()


def read_data(stock_list, days):
    df = pd.DataFrame()
    for ticker in stock_list :
        df[ticker] = data.DataReader(ticker,'yahoo',start = '1/1/2010')['Adj Close']
    return df.head(days)

def RSI(price_data) :
    delta = price_data.diff()
    up, down = delta.copy(), delta.copy()
    up[up<0] = 0
    down[down>0] = 0

    roll_up = up.mean()
    roll_down = down.abs().mean()
     RS = roll_up/roll_down
     RSI = (100.0-(100.0/(1.0+RS)))[0]

     if(RSI > 70): return -1
     if(RSI <30): return 1
     else return 0
