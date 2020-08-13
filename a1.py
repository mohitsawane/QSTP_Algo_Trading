#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Fetching Data
import pandas_datareader.data as pdr
import datetime as dt
import pandas as pd
tickers  = ['SBIN.NS'] # Enter all the tickers whose data you require
stock_cp = pd.DataFrame()
start_date = dt.date.today() - dt.timedelta(365)  # Enter the Startdate in the form of datetime.date()
end_date = dt.date.today() # Enter the End Date in the form of datetime.date()
attempt = 0
drop = []
while len(tickers) != 0 and attempt <=5:
    tickers = [j for j in tickers if j not in drop]
    for i in range(len(tickers)):
        try:
            temp = pdr.get_data_yahoo(tickers[i],start_date,end_date)
            temp.dropna(inplace = True)
            stock_cp[tickers[i]] = temp['Adj Close']
            drop.append(tickers[i])
        except:
            print(tickers[i],"failed to fetch data.....retrying")
            continue
        attempt+=1


# In[2]:


stock_cp


# In[3]:


def rsi():
    s = stock_cp.copy()
    dailypos = list()
    dailyneg = list()
    rsi =list()
    forteencount = 0
    avggain = list()
    avglos = list()
    count = 0

    for delta in (stock_cp['SBIN.NS']-stock_cp['SBIN.NS'].shift(1)).dropna() :
            #daily.append(delta)

            #-----------------------------
                    if delta > 0:
                        dailypos.append(delta)
                        dailyneg.append(0)
                    else:
                        dailyneg.append(delta)
                        dailypos.append(0)
                        count++

                    if forteencount == 14:

                        avggain.append((sum(dailypos))/(14 - count))
                        avglos.append((sum(dailyneg))/count)
                        forteencount = 0
                        count = 0
                        dailypos.clear()
                        dailyneg.clear()



        forteencount++
    #daily = pd.Series(dailypos)
    #dailypos = daily.[]
    #avggain = daily.rolling(window=14).mean()
    for i in range(len(avggain)) :
             rsilist.append(100 - (100/(1 + (avggain[i]/avglos[i]))))



    stock_cp['rsi'].append(rsilist) = rsilist.Series.
    return stock_cp


# In[4]:


def macd():
    pass


# In[5]:


def bollingerband():
        newpop = list()
    dc = census_df.copy()
    dc.reset_index()
    count = 0
    for state in dc['STNAME'] :
        if dc.iloc[i]['STNAME'] == state :
        topCOUNTYS = dc.nlargest(3, 'COUNTY', keep='last')
        #for pop in topCOUNTYS :


    #topstates = toprows['STNAME']
    #final = topstates.values.tolist()

    #return final
    pass


# In[6]:


def adx():
    i = 11;
    count = 1;
    for i in range(len(census_df['COUNTY'])) :
        if cencus_df.iloc[i]['COUNTY'] == 0  :
            list1.append(i)
            list2.append(census_df.iloc[i]['STNAME'])
    listseries = pd.Series(list1)
    i = 0
    for i in range(len(listseries)) :
        counties = listseries.loc[i+1]-listseries.loc[i]
        list3.append(counties)
    maxi = max(listseries)
    index = listseries.index(maxi)
    i=0


    return census_df.iloc[val]['STNAME']
    pass


# In[7]:


def atr():
    stock_cp.iloc[0]['SBIN.NS'].colum
    stock_cp.drop()
    ser = pd.series()
    ser.
    pass


# In[ ]:
delta = 0
forteencount = 14;
for k in range(len(SBI.NSI), 0, -1):
          delta = SBI.Nsi[k] - SBI.nsi[k - 1]

          if delta > 0:
                        dailypos.append(delta)
                        dailyneg.append(0)
                    else:
                        dailyneg.append(delta)
                        dailypos.append(0)
                        count += 1

            if forteencount == 0:

                        avggain.append((sum(dailypos))/(14 - count))
                        avglos.append((sum(dailyneg))/count)
                        forteencount = 14
                        count = 0
                        dailypos.clear()
                        dailyneg.clear()



               forteencount -= 1


#ANSWER 7
def answer_seven():
    differences = list()
    count = 0

    for i in range(len(census_df['COUNTY'])):
        if census_df.iloc[i]['COUNTY'] != 0 :
            maxi = max(census_df.iloc[i]['POPESTIMATE2010'],census_df.iloc[i]['POPESTIMATE2011'],census_df.iloc[i]['POPESTIMATE2012'],census_df.iloc[i]['POPESTIMATE2013'],census_df.iloc[i]['POPESTIMATE2014'],census_df.iloc[i]['POPESTIMATE2015'])
            mini = min(census_df.iloc[i]['POPESTIMATE2010'],census_df.iloc[i]['POPESTIMATE2011'],census_df.iloc[i]['POPESTIMATE2012'],census_df.iloc[i]['POPESTIMATE2013'],census_df.iloc[i]['POPESTIMATE2014'],census_df.iloc[i]['POPESTIMATE2015'])
            final = abs(maxi - mini)
            differences.append(final)
        else:
            count += 1

    result = max(differences)
    reseries = pd.Series(differences)
    reseries.reset_index()
    index = reseries[reseries == result].index.values[0]
    #
    k = 0
    count_two = 0
    while k < index:
        if census_df.iloc[k]['COUNTY'] == result :
            #do something
            break
        else:
            if census_df.iloc[k]['COUNTY'] == 0 :
                count_two += 1

    y = census_df.iloc[index + count_two]['CTYNAME']
    return y
    

answer_seven()
