import cld2
import pandas as pd


if __name__ == '__main__':
    #==========Baca file csv===================
    df = pd.read_csv('DataUserClean.csv', encoding='latin-1')
    #PRINT DATA
    print(df)

    for f in range(df.shape[0]):
        alltext = df['text'][f]
        print(alltext)
        isReliable, textBytesFound, details = cld2.detect(alltext)
        print('  reliable: %s' % (isReliable != 0))
        print('  textBytes: %s' % textBytesFound)
        print('  details: %s' % str(details))
