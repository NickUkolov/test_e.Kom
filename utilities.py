import os
import re
from pathlib import Path

from tinydb import Query, TinyDB


db = TinyDB(os.path.join(Path(__file__).resolve().parent, 'db.json'))
forms = db.table('forms')


date_regex = re.compile(r'(0?[1-9]|[12][0-9]|3[01]).(0?[1-9]|1[012]).((19|20)\d\d)|'
                        r'[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])')
phone_regex = re.compile(r'^((\+7|7)+([0-9]){10})$')
email_regex = re.compile(r'^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$')


def validate_form(data_):

    res = dict()
    for key, value in data_.items():

        if date_regex.match(value):
            value = 'date'
            res[key] = value

        elif phone_regex.match(value.strip()):
            value = 'phone'
            res[key] = value

        elif email_regex.match(value):
            value = 'email'
            res[key] = value

        else:
            value = 'text'
            res[key] = value

    if not res:
        return {'error': 'Enter data'}

    if form_name := forms.search(Query().fragment(res)):
        return f'Form name: {form_name[0].get("name")}'

    return res
