import os
import pathlib
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'django_web.settings')
django.setup()

from dbase.models import Vocab

import pandas as pd


def add_data():
    df = pd.read_csv('static/dbase/meta.csv')
    Vocab.objects.all().delete()
    for i in range(len(df)):
        au = df.iloc[i]['author']
        ti = df.iloc[i]['title']
        yr = df.iloc[i]['year']
        gn = df.iloc[i]['genre']
        entry = Vocab.objects.get_or_create(author = au, title = ti, year = yr, genre = gn)

add_data()