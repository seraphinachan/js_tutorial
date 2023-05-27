import FinanceDataReader as fdr
import matplotlib.pyplot as plt
 
from matplotlib.gridspec import GridSpec
from datetime import datetime 
 
start_date = datetime(2023,5,20).strftime('%Y-%m-%d')
end_date = datetime(2023,5,27).strftime('%Y-%m-%d')
    
df = fdr.DataReader('005930', start_date, end_date) # 삼성전자 데이터
df.head()

# print(df)

# json 파일로 변환
df.to_json('stock_data.json', orient='records')
