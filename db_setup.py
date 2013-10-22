import sys

__author__ = 'bitm'
"""
Only run this once to det up a new db
Or maybe if you wanna trash it all and start over

I mostly use this for development.
"""

from cardsubmitter import models, db


def main():
    db.drop_all()
    db.create_all()
    anon_user = models.Author(name="Anon")
    db.session.add(anon_user)
    db.session.commit()


def dummy_data():
    for user in xrange(1, 50):
        u = models.Author(name="Testuser{}".format(user))
        for card in xrange(1, 50):
            models.Card.create_card("test white {}-{}".format(user, card), u, '__')
            models.Card.create_card("test __ card  {}-{}".format(user, card), u, '__')


if __name__ == '__main__':
    main()
    if len(sys.argv) > 1 and sys.argv[1] == "data":
        dummy_data()