from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import sqlalchemy
import os
from os import getenv
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
db_url = getenv("DB_URL")
engine = sqlalchemy.create_engine(db_url)

Base = declarative_base()
meta = MetaData()

class Artist(Base):
    __tablename__ = "Artist"

    id = Column(String(22), primary_key=True)
    name = Column(VARCHAR(100), nullable=False)
    uri = Column(VARCHAR(50), nullable=False)
    genres = Column(Text, nullable=False)
    popularity = Column(Integer, nullable=False)
    track = relationship("Track", back_populates='artist')

class Track(Base):
    __tablename__ = "Track"
    id = Column(String(22), primary_key=True)
    name = Column(String(100), nullable=False)
    uri = Column(String(50), nullable=False)
    popularity = Column(Integer, nullable=False)
    duration = Column(BigInteger, nullable=False)
    explicit = Column(Integer, nullable=False)
    release_date = Column(Text, nullable=False)
    year = Column(Text, nullable=False)
    artist_id = Column(ForeignKey("Artist.id"), nullable=False)
    danceability = Column(Float, nullable=False)
    energy = Column(Float, nullable=False)
    key = Column(Integer, nullable=False)
    loudness = Column(Float, nullable=False)
    mode = Column(Integer, nullable=False)
    speechiness = Column(Float, nullable=False)
    acousticness = Column(Float, nullable=False)
    instrumentalness = Column(Float, nullable=False)
    liveness = Column(Float, nullable=False)
    valence = Column(Float, nullable=False)
    tempo= Column(Float, nullable=False)
    artist = relationship("Artist", back_populates="track")


Base.metadata.create_all(bind=engine, checkfirst=True)
"""
artist = Table('Artist', meta,
    Column('id', String(22), primary_key=True),
    Column('name', VARCHAR(100), nullable=False),
    Column('uri', VARCHAR(50), nullable=False),
    Column('genres', Text),
    Column('popularity', Integer, nullable=False)
    )

track = Table('Track', meta,
    Column('id', String(22), primary_key=True),
    Column('name', String(100), nullable=False),
    Column('uri', String(50), nullable=False),
    Column('popularity', Integer, nullable=False),
    Column('duration', BigInteger, nullable=False),
    Column('explicit', BINARY, nullable=False),
    Column('release_date', DATE, nullable=False),
    Column('year', DATE, nullable=False),
    Column('artist_id', String, ForeignKey("Artist.id")),
    Column('danceability', Float, nullable=False),
    Column('energy', Float, nullable=False),
    Column('key', Integer, nullable=False),
    Column('loudness', Float, nullable=False),
    Column('mode', BINARY, nullable=False),
    Column('speechiness', Float, nullable=False),
    Column('acousticness', Float, nullable=False),
    Column('instrumentalness', Float, nullable=False),
    Column('liveness', Float, nullable=False),
    Column('valence', Float, nullable=False),
    Column('tempo', Float, nullable=False),
    )
track.artist = relationship("Artist", back_populates="artist_id")
meta.create_all(bind=engine)
"""