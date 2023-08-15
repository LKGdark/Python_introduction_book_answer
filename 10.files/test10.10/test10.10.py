from pathlib import Path

def count_words(path):
    """计算一个文件大概包含多少个单词"""
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry,the file {path} does not exist.")
    else:
        #计算文件大概包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('Jane Eyre - Charlotte Bronte.txt')
count_words(path)
