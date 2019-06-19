
# NLP

- 自然语言处理的主要范畴
    - 文本朗读（Text to speech）/语音合成（Speech synthesis）
    - 语音识别（Speech recognition）
    - 中文自动分词（Chinese word segmentation）
    - 词性标注（Part-of-speech tagging）
    - 句法分析（Parsing）
    - 自然语言生成（Natural language generation）
    - 文本分类（Text categorization）
    - 信息检索（Information retrieval）
    - 信息抽取（Information extraction）
    - 文字校对（Text-proofing）
    - 问答系统（Question answering）
        - 给一句人类语言的问句，决定其答案。 典型问题有特定答案 (像是加拿大的首都叫什么?)，但也考虑些开放式问句(像是人生的意义是是什么?)
    - 机器翻译（Machine translation）
        - 将某种人类语言自动翻译至另一种语言
    - 自动摘要（Automatic summarization）
        - 产生一段文字的大意，通常用于提供已知领域的文章摘要，例如产生报纸上某篇文章之摘要
    - 文字蕴涵（Textual entailment）
    - 命名实体识别（Named entity recognition）
    
    
- `NLTK` - 自然语言工具包
- `nltk.download()` - 下载相关数据
- `nltk.download(path)` - 离线选取数据位置

### 1. 分词

    import nltk.tokenize as tk
    tk.sent_tokenize(文本)->句子列表
    tk.word_tokenize(文本)->单词列表   -\
    分词器 = tk.WordPunctTokenizer()   > 略有不同
    分词器.tokenize(文本)->单词列表     -/


```python
# tkn.py
import nltk.tokenize as tk

doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."

print(doc)
```

    Are you curious about tokenization? Let's see how it works! We need to analyze a couple of sentences with punctuations to see it in action.



```python
tokens = tk.sent_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
```

     1 Are you curious about tokenization?
     2 Let's see how it works!
     3 We need to analyze a couple of sentences with punctuations to see it in action.



```python
tokens = tk.word_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
```

     1 Are
     2 you
     3 curious
     4 about
     5 tokenization
     6 ?
     7 Let
     8 's
     9 see
    10 how
    11 it
    12 works
    13 !
    14 We
    15 need
    16 to
    17 analyze
    18 a
    19 couple
    20 of
    21 sentences
    22 with
    23 punctuations
    24 to
    25 see
    26 it
    27 in
    28 action
    29 .



```python
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
```

     1 Are
     2 you
     3 curious
     4 about
     5 tokenization
     6 ?
     7 Let
     8 '
     9 s
    10 see
    11 how
    12 it
    13 works
    14 !
    15 We
    16 need
    17 to
    18 analyze
    19 a
    20 couple
    21 of
    22 sentences
    23 with
    24 punctuations
    25 to
    26 see
    27 it
    28 in
    29 action
    30 .


### 2. 词干

    import nltk.stem.porter as pt
    pt.PorterStemmer() -> 波特词干提取器，偏宽松

    import nltk.stem.lancaster as lc
    lc.LancasterStemmer() -> 朗卡斯特词干提取器，偏严格

    import nltk.stem.snowball as sb
    sb.SnowballStemmer() -> 思诺博词干提取器，偏中庸

    词干提取器.stem(单词)->词干


```python
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']

pt_stemmer = pt.PorterStemmer()
lc_stemmer = lc.LancasterStemmer()
sb_stemmer = sb.SnowballStemmer('english')

for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print('%8s %8s %8s %8s' % (word, pt_stem, lc_stem, sb_stem))
```

       table     tabl     tabl     tabl
    probably  probabl     prob  probabl
      wolves     wolv     wolv     wolv
     playing     play     play     play
          is       is       is       is
         dog      dog      dog      dog
         the      the      the      the
     beaches    beach    beach    beach
    grounded   ground   ground   ground
      dreamt   dreamt   dreamt   dreamt
    envision    envis    envid    envis


### 3. 原型

- 名词：复数->单数
- 动词：分词->原型


