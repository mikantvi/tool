import pandas_datareader.data as pdr
start="1949/9/30"
end="2016/9/30"
N225=pdr.DataReader("NIKKEI225",'fred',start,end)
N225.head(1)
