def high(x):
    words = x.lower().split()
    word_score = []
    
    for i in words:
        word_score.append(sum(ord(x)-ord('a') for x in i))
    
    max_score = max(word_score)
    index_word = word_score.index(max_score)

    print(words)
    print(word_score)
    print(max_score)
    print(index_word)
    print(words[index_word])
    # print(words[word_score.index(max_score)])
    

high('aa b')

# word = 'volcano'
# for i in word:
#     print(f'{i} : {ord(i)-ord("a")}')
# print(sum(ord(i)-ord("a") for x in word))