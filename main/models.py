from peewee import *

db = SqliteDatabase("report.db")


class Racer(Model):
    position = IntegerField()
    driver = CharField()
    car = CharField()
    start = DateTimeField()
    end = DateTimeField()
    time = CharField()
    disqualifid = CharField()
    result = CharField()
    key = CharField(unique=True)

    class Meta:
        database = db
        db_tables = 'Racers'
        order_by = ('position',)