```python
import nltk.stem as ns

lemmatizer = ns.WordNetLemmatizer()

for word in words:
    n_lemma = lemmatizer.lemmatize(word, pos='n')  # 按照名次还原， 动词不受影响
    v_lemma = lemmatizer.lemmatize(word, pos='v')  # 按照动词还原，名次不受影响
    print('%8s %8s %8s' % (word, n_lemma, v_lemma))
```

       table    table    table
    probably probably probably
      wolves     wolf   wolves
     playing  playing     play
          is       is       be
         dog      dog      dog
         the      the      the
     beaches    beach    beach
    grounded grounded   ground
      dreamt   dreamt    dream
    envision envision envision


### 4. 词袋

The brown dog is running. The black dog is in the black room. Running in the room is forbidden.

1 The brown dog is running

2 The black dog is in the black room

3 Running in the room is forbidden

       the  brown       dog   is   running     black   in    room    forbidden
    1   1      1         1    1      1            0     0     0          0
    2   1      0         1    1      0            2     1     1          0
    3   1      0         0    1      1            0     1     1          1


```python
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
```

    The brown dog is running. The black dog is in the black room. Running in the room is forbidden.



```python
sentences = tk.sent_tokenize(doc)
print(sentences)
```

    ['The brown dog is running.', 'The black dog is in the black room.', 'Running in the room is forbidden.']



```python
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
```

    [[0 1 1 0 0 1 0 1 1]
     [2 0 1 0 1 1 1 0 2]
     [0 0 0 1 1 1 1 1 1]]
    ['black', 'brown', 'dog', 'forbidden', 'in', 'is', 'room', 'running', 'the']


### 5. 词频
       apple
    1 5/8
    2 10/100
    词袋矩阵的归一化。


```python
import sklearn.preprocessing as sp
tf = sp.normalize(bow, norm='l1')
print(tf)
```

    [[0.         0.2        0.2        0.         0.         0.2
      0.         0.2        0.2       ]
     [0.25       0.         0.125      0.         0.125      0.125
      0.125      0.         0.25      ]
     [0.         0.         0.         0.16666667 0.16666667 0.16666667
      0.16666667 0.16666667 0.16666667]]


### 6. 文档频率

$$文档频率=\frac{含有某个单词的样本数}{总样本数}$$

### 7. 逆文档频率
$$逆文档=\frac{总样本数}{含有某个单词的样本数}$$

### 8. 词频-逆文档频率(TF-IDF)

词频矩阵中的每一个元素乘以相应单词的逆文档频率，其值越大说明该词对样本语义的贡献越大，根据每个词的贡献力度，构建学习模型。


```python
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
print(tfidf)
```

    [[0.         0.59188659 0.45014501 0.         0.         0.34957775
      0.         0.45014501 0.34957775]
     [0.73130492 0.         0.27808812 0.         0.27808812 0.21596023
      0.27808812 0.         0.43192047]
     [0.         0.         0.         0.53972482 0.41047463 0.31877017
      0.41047463 0.41047463 0.31877017]]


### 9.文本分类(主题识别)


```python
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb

train = sd.load_files('../data/20news', encoding='latin1', shuffle=True, random_state=7)
train_data = train.data
train_y = train.target
categories = train.target_names
print(categories)
```

    ['misc.forsale', 'rec.motorcycles', 'rec.sport.baseball', 'sci.crypt', 'sci.space']



```python
cv = ft.CountVectorizer()  # 创建词袋
train_bow = cv.fit_transform(train_data)
tt = ft.TfidfTransformer()
train_x = tt.fit_transform(train_bow)
model = nb.MultinomialNB()
model.fit(train_x, train_y)

test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
test_bow = cv.transform(test_data)
test_x = tt.transform(test_bow)
pred_test_y = model.predict(test_x)

for sentence, index in zip(test_data, pred_test_y):
    print(sentence, '->', categories[index])
```

    The curveballs of right handed pitchers tend to curve to the left -> rec.sport.baseball
    Caesar cipher is an ancient form of encryption -> sci.crypt
    This two-wheeler is really good on slippery roads -> rec.motorcycles


### 10. 性别识别


```python
import random
import numpy as np
import nltk.corpus as nc  # 语料库
import nltk.classify as cf

male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')
models, acs = [], []

for n_letters in range(1, 6):
    data = []
    for male_name in male_names:
        feature = {'feature': male_name[
            -n_letters:].lower()}
        data.append((feature, 'male'))
    for female_name in female_names:
        feature = {'feature': female_name[
            -n_letters:].lower()}
        data.append((feature, 'female'))
    random.seed(7)
    random.shuffle(data)
    train_data = data[:int(len(data) / 2)]
    test_data = data[int(len(data) / 2):]
    model = cf.NaiveBayesClassifier.train(
        train_data)
    ac = cf.accuracy(model, test_data)
    models.append(model)
    acs.append(ac)
best_index = np.array(acs).argmax()
best_letters = best_index + 1
best_model = models[best_index]
best_ac = acs[best_index]
print(best_letters, best_ac)
names, genders = [
    'Leonardo', 'Amy', 'Sam', 'Tom', 'Katherine',
    'Taylor', 'Susanne'], []
for name in names:
    feature = {'feature': name[
        -best_letters:].lower()}
    gender = best_model.classify(feature)
    genders.append(gender)
for name, gender in zip(names, genders):
    print(name, '->', gender)
```

    2 0.7781973816717019
    Leonardo -> male
    Amy -> female
    Sam -> male
    Tom -> male
    Katherine -> female
    Taylor -> male
    Susanne -> female


### 11. 情感分析


```python
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu

pdata = []
fileids = nc.movie_reviews.fileids('pos')  # 积极的
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True
    pdata.append((feature, 'POSITIVE'))
    
ndata = []
fileids = nc.movie_reviews.fileids('neg')  # 消极的
for fileid in fileids:
    feature = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        feature[word] = True
    ndata.append((feature, 'NEGATIVE'))
    
pnumb, nnumb = int(0.8 * len(pdata)), int(0.8 * len(ndata))  # 设定分区比率
train_data = pdata[:pnumb] + ndata[:nnumb]  # 训练集
test_data = pdata[pnumb:] + ndata[nnumb:]  # 测试集
model = cf.NaiveBayesClassifier.train(train_data)  # 训练模型
ac = cu.accuracy(model, test_data)  # 准确率
print(ac)
tops = model.most_informative_features()  # 最重要的词
for top in tops[:10]:  # 去前十个
    print(top[0])
```

    0.735
    outstanding
    insulting
    vulnerable
    ludicrous
    uninvolving
    avoids
    astounding
    fascination
    symbol
    seagal



```python
reviews = ['It is an amazing movie.',
           'This is a dull movie. I would never recommend it to anyone.',
           'The cinematography is pretty great in this movie.',
           'The direction was terrible and the story was all over the place.']

sents, probs = [], []

for review in reviews:
    feature = {}
    words = review.split()
    for word in words:
        feature[word] = True
    pcls = model.prob_classify(feature)
    sent = pcls.max()
    prob = pcls.prob(sent)
    sents.append(sent)
    probs.append(prob)
    
for review, sent, prob in zip(reviews, sents, probs):
    print(review, '->', sent, '%.2f' % prob)
```

    It is an amazing movie. -> POSITIVE 0.63
    This is a dull movie. I would never recommend it to anyone. -> NEGATIVE 0.77
    The cinematography is pretty great in this movie. -> POSITIVE 0.69
    The direction was terrible and the story was all over the place. -> NEGATIVE 0.67


### 12. 主题抽取(无监督)


```python
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc


doc = []
with open('../data/topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
        
tokenizer = tk.RegexpTokenizer(r'\w+')
stopwords = nc.stopwords.words('english')
stemmer = sb.SnowballStemmer('english')
lines_tokens = []

for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)
    
dic = gc.Dictionary(lines_tokens)
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)
n_topics = 2
model = gm.LdaModel(bow, num_topics=n_topics, id2word=dic, passes=25)
topics = model.print_topics(num_topics=n_topics, num_words=4)
print(topics)
```

    [(0, '0.036*"spaghetti" + 0.027*"made" + 0.020*"like" + 0.020*"wheat"'), (1, '0.025*"cryptographi" + 0.025*"spaghetti" + 0.018*"italian" + 0.018*"practic"')]

