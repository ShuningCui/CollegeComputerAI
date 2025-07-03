# 14. 输入一系列英文单词，单词之间用空格隔开。
# 统计输入过哪些单词以及各单词出现的次数，
# 统计时区分大小写字母，
# 最后按单词的字典顺序输出单词和出现次数的对照表。


words = input("Enter a series of English words separated by spaces: ").split()
words_dict = {}
for word in words:
    if word in words_dict:
        words_dict[word] += 1
    else:
        words_dict[word] = 1
for word in sorted(words_dict):
    print(f"{word}: {words_dict[word]}")
