__author__ = 'Anuj'


import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')


a = list(df.columns.values)
new_col = []

for colname in a:
    new_col.append(colname.replace(' ', ''))


df.columns = new_col


mark = pd.read_csv('Market.csv')

new_df2 = pd.DataFrame(np.random.randint(4, size=(3*mark.shape[0]*df.shape[0])))

columns = ['Stat Case Volume', 'Stat Case Base Volume', "Stat Case Inc'l Volume", 'Dollar Sales',
           'Base Dollars', 'Incremental Dollars', 'Avg Price/Vol', 'Wtd Base Price per Volume',
           'Wkly Ttl Dist Points', 'ACV Wtd Dist', 'Avg Items per Store', 'Avg Wkly Volume Sales per $MM ACV',
           '% Base Volume, Any Merch', '% Base Volume, PrcRed Only', '% Base Volume, Feature &/or Display',
           'Wtd Avg % PrcRed, Any Merch', 'Wtd Avg % PrcRed, PrcRed Only', 'Wtd Avg % PrcRed, Feature &/or Display',
           'Markdown Dollars']

columns2 = []
for c in columns:
    columns2.append(c.replace(' ', ''))


for col1 in columns2:
    fill = []
    for col2 in df.columns:
        if col1 == col2[0:len(col1)]:
            fill.append(df[col2])
        else:
            continue
    fill2 = [item for sublist in fill for item in sublist]
    new_df2[str(col1)] = fill2


cc = [('Company1 '*df.shape[0]).split(), ('Competitor1 '*df.shape[0]).split(), ('Competitor2 '*df.shape[0]).split()]
cc2 = [item2 for sublist2 in cc for item2 in sublist2]
new_df2['Company'] = cc2*mark.shape[0]


regions = []
for ma in mark['Market']:
    regions.append([(ma.replace(' ', '').split('-'))[0]]*(df.shape[0]*3))
regions2 = [item4 for sublist4 in regions for item4 in sublist4]

new_df2['Market'] = regions2
# Creating the date column
new_date = []

# reading dates
df_date = pd.read_csv('dates.csv')
new_df2['Date'] = list(df_date['Date'])*(mark.shape[0]*len(cc))

new_df2 = new_df2.reindex(columns=['Date', 'Company', 'Market', 'StatCaseVolume', 'StatCaseBaseVolume', "StatCaseInc'lVolume",
                      'DollarSales', 'BaseDollars', 'IncrementalDollars', 'ACVWtdDist', 'AvgItemsperStore',
                      'AvgPrice/Vol', 'AvgWklyVolumeSalesper$MMACV', 'WklyTtlDistPoints', 'WtdAvg%PrcRed,AnyMerch',
                      'WtdAvg%PrcRed,Feature&/orDisplay', 'WtdAvg%PrcRed,PrcRedOnly', 'WtdBasePriceperVolume',
                      '%BaseVolume,AnyMerch', '%BaseVolume,Feature&/orDisplay', '%BaseVolume,PrcRedOnly',
                      'MarkdownDollars'])
print new_df2.shape
new_df2.to_csv('new_data.csv', sep=',')
