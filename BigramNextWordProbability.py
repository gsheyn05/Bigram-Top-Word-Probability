import operator


def test_next(word1, word2,document):
    lines=open(document).readlines()

    countoc = 0
    wordli = {}

    for i in lines:

        lined = i.strip().split()
        for i2 in range(len(lined) - 2):
            i3 = i2 + 1

            if (lined[i2] == word1 and lined[i3] == word2):

                countoc = countoc + 1
                third = lined[i3 + 1]
                if third not in wordli:
                    wordli[third] = 1
                else:
                    wordli[third] += 1


    for key, value in wordli.items():
        wordli[key] = float(value / countoc)


    sortdic = sorted(wordli.items(), key=operator.itemgetter(1), reverse=True)

    return sortdic


def top_next_word(word1, word2, n):

  sortdic=test_next(word1,word2)

  stop=0
  wordli2=[]
  wordfre=[]

  for x,y in enumerate(sortdic):
    stop=stop+1
    wordli2.append(y[0])
    wordfre.append(y[1])

    if (stop==n):
      return wordli2, wordfre