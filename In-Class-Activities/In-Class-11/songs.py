def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def print_hist(h):
    for c in h:
        print(c, h[c])


she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

                 'you', 'think', "you've", 'lost', 'your', 'love',
                 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
                 "it's", 'you', "she's", 'thinking', 'of',
                 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'she', 'said', 'you', 'hurt', 'her', 'so',
                 'she', 'almost', 'lost', 'her', 'mind',
                 'and', 'now', 'she', 'says', 'she', 'knows',
                 "you're", 'not', 'the', 'hurting', 'kind',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',

                 'you', 'know', "it's", 'up', 'to', 'you',
                 'i', 'think', "it's", 'only', 'fair',
                 'pride', 'can', 'hurt', 'you', 'too',
                 'pologize', 'to', 'her',

                 'Because', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'Yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'yeah', 'yeah', 'yeah',
                 'yeah', 'yeah', 'yeah', 'yeah'
                 ]

beatles = histogram(she_loves_you)
print_hist(beatles)