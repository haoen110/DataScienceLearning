
# 推荐引擎

### 1.欧氏距离分数

$$欧氏距离分数 = \frac{1}{1+欧氏距离}$$

$$构建距离矩阵$$

```json
/ 不同人看过的电影以及评分
{
    "John Carson": 
    {
        "Inception": 2.5,
        "Pulp Fiction": 3.5,
        "Anger Management": 3.0,
        "Fracture": 3.5,
        "Serendipity": 2.5,
        "Jerry Maguire": 3.0
    },
    "Michelle Peterson": 
    {
        "Inception": 3.0,
        "Pulp Fiction": 3.5,
        "Anger Management": 1.5,
        "Fracture": 5.0,
        "Jerry Maguire": 3.0,
        "Serendipity": 3.5 
    },
    "William Reynolds": 
    {
        "Inception": 2.5,
        "Pulp Fiction": 3.0,
        "Fracture": 3.5,
        "Jerry Maguire": 4.0
    },
    "Jillian Hobart": 
    {
        "Pulp Fiction": 3.5,
        "Anger Management": 3.0,
        "Jerry Maguire": 4.5,
        "Fracture": 4.0,
        "Serendipity": 2.5 
    },
    "Melissa Jones": 
    {
        "Inception": 3.0,
        "Pulp Fiction": 4.0,
        "Anger Management": 2.0,
        "Fracture": 3.0,
        "Jerry Maguire": 3.0,
        "Serendipity": 2.0
    },
    "Alex Roberts": 
    {
       "Inception": 3.0,
       "Pulp Fiction": 4.0,
       "Jerry Maguire": 3.0,
       "Fracture": 5.0,
       "Serendipity": 3.5
    },
    "Michael Henry": 
    {
       "Pulp Fiction": 4.5,
       "Serendipity": 1.0,
       "Fracture": 4.0
    }
}
```


```python
import json
import numpy as np

with open('../data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())

print(ratings)
print('\n',ratings.keys())
```

    {'John Carson': {'Inception': 2.5, 'Pulp Fiction': 3.5, 'Anger Management': 3.0, 'Fracture': 3.5, 'Serendipity': 2.5, 'Jerry Maguire': 3.0}, 'Michelle Peterson': {'Inception': 3.0, 'Pulp Fiction': 3.5, 'Anger Management': 1.5, 'Fracture': 5.0, 'Jerry Maguire': 3.0, 'Serendipity': 3.5}, 'William Reynolds': {'Inception': 2.5, 'Pulp Fiction': 3.0, 'Fracture': 3.5, 'Jerry Maguire': 4.0}, 'Jillian Hobart': {'Pulp Fiction': 3.5, 'Anger Management': 3.0, 'Jerry Maguire': 4.5, 'Fracture': 4.0, 'Serendipity': 2.5}, 'Melissa Jones': {'Inception': 3.0, 'Pulp Fiction': 4.0, 'Anger Management': 2.0, 'Fracture': 3.0, 'Jerry Maguire': 3.0, 'Serendipity': 2.0}, 'Alex Roberts': {'Inception': 3.0, 'Pulp Fiction': 4.0, 'Jerry Maguire': 3.0, 'Fracture': 5.0, 'Serendipity': 3.5}, 'Michael Henry': {'Pulp Fiction': 4.5, 'Serendipity': 1.0, 'Fracture': 4.0}}
    
     dict_keys(['John Carson', 'Michelle Peterson', 'William Reynolds', 'Jillian Hobart', 'Melissa Jones', 'Alex Roberts', 'Michael Henry'])



```python
users, scmat = list(ratings.keys()), []

for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()  # 共同看过的电影的集合
        for movie in ratings[user1]:  # 拿到user1所看过的电影
            if movie in ratings[user2]:  # 判断user2是否看过该电影
                movies.add(movie)  # 是的话追加到集合中
        if len(movies) == 0:
            score = 0  # 如果没有共同看过的电影，则为零分
        else:  # 如果有共同看过的电影
            x, y = [], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
            score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))
        scrow.append(score)  # 得到user1的一整行
    scmat.append(scrow)  # 将这一行追加到scmat中
    
users = np.array(users)
scmat = np.array(scmat)

for scrow in scmat:
    print(' '.join('{:>5.2f}'.format(score) for score in scrow))
```

     1.00  0.29  0.47  0.39  0.41  0.34  0.35
     0.29  1.00  0.34  0.28  0.28  0.67  0.26
     0.47  0.34  1.00  0.54  0.39  0.32  0.39
     0.39  0.28  0.54  1.00  0.31  0.32  0.36
     0.41  0.28  0.39  0.31  1.00  0.29  0.40
     0.34  0.67  0.32  0.32  0.29  1.00  0.27
     0.35  0.26  0.39  0.36  0.40  0.27  1.00


### 2. 皮氏距离分数

$$相关性矩阵$$

$$\\ \begin{pmatrix}1 & 相关系数 \\
相关系数 & 1\end{pmatrix}$$

$$相关性系数 = \frac{协方差}{标准差之积}$$

$$-1 <------- 0 -------> 1 $$


```python
users, scmat = list(ratings.keys()), []

for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()  # 共同看过的电影的集合
        for movie in ratings[user1]:  # 拿到user1所看过的电影
            if movie in ratings[user2]:  # 判断user2是否看过该电影
                movies.add(movie)  # 是的话追加到集合中
        if len(movies) == 0:
            score = 0  # 如果没有共同看过的电影，则为零分
        else:  # 如果有共同看过的电影
            x, y = [], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
            score = np.corrcoef(x, y)[0, 1]  # 皮尔逊相关系数
        scrow.append(score)  # 得到user1的一整行
    scmat.append(scrow)  # 将这一行追加到scmat中
    
users = np.array(users)
scmat = np.array(scmat)

for scrow in scmat:
    print(' '.join('{:>5.2f}'.format(score) for score in scrow))
```

     1.00  0.40  0.40  0.57  0.59  0.75  0.99
     0.40  1.00  0.20  0.31  0.41  0.96  0.38
     0.40  0.20  1.00  1.00 -0.26  0.13 -1.00
     0.57  0.31  1.00  1.00  0.57  0.03  0.89
     0.59  0.41 -0.26  0.57  1.00  0.21  0.92
     0.75  0.96  0.13  0.03  0.21  1.00  0.66
     0.99  0.38 -1.00  0.89  0.92  0.66  1.00


### 3. 按照相似度从高到低排列每个用户的相似用户


```python
for i, user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i, sorted_indices]
    print(user, similar_users, similar_scores, sep='\n')
```

    John Carson
    ['Michael Henry' 'Alex Roberts' 'Melissa Jones' 'Jillian Hobart'
     'William Reynolds' 'Michelle Peterson']
    [0.99124071 0.74701788 0.59408853 0.56694671 0.40451992 0.39605902]
    Michelle Peterson
    ['Alex Roberts' 'Melissa Jones' 'John Carson' 'Michael Henry'
     'Jillian Hobart' 'William Reynolds']
    [0.96379568 0.41176471 0.39605902 0.38124643 0.31497039 0.2045983 ]
    William Reynolds
    ['Jillian Hobart' 'John Carson' 'Michelle Peterson' 'Alex Roberts'
     'Melissa Jones' 'Michael Henry']
    [ 1.          0.40451992  0.2045983   0.13483997 -0.25819889 -1.        ]
    Jillian Hobart
    ['William Reynolds' 'Michael Henry' 'Melissa Jones' 'John Carson'
     'Michelle Peterson' 'Alex Roberts']
    [1.         0.89340515 0.56694671 0.56694671 0.31497039 0.02857143]
    Melissa Jones
    ['Michael Henry' 'John Carson' 'Jillian Hobart' 'Michelle Peterson'
     'Alex Roberts' 'William Reynolds']
    [ 0.92447345  0.59408853  0.56694671  0.41176471  0.21128856 -0.25819889]
    Alex Roberts
    ['Michelle Peterson' 'John Carson' 'Michael Henry' 'Melissa Jones'
     'William Reynolds' 'Jillian Hobart']
    [0.96379568 0.74701788 0.66284898 0.21128856 0.13483997 0.02857143]
    Michael Henry
    ['John Carson' 'Melissa Jones' 'Jillian Hobart' 'Alex Roberts'
     'Michelle Peterson' 'William Reynolds']
    [ 0.99124071  0.92447345  0.89340515  0.66284898  0.38124643 -1.        ]


### 4. 生成推荐清单

- 考虑因素

    - 推荐度

    - 皮氏距离分数>0的用户

    - 打分高低

    - 相似度权重


```python
for i, user in enumerate(users):
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i, sorted_indices]
    positive_mask = similar_scores > 0
    similar_users = similar_users[positive_mask]
    similar_scores = similar_scores[positive_mask]
    score_sums, weight_sums = {}, {}
    for similar_user, similar_score in zip(similar_users, similar_scores):
        for movie, score in ratings[similar_user].items():
            if movie not in ratings[user].keys():
                if movie not in score_sums.keys():
                    score_sums[movie] = 0
                score_sums[movie] += score * similar_score
                if movie not in weight_sums.keys():
                    weight_sums[movie] = 0
                weight_sums[movie] += similar_score
    movie_ranks = {}
    
    for movie, score_sum in score_sums.items():
        movie_ranks[movie] = score_sum / weight_sums[movie]
    sorted_indices = np.array(list(movie_ranks.values())).argsort()[::-1]
    recomms = np.array(list(movie_ranks.keys()))[sorted_indices]
    print(user, recomms, sep='\n')
```

    John Carson
    []
    Michelle Peterson
    []
    William Reynolds
    ['Anger Management' 'Serendipity']
    Jillian Hobart
    ['Inception']
    Melissa Jones
    []
    Alex Roberts
    ['Anger Management']
    Michael Henry
    ['Jerry Maguire' 'Inception' 'Anger Management']

