import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
import warnings

from sqlalchemy import select
from sqlalchemy.orm import aliased

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer

from bot.app.database import Session
from bot.app.database.models_orm import Books, Authors, Category, CategoryID

warnings.filterwarnings('ignore')
lemm = WordNetLemmatizer()
stemmer = SnowballStemmer("russian")


stop_words = stopwords.words('english') + stopwords.words('russian')


def get_data(session: Session, cat: str):
    with session() as s:
        b = aliased(Books)
        a = aliased(Authors)
        c = aliased(Category)
        ci = aliased(CategoryID)

        query = (
            select(
                b.id,
                b.title,
                a.firstname,
                a.lastname,
                b.description,
                b.description_nlp,
                b.rating,
                b.votes
            )
            .select_from(b)
            .join(a, a.id == b.author)
            .join(c, c.id == b.category)
            .join(ci, ci.id == c.cat_id)
            .where(ci.title == cat)
        )

        result = s.execute(query)
        return result.all()


def create_data_frame(data) -> pd.DataFrame:
    return pd.DataFrame(data)


def create_coefs(data: pd.DataFrame) -> pd.DataFrame:
    min_num_ratings = np.min(data.votes)
    max_num_ratings = np.max(data.votes)

    norm_coef = max_num_ratings - min_num_ratings

    data['coef'] = data.rating * (data.votes - min_num_ratings) / norm_coef

    return data


def tokenize(row, lemm_, stemmer_):
    token = word_tokenize(row)
    token = [i for i in token if (i not in stop_words)]
    token = [lemm_.lemmatize(t) for t in token]
    token = [stemmer_.stem(t) for t in token]
    return ' '.join([t.lower() for t in token])


def nearest_neighbors(data: pd.DataFrame, string: str) -> dict:
    tfidf = TfidfVectorizer()
    X_tfidf = tfidf.fit_transform(data.description_nlp)

    neighbors = NearestNeighbors(n_neighbors=30, metric='cosine')
    neighbors.fit(X_tfidf)

    X_tfidf = tfidf.transform([tokenize(string, lemm, stemmer)])

    res = neighbors.kneighbors(X_tfidf, return_distance=True)

    result = data.iloc[res[1][0]].sort_values(['coef', 'rating', 'votes'], ascending=[False, False, True])
    result.drop_duplicates('title', inplace=True)
    return result[['title', 'description', 'rating']].head(10).to_dict()
