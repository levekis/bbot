import pandas as pd

# load DataFrame
column_names = ['Aggregate tradeId','Price', 'Quantity', 'First tradeId', 'Last tradeId', 'Timestamp', 'Buyer','Best Price']
btc_df = pd.read_csv('ALGOBTC-aggTrades-2021-10.csv', index_col=5, header=None, names=column_names)


#btc_df.index = pd.to_datetime(btc_df.index, unit='ms')
#print(btc_df.at['2021-10-31 23:59:58.790','Price'])


print(btc_df)
# calculate 20 moving average using Pandas
#btc_df['20sma'] = btc_df.Quantity.rolling(2000).mean()
#print(btc_df.tail(50))