import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# data = {'Artist': pd.Series(['Billie Holiday', 'Jimi Hendrix', 'Miles Davis', 'SIA']),
#         'Genre': pd.Series(['Jazz', 'Rock', 'Jazz', 'Pop']),
#         'Listeners': pd.Series([1300000, 2700000, 1500000, 2000000]),
#         'Plays': pd.Series([27000000, 70000000, 48000000, 74000000])}
# df = pd.DataFrame(data)
# print(df)

titanic_df = pd.read_csv('titanic.csv')
print(titanic_df)
titanic_df.info()


# sns.catplot(
#         x="Gender",
#         hue="Survived",
#         kind="count",
#         data=titanic_df
# )
# plt.show()

# print(titanic_df.head(10))
# print(titanic_df.tail(10))

# 컬럼 Name 삭제
# titanic_df.drop(columns="Name", inplace=True)
titanic_df.info()

# titanic_df.drop(columns=['Cabin', 'Ticket', 'Embarked'], inplace=True)
# print(titanic_df.head(2))

print()
print(titanic_df[titanic_df.duplicated()])

print(titanic_df.tail(10))

titanic_df.drop(columns=['Cabin', 'Ticket', 'Embarked', 'PassengerId'], inplace=True)
titanic_df.drop_duplicates(inplace=True)
# print(titanic_df[titanic_df.duplicated()])
print(titanic_df.tail(10))

cats = ['rec.motorcycles',
        'rec.sport.baseball',
        'comp.graphics',
        'comp.windows.x',
        'talk.politics.mideast',
        'sci.space',
        'sci.electronics',
        'sci.med']

news_df = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'), categories=cats, random_state=15)

train_news = fetch_20newsgroups(subset='train', remove=('headers', 'footers', 'quotes'), categories=cats, random_state=131)
test_news = fetch_20newsgroups(subset='test', remove=('headers', 'footers', 'quotes'), categories=cats, random_state=131)

x_train = train_news.data
y_train = train_news.target
x_test = test_news.data
y_test = test_news.target



print()
print("===============================================================================")
print(news_df["data"][0])

print(type(news_df))
print(news_df.keys())
print(type(news_df.data), type(news_df.target_names), type(news_df.target))

for i, val in zip(np.unique(news_df.target), news_df.target_names):
    print("index({}): topic {}".format(i, val))


print(len(news_df.data), len(news_df.data[0]), len(news_df.data[1]))
print(len(news_df.target_names))
print(news_df.target.shape)
print(news_df.data[0][:100])


cnt_vect = CountVectorizer(
        max_df=0.95,
        max_features=1500,
        min_df=2,
        stop_words='english',
        ngram_range=(1, 2)
)



word_vect = cnt_vect.fit_transform(x_train)
np_vect = word_vect.todense()
print(np_vect[0])
print(cnt_vect.inverse_transform(word_vect[0]))


from sklearn.decomposition import LatentDirichletAllocation

lda = LatentDirichletAllocation(n_components=8, random_state=42)
lda.fit(word_vect)

print(lda.components_.shape)
print(lda.components_)
