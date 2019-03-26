import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

from appTwo.models import Topic,AccessRecord, Webpages


import random

from faker import Faker

fakegen = Faker()

topics = ['search', 'social', 'Marketplace', 'News', 'Games']


def add_topic():
    # noinspection PyUnresolvedReferences
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        # get the topic for the entry

        top = add_topic()

        # create the fake data for that entry

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the webpage entry

        webpg = Webpages.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':

    print("populating script!")
    populate(20)
    print("completed")
