#read csv file
import csv
import cld2
import glob
from DBRepository.UserAllRepository import UserAllRepository as UserAllRepo
from Model.User import User

def detectCsv(namecsv):
    f = open('realDonaldTrump_tweets.csv', 'r')
    with f:
        textUser=""
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            # print(row)
            # h = row[0]
            # print(row[0])
            # print("row" )
            # print(type(row))
            i=0
            for e in row:
                if(i==2):
                    # print(e)
                    textUser = textUser + e
                # print(type(e))
                i = i+1
                # print(type(e))
        # print(textUser)
    print("---------------------------")
    isReliable, textBytesFound, details = cld2.detect(textUser)
    print('  reliable: %s' % isReliable)
    print('  textBytes: %s' % textBytesFound)
    print('  details: %s' % str(details))
    print("---------------------------")
    if(details[0][1]=="en"):
        print("OK english")
def readFolderCSV(dir):
    csvDir = glob.glob(dir + '/*.csv');
    filenamecsv = []
    i = 0;
    for file in csvDir:
        i=i+1
        nameOfFile = file
        space = nameOfFile.find(" ")
        file = nameOfFile[54:]
        num = nameOfFile[54:space]
        nameCSV = nameOfFile[space+1:]
        name = nameCSV[:-11]
        print("{} | {} | {} | {} | file : {}" .format(i, num, nameCSV, name, file))
        filenamecsv.append(file)
        # singleCSV = csv.reader(open(file, 'r', errors='ignore'), delimiter=',')
        # for row in singleCSV:
        #     print(i)
        #     i = i + 1
            # newTweet = Tweet(None, row[1], row[2], row[5], row[9],state)
            # insertTweet(repoTweet, newTweet)
            # print("ok")
    return filenamecsv

def sampleFindOne():
    import pymongo

    uname = "x_hannahbanana_"
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["test"]
    mycol = mydb["userALL"]

    myquery = {"username": uname}

    mydoc = mycol.find(myquery)

    for x in mydoc:
        print(x)

if __name__ == '__main__':
    dir = "C:\\Users\\Nadian\\PycharmProjects\\mypython\\TweetPerUser"

    # detectCsv("f")
    #read file-file csv di dalam 1 folder untuk bisa diakses
    fileNameCSVs = []
    fileNameCSVs = readFolderCSV(dir)
    print("{} CSVs have been found".format(len(fileNameCSVs)))
    for fileName in fileNameCSVs:
        #filter aktif
        #read csv as row (membaca file cssv per barisnya)
        # f = open(fileName, 'r')
        f = open(fileName, 'r')
        with f:
            # mergetweet = mergetweet + row (menggabungkan text2 tweet untuk deteksi bahasa)
            mergetweet = ""
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                # hitung jumlah baris tweet dalam 1 csv, simpan lokal sumtweet = sumtweet+1
                # print(row)
                # h = row[0]
                # print(row[0])
                # print("row" )
                # print(type(row))
                i = 0
                for e in row:
                    if (i == 2):
                        # print(e)
                        mergetweet = mergetweet + e
                    # print(type(e))
                    i = i + 1
                    # print(type(e))
            # print(textUser)
        print("---------------------------")
        isReliable, textBytesFound, details = cld2.detect(mergetweet)
        print('  reliable: %s' % isReliable)
        print('  textBytes: %s' % textBytesFound)
        print('  details: %s' % str(details))
        print("---------------------------")
        if (details[0][1] == "en"):
            print("OK english")

            #isActiveUser = variabel simpan bolean active user/tidak (parameter jumlah tweet)
            #lang = variabel simpan language of entire tweets
            #if(sumtweet>25) cek apakah ada tweet sejumlah 25
                #jika >25 isActive = 1
            #else isActive = 0

            #ceklah languagenya
                # lang= resultLang
            # update db sumTweet= sumtweet, lang = resultLang
    #cek apakah tweetnya 75% berbahasa inggris kasih label di db
    f = open('1 x_hannahbanana__tweets.csv', 'r')
    uname = "x_hannahbanana_"
    with f:
            # mergetweet = mergetweet + row (menggabungkan text2 tweet untuk deteksi bahasa)
            mergetweet = ""
            reader = csv.reader(f, delimiter=",")
            baris = 0
            for row in reader:
                # hitung jumlah baris tweet dalam 1 csv, simpan lokal di akhir->sumtweet
                i = 0
                baris= baris+1
                # print(baris)
                # print(row)
                for e in row:
                    if (i == 2):
                        mergetweet = mergetweet + e
                    i = i + 1

            # print(textUser)
            sumtweet = (baris-2)/2
            print("total tweet user : {} ".format((baris-2)/2))
            if (sumtweet>25):
                print(i)
                isActiveUser = True
    print("---------------------------")
    isReliable, textBytesFound, details = cld2.detect(mergetweet)
    print('  reliable: %s' % isReliable)
    print('  textBytes: %s' % textBytesFound)
    print('  details: %s' % str(details))
    print("---------------------------")
    lang = details[0][1]
    if (isActiveUser):
        print("OK this user is active")
    if ((isReliable == True) & (lang == "en")):
        print("OK english")

    #mencari id data dengan username=xxx
    repoUser = UserAllRepo()
    findUser = repoUser.searchName(uname)
    objUserFind = User()
    objUserALLUpdate = User()
    for tweet in findUser:
        isSuccess = True
        tem_tweet = objUserFind.build_from_json(tweet)
        print(tweet["_id"])
        objUserALLUpdate = User( tweet["_id"], tweet["username"], tweet["date"], tweet["text"], tweet["tweet_id"], tweet["state"], isActiveUser , lang)
        repoUser.update(objUserALLUpdate)
        print()
        # tweets.append(tem_tweet)
    if not isSuccess:
        print("Belum ada di database")


    # repoUser.update(objUserUpdate)
    # update db sumTweet= sumtweet, lang = resultLang