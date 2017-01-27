import cfr
import datetime
import json

print(json.dumps(cfr.train.schedule(
    datetime.date(2016, 12, 27),
    'Cluj-Napoca',
    'Brasov'
)))
