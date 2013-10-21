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


if __name__ == '__main__':
    main()