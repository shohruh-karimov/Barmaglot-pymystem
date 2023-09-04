import pymorphy2
morph = pymorphy2.MorphAnalyzer()

i = 0
with open('keywords','r',encoding= 'UTF-8') as f:

    for line in f:
        line = line.strip().split('\t')
        word = line[0]
        # wordCount = line[1]
        morph_analyze = morph.parse(word)
        print(morph_analyze[0].normal_form)
        print(word,morph_analyze[0])
        if i > 5:
            break
        i +=1


# a = morph.parse('и хрюкотали зелюки как мюмзики в мове')
# print(a)

