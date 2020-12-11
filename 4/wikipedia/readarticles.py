import os

from joblib import load
from tqdm import tqdm

outputFilePath = "storage/text_articles"
filePath = "storage/articles"


def createTxtFiles():
    if os.path.isdir(outputFilePath) is False:
        os.mkdir(outputFilePath)

    files = os.listdir(filePath)

    for file in tqdm(files):
        article = load(os.path.join(filePath, file))
        with open(os.path.join(outputFilePath, file + '.txt'), 'w') as f:
            f.write(article)
            f.close()
        # print(f"{file} written")


def createTxtWithAllWords():
    allTxtFiles = os.listdir(outputFilePath)
    wordDict = dict()
    ignoreList = [' ', '-', '.', '', '\n', '·', '/', '‏‏‎U+0020‎‎‎‎‎']

    for file in tqdm(allTxtFiles):
        # print(f"reading {file}")
        article = open(os.path.join(outputFilePath, file), 'r')
        lines = article.readlines()

        for line in lines:
            words = line.replace(".", '').replace("\n", '').replace('=', ' ').split(" ")
            for word in words:
                if word in ignoreList:
                    continue
                if wordDict.__contains__(word):
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1

    print(f"{len(wordDict)} words found")
    wordDict = {key: value for key, value in sorted(wordDict.items(), key=lambda item: item[1], reverse=True)}

    count = 0
    with open("stop_words11.txt", "w") as file:
        for key, value in wordDict.items():
            count += 1
            if count > 100:
                break
            print(f"{key}  -->   {value}")
            file.write(str(key) + "\n")


createTxtWithAllWords()
# 21151 unique words found
# आहे  -->   2080
# या  -->   1551
# व  -->   1338
# आणि  -->   1259
# हे  -->   967
# आहेत  -->   785
# हा  -->   781
# एक  -->   660
# इस  -->   650
# ते  -->   579
# ही  -->   531
# त्यांनी  -->   442
# होते  -->   433
# केले  -->   370
# मध्ये  -->   350
# भारतीय  -->   334
# मराठी  -->   297
# ह्या  -->   296
# साहित्य  -->   294
# केली  -->   293
# असे  -->   292
# लेणी  -->   288
# येथे  -->   287
# विमानतळ•  -->   273
# म्हणून  -->   262
# असून  -->   251
# अनेक  -->   246
# साली  -->   241
# होता  -->   237
# यांनी  -->   233
# जाते  -->   223
# दोन  -->   202
# त्या  -->   200
# झाले  -->   194
# तर  -->   189
# करून  -->   186
# तसेच  -->   184
# केला  -->   183
# तो  -->   181
# नाही  -->   180
# काही  -->   177
# होती  -->   170
# राष्ट्रीय  -->   170
# यांच्या  -->   166
# आले  -->   164
# क्रिकेट  -->   158
# झाला  -->   156
# च्या  -->   154
# त्यांना  -->   151
# विमानतळ  -->   148
# किंवा  -->   144
# करण्यात  -->   141
# सर्व  -->   141
# खेळाडू  -->   141
# दक्षिण  -->   141
# झाली  -->   140
# संगीत  -->   140
# गेले  -->   138
# एका  -->   138
# त्याने  -->   137
# त्यांच्या  -->   134
# चित्रपट  -->   131
# अजय  -->   126
# सुरू  -->   124
# अशा  -->   124
# येथील  -->   122
# ती  -->   118
# तीन  -->   115
# सर्वात  -->   113
# असलेल्या  -->   112
# काळात  -->   111
# प्रसिद्ध  -->   110
# त्यांची  -->   109
# असते  -->   107
# काम  -->   107
# आंतरराष्ट्रीय  -->   102
# जातो  -->   102
# अजिंठा  -->   102
# अध्यक्ष  -->   102
# नंतर  -->   101
# पण  -->   101
# भगवान  -->   101
# येते  -->   100
# नाव  -->   99
# यांचा  -->   99
# इतर  -->   98
# आली  -->   96
# विविध  -->   96
# त्यानंतर  -->   95
# रोजी  -->   95
# उपलब्ध  -->   95
# दिला  -->   95
# त्यांचे  -->   94
# अशी  -->   94
# आपल्या  -->   93
# श्री  -->   93
# किमी  -->   92
# मुख्य  -->   90
# शहर  -->   88
# असलेले  -->   88
