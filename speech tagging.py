import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
x=set(stopwords.words("english"))
sm = "Iam hima from wayand now Iam pursuing my postgraduation in mca ,in my family apart my parents I have a sister"
token =nltk.sent_tokenize(sm)
print(token)
for i in token:
    wcc=nltk.word_tokenize(i)
    wcc=[w for w in wcc if not w in x]
    tag=nltk.pos_tag(wcc)
    print(tag)
