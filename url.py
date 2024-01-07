products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds','settee', 'divan','daybed']
keywords =  ['sale', 'bargain', 'affordable','cheap', 'low cost', 'low price', 'budget', 'inexpensive', 'economical']
keyword_list = [] # eventually, each line in this list will correspond to a keyword
for product in products:
    for word in keywords:
        keyword_list.append([product, product + ' ' + word])
        keyword_list.append([product, word + ' ' + product])
print(keyword_list[:50])

import pandas as pd

# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keyword_list)
keywords_df = keywords_df.rename(columns={0: "Ad Group",1: "Keyword"})

keywords_df.head()

keywords_df['Campaign']='SEM Sofas'
keywords_df['Criterion Type']='Exact'

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase

keywords_phrase['Criterion Type']='Phrase'

# Append the DataFrames
keywords_df_final = keywords_df.append(keywords_phrase)
keywords_df_final.sample(15)
print(keywords_df_final)

keywords_df.to_csv('keyword.csv', index=False)
# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)

pages_products = [
('http://example.com/?make=cheap&model=sofas', 'cheap sofas'),
('http://example.com/?make=affordable&model=sofas','affordable sofas'),
('http://example.com/?make=lowprice&model=sofas','lowprice sofas'),
('http://example.com/?make=convertible&model=sofas','convertible sofas'),
('http://example.com/?make=cushion&model=sofas','cushion sofas'),
    ]

ads_list = [['Campaign', 'Ad Group', 'Headline 1', 'Headline 2', 'Description', 'Final URL']]

for page, adgroup in pages_products:
    row = [
        'SEM Sofas',
        adgroup,
        adgroup +' '+'for Sale',
        'Great Prices and Options',
        '30-day Returns With Free Delivery ',
        page
    ]
    ads_list.append(row)

    row = [
        'SEM Sofas',
        adgroup,
        'Second Hand'+' '+adgroup,
        'Great Prices and Options',
        '30-day Returns With Free Delivery ',
        page
    ]
    ads_list.append(row)

ads=pd.DataFrame.from_records(ads_list,columns={'Campaign','Ad Group','Headline 1','Headline 2','Description','Final Url'})
ads=ads.loc[1:]
ads.head(7)
ads.to_csv('ads.csv', index=False)