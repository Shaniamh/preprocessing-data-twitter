import pandas as pd


if __name__ == '__main__':
    #==========Baca file csv===================
    df = pd.read_csv('clean_tweet.csv', encoding='latin-1')
    #PRINT DATA
    print(df)
    df.to_csv(r'E:\1 DATA KULIAH\D4 IT B SEMESTER 7\TUGAS AKHIR\DATA PROCESSING SHANIA\USER\data_tweet_clean.csv',
              index=None, header=True)