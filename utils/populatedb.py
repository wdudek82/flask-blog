import datetime as dt
from faker import Faker
from project import db
from apps.posts.models import Author, Post


class PopulateDB:
    fake = Faker()

    @classmethod
    def create_fake_authors(cls, count=3):
        print("Deleting old authors...", end=' ')
        Author.query.delete()
        db.session.commit()
        print("OK")

        print("Creating fake authors...", end=' ')
        for _ in range(count):
            username = cls.fake.name()
            email = cls.fake.email()

            author = Author(username=username, email=email)
            db.session.add(author)
        db.session.commit()
        print("OK")

    @classmethod
    def create_fake_posts(cls, count=10):
        print("Deleting old posts...", end=' ')
        Post.query.delete()
        db.session.commit()
        print("OK")

        print("Creating fake posts...", end=' ')
        for _ in range(count):
            title = cls.fake.sentence()
            content = cls.fake.text()
            # pub_date = cls.fake.date

            post = Post(
                title=title,
                content=content,
                pub_date=dt.datetime.now(),
                created_at=dt.datetime.now(),
                updated_at=dt.datetime.now(),
            )
            db.session.add(post)
        db.session.commit()
        print("OK")


if __name__ == '__main__':
    PopulateDB.create_fake_authors()
    PopulateDB.create_fake_posts()
