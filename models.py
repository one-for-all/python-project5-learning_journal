import datetime

from peewee import *


DATABASE = SqliteDatabase('journal.db')


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Entry, Tag], safe=True)
    DATABASE.close()


class Entry(Model):
    title = CharField(max_length=255)
    date = DateField(default=datetime.date.today)
    time_spent = CharField(max_length=100)
    learned = TextField()
    resources = TextField()

    def tags(self):
        return Tag.select().where(Tag.entry == self)

    class Meta:
        database = DATABASE
        order_by = ('-date',)


class Tag(Model):
    entry = ForeignKeyField(Entry, related_name='tags')
    content = CharField(max_length=255)

    class Meta:
        database = DATABASE
