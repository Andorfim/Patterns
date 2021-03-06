# -*- coding: utf-8 -*-
"""Шип2.0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q4TGO3ZgNlHP4jy7QJajUCgcWOhPfRsp
"""

!pip install yfinance

import yfinance as yf
from datetime import datetime
import pandas as pd
datetime().strftime('%Y-%m-%d')
i = 0
k = list = []
t = list = ["MSFT"]

#a = yf.download(t[i], start="", end="")

from datetime import datetime
d1 = datetime.today().strftime('%Y-%m-%d')



import yfinance as yf
import pandas as pd
import arrow













!pip install arrow









from datetime import datetime
datetime.today().strftime('%Y-%m-%d')













import yfinance as yf
import arrow 
t = list = ["A","AA","AAL","AAP","AAPL","ABBV","ABT","ADBE","ADI","ADM","ADP","ADS","ADSK","AEE","AES",
"AFL","AIG","AIV","AIZ","AJG","AKAM","ALB","ALGN","ALK","ALL","ALXN","AMAT","AMD","AME","AMG","AMGN",
"AMP","AMT","AMZN","AN","ANSS","ANTM","APA","APD","APH","ARE","ARNC","ATVI","AVB",
"AVGO","AVY","AXP","AYI","AZO",
"BA","BAC","BAX","BBBY","BBY","BDX","BEN","BHF",
"BIIB","BK","BKNG","BLK","BLL","BMY","BRK-B","BSX","BWA","BXP",
"C","CAG","CAH","CAT","CBOE",
"CBRE","CCI","CERN","CF","CFG","CHD","CHK","CHRW","CHTR","CI","CINF","CL","CLF","CLX",
"CMA","CMCSA","CME","CMG","CMI","CMS","CNC","CNP","COF","COG","COO","COP","COST","COTY","CPB",
"CRM","CSCO","CTAS","CTSH","CTXS","CVS","CVX",
"DAL","DE","DFS","DG","DGX","DHI","DHR","DIS",
"DISCA","DISCK","DLR","DLTR","DNB","DRI","DTE","DVA","DVN","DXC",
"EA","EBAY","ECL","ED",
"EFX","EIX","EL","EMN","EMR","EOG","EQIX","EQT","ES",
"F","FAST","FB","FBHS","FCX","FDX","FE","FFIV","FIS","FISV","FITB",
"FL","FLR","FLS","FMC","FOX","FOXA","FSLR","FTV","GD","GE","GILD","GIS","GLW",
"GM","GOOG","GOOGL","GPC","GPN","GPS","GS","GT","GWW","HAL","HAS","HBAN","HBI","HCA","HD",
"HES","HIG","HLT","HOG","HOLX","HON","HP","HPE","HPQ","HRB","HRL","HSIC","HST","HSY","HUM",
"IBM","ICE","IDXX","IFF","ILMN","INCY","INTC","INTU","IP","IPG","IRM","ISRG","IT","ITW","JBHT","JNJ","JNPR","JPM","JWN","K","KEY","KHC","KIM","KLAC","KMB","KMI","KMX","KO","KR","KSU","L",
"LB","LEG","LEN","LEN-B","LH","LKQ","LLY","LMT","LNT","LOW","LRCX","LUV","M","MA",
"MAA","MAC","MAR","MAS","MAT","MCD","MCHP","MCK","MCO","MDLZ","MET","MHK","MKC","MLM","MMC","MMM",
"MNST","MO","MOS","MPC","MRK","MRO","MS","MSFT","MSI","MTB","MTD","MU","MUR","NAVI","NDAQ",
"NEE","NEM","NFLX","NKE","NOC","NOV","NRG","NSC","NTAP","NTRS","NUE","NVDA","NWL","NWS","NWSA",
"O","OI","OKE","OMC","ORCL","ORLY","OXY","PANW","PBCT","PBI","PCAR","PCG","PDCO","PEG","PEP","PFE","PFG",
"PG","PGR","PH","PHM","PKI","PLD","PM","PNC","PPG","PPL","PRU","PSA","PSX","PVH","PWR","PXD","PYPL","QCOM",
"QRVO","R","REG","REGN","RF","RHI","RJF","RL","ROK","ROP","ROST","RRC","RSG","SBUX","SCHW",
"SEE","SHW","SJM","SLG","SNA","SNPS","SO","SOHU","SPG","SPGI","SPLK","SQ","SRCL","SRE","STT","STZ","SWK",
"SWKS","SWN","SYF","SYK","SYY","T","TAP","TDC","TDG","TGNA","TGT","TJX","TMO","TPR","TRIP",
"TROW","TRV","TSCO","TSLA","TSN","TWTR","TXN","TXT","UA","UAA","UAL","UDR","UHS","ULTA","UNH","UNM",
"UNP","UPS","URBN","URI","USB","V", "VFC","VLO","VMC","VNO","VRSK","VRSN","VRTX","VTR","VZ","WAT",
"WBA","WDC","WEC","WELL","WFC","WHR","WM","WMB","WMT","WRK","WU","WY","WYNN","XEC","XEL","XLNX","XOM","XRAY","XRX","XYL","YUM","ZBH","ZION","ZTS"]
k = list = []
i = 0
while i <=421:
  d = arrow.now().format("YYYY-MM-DD") #Сегодняшняя дата
  a = yf.download(t[i], start="2021-07-01", end=d)
  
  close = a["Close"]
  high = a["High"]
  low = a["Low"]

  close2 = close[len(a)-2]
  high2 = high[len(a)-2]
  low2 = low[len(a)-2]

  close1 = close[len(a)-3]
  high1 = high[len(a)-3]
  low1 = low[len(a)-3]

  close0 = close[len(a)-4]
  high0 = high[len(a)-4]
  low0 = low[len(a)-4]

  k1 = high0-low0 #Длина первого тика
  k2 = (high1-low1)/(k1) #Отношение длин второго и первого тика 
  k3 = (high2-low2)/(k1) #Отношение длин третьего и первого тика
  k4 = (high2-close2)/(high2-low2) #Закрытие вблизи верхней границы
  #k5 = (high2-low2)/(high1+low1) #Третий тик больше второго
  print(k1, k2, k3, k4)
  if k2 >=1  and k3 >= 1.02 and k4 <=0.5:
    print(t[i])
    k[len(k):] = [t[i]]
    i = i + 1
  else:
    print(t[i])
    print(k)
    i = i + 1
print(k)





close[len(a)-2]







close[len(a)-3]









