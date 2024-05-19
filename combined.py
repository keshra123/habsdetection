import pandas as pd
df = pd.read_csv('instagram.csv',index_col=0)
df['source type'] = "instagram"
df1 = pd.read_csv('googlenews2.csv',index_col=0)
df1['source type'] = "google"
df2 = pd.read_csv('reddit.csv',index_col=0)
df2['source type'] = "reddit"
frames = [df,df1,df2]
results = pd.concat(frames)
#results.drop()
results.reset_index(inplace=True, drop=True)
#results.drop(['index'], axis=1)
results.to_csv('combined.csv')
print(results)
