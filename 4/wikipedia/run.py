import os
from tqdm import tqdm

inputDirs = os.listdir("storage/stop_words_removed")
outputDir = "storage/stop_words_removed"


def removeStopWords():
    # 86256 words removed
    stopWords = []
    with open("stop_words.txt") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            stopWords.append(line)

    removed = 0
    for file in tqdm(inputDirs):
        cleanedLines = []
        with open(os.path.join("storage/stop_words_removed", file), "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(" ")
                for word in words:
                    for stop in stopWords:
                        if word.__contains__(stop):
                            removed += 1
                            # print(f"removed {word} from {file}")
                            line = line.replace(word, "")
                            line = line.replace("\n", "")
                            line = line.replace("  ", "")
                cleanedLines.append(line)

        with open(os.path.join(outputDir, file), "w") as f:
            for line in cleanedLines:
                line = line.replace("\n", "")
                f.write(line)
            f.close()
        # print(f"{file} written")
    print(f"{removed} words removed")


def stemming():
    # 7901 stemming done
    stemmers = []
    with open("stemmers.txt", "r") as stem:
        lines = stem.readlines()
        for line in lines:
            line = line.replace("\n", "")
            stemmers.append(line)

    removed = 0
    for file in tqdm(inputDirs):
        cleanedLines = []
        with open(os.path.join("storage/stemms_removed", file), "r") as f:
            lines = f.readlines()
            for line in lines:
                words = line.split(" ")
                for word in words:
                    for stem in stemmers:
                        if word.__contains__(stem):
                            line = line.replace(stem, "")
                            removed += 1
                cleanedLines.append(line)

        with open(os.path.join("storage/stemms_removed", file), "w") as f:
            for line in cleanedLines:
                line = line.replace("\n", "")
                f.write(line)
            f.close()
    print(f"{removed} stemmers removed......")


def stats():
    dirs = os.listdir("storage/stemms_removed")
    files = 0
    lineCount = 0
    wordCount = 0
    characterCount = 0

    for file in tqdm(dirs):
        with open(os.path.join("storage/stemms_removed", file), "r") as f:
            files += 1
            lines = f.readlines()
            for line in lines:
                lineCount += 1
                words = line.split(" ")
                for word in words:
                    wordCount += 1
                    characterCount += len(word)

    print(f"{files} articles.")
    print(f"{lineCount} lines.")
    print(f"{wordCount} words.")
    print(f"{characterCount} characters.")
    # 852 articles.
    # 831 lines.
    # 43889 words.
    # 334342 characters.


stats()
# removeStopWords()
# stemming()
