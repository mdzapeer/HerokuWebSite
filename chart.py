import pandas
from alpha_vantage.cryptocurrencies import CryptoCurrencies
from bokeh.plotting import figure, show , output_file
from bokeh.embed import components

#use alphavantage method to load API format
cc = CryptoCurrencies(key='K53QQNRE6X9S2YCI', output_format='pandas')
#create data set variables for BTC for daily chart
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='USD')
#create Date column in pandas dataframe  
data["Date"]=pandas.to_datetime(data.index)
#extract last 50 entries
data1=data[-50:]
#create Bokeh object 'p', depecrated warning, need to update...
p=figure(x_axis_type='datetime', width=1000, height=300,responsive=True)
p.title.text="Candlestick Chart"

w = 12*60*60*1000 # half day in ms
#new dataframe data1 for last 50 entries
data1["Date"]=pandas.to_datetime(data1.index)

#create dataframe variables for increase or decrease for candlestick chart
increase=data1["4a. close (USD)"] > data1["1a. open (USD)"]
decrease=data1["4a. close (USD)"] < data1["1a. open (USD)"]
#the lines for the candle stick chart
p.segment(data1.Date,data1["2b. high (USD)"],data1.Date,data1["3b. low (USD)"],color="black")
#actual candles
p.vbar(data1.Date[increase],w,data1["1a. open (USD)"][increase],data1['4b. close (USD)'][increase],fill_color="green", line_color="black")
p.vbar(data1.Date[decrease],w,data1["1a. open (USD)"][decrease],data1['4b. close (USD)'][decrease],fill_color="red", line_color="black")
#get the script and div componeents for embeddnig
script1, div1 = components(p)