import pandas as pd

chunk_size = 5000
batch_no = 1

for chunk in pd.read_csv('googleolaystore.csv',chunksize=chunk_size):
	chunk.to_csv('googleolaystore' + str(batch_no) + '.csv', index = False)
	batch_no +=1