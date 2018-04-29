from tvseries.ext import db
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship


class Responses(db.Model):
    __tablename__ = 'responses'
    #__table_args__ = {'schema': 'public'}
    id = db.Column(db.Integer(),
                   nullable=False, unique=True,
                   autoincrement=True, primary_key=True)
    end_user_id = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    campaign_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    ip_address = db.Column(db.String(50), nullable=False)
    origin_url = db.Column(db.String(250), nullable=True)

    tags = db.Column(db.Integer(), ForeignKey('tags.id'), nullable=True)
    tag = relationship("Tags")

    def __repr__(self):
        if self.description:
            self.description = "{0}...".format(self.description[0:10])

        return ("Responses(id={!r}, end_user_id={!r},  score={!r}, "
                "description={!r}, campaign_id={!r}), "
                "created_at={!r}, updated_at={!r}), "
                "ip_address={!r}, origin_url={!r}),  tags={!r})").format(
            self.id,
            self.end_user_id,
            self.score,
            self.description,
            self.campaign_id,
            self.created_at,
            self.updated_at,
            self.ip_address,
            self.origin_url,
            self.tags)


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer(),
                   nullable=False, unique=True,
                   autoincrement=True, primary_key=True)
    name = db.Column('name', db.String(200), nullable=False)

    def __repr__(self):
        return ("Tags(id={!r}, name={!r}").format(
            self.id,
            self.name)
