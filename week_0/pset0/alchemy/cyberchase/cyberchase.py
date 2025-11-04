# cyberchase_orm.py
import sqlalchemy
import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    select,
    func
)
from sqlalchemy.orm import declarative_base, Session

# --- Boilerplate Setup ---
# Establishes the connection to the SQLite database file.
engine = create_engine("sqlite:///week_0/pset_0/alchemy/cyberchase/cyberchase.db")

# The Base is a factory for creating ORM models.
Base = declarative_base()


# --- ORM Model Definition ---
# This class maps to the 'episodes' table in the database.
class Episode(Base):
    """SQLAlchemy ORM model for the 'episodes' table."""

    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True)
    season = Column(Integer)
    episode_in_season = Column(Integer)
    title = Column(String)
    topic = Column(String)
    # The database stores dates, so we use the Date type.
    air_date = Column(Date)
    production_code = Column(String)

    def __repr__(self):
        """Provides a developer-friendly representation of an Episode object."""
        return (
            f"<Episode(id={self.id}, season={self.season}, "
            f"title='{self.title}')>"
        )


# --- Main Execution Block ---
if __name__ == "__main__":
    # The session is the primary interface for database operations.
    with Session(engine) as session:
        print("Cyberchase ORM Exercises")

        # 1. List the titles of all episodes in Season 1.
        statement_one = select(Episode).where(Episode.season == 1)
        season_one_episodes = session.scalars(statement_one).all()
        # print(season_one_episodes)

        # 2. List the season number and title of the first episode of every season.
        statement_two = select(Episode.title).where(Episode.episode_in_season == 1)
        first_episode_of_season = session.scalars(statement_two).all()
        # print(first_episode_of_season)

        # 3. Find the production code for the episode “Hackerized!”.
        statement_three = select(Episode.production_code).where(Episode.title == "Hackerized!")
        production_code_hackerized = session.scalar(statement_three)
        # print(production_code_hackerized)

        # 4. Find the titles of episodes that do not yet have a listed topic.
        statement_four = select(Episode.title).where(Episode.topic.is_(None))
        titles_production_null = session.scalars(statement_four).all()
        # print(titles_production_null)

        # 5. Find the title of the holiday episode that aired on December 31st, 2004.
        statement_five = select(Episode.title).where(Episode.air_date == '2004-12-31')
        holiday_episode_2004 = session.scalar(statement_five)
        # print(holiday_episode_2004)

        # 6. List the titles of episodes from season 6 (2008) that were released early, in 2007.
        statement_six = select(Episode.title).where(Episode.air_date.like('2007%'), Episode.season == 6)
        early_season_six = session.scalars(statement_six).all()
        # print(early_season_six)

        # 7. List the titles and topics of all episodes teaching fractions.
        statement_seven = select(Episode.title).where(Episode.topic.like('%fraction%'))
        fraction_episodes = session.scalars(statement_seven).all()
        # print(fraction_episodes)

        # 8. Count the number of episodes released from 2018 to 2023, inclusive.
        # ******Use variables for robust/portable code. Databases use different requirements for date string literals********
        start_date = datetime.date(2018, 1, 1)
        end_date = datetime.date(2023, 12, 31)
        
        statement_eight = select(func.count(Episode.title)).where(Episode.air_date.between(start_date, end_date))
        episodes_2018_2023 = session.scalar(statement_eight)
        # print(episodes_2018_2023)

        # 9. Count the number of episodes released from 2002 to 2007, inclusive.
        start_date9 = datetime.date(2002, 1, 1)
        end_date9 = datetime.date(2007, 12, 31)
        
        statement_nine = select(func.count(Episode.title)).where(Episode.air_date.between(start_date9, end_date9))
        episodes_2002_2007 = session.scalar(statement_nine)
        # print(episodes_2002_2007)

        # 10. List the ids, titles, and production codes of all episodes, ordered by production code.
        statement_ten = select(Episode.id, Episode.title, Episode.production_code).order_by(Episode.production_code)
        id_title_prod_orderedByCode = session.execute(statement_ten).all()
        # print(id_title_prod_orderedByCode)

        # 11. List the titles of episodes from season 5, in reverse alphabetical order.
        statement_eleven = select(Episode.title).where(Episode.season == 5).order_by(Episode.title.desc())
        reverse_season_5 = session.scalars(statement_eleven).all()
        # print(reverse_season_5)

        # 12. Count the number of unique episode titles.
        statement_twelve = select(func.count(Episode.title).distinct())
        unique_titles_count = session.scalar(statement_twelve)
        # print(unique_titles_count)

        # 13. Your own custom query.
        custom_air_date = datetime.date(2019, 1, 1)
        statement_thirteen = select(func.count(Episode.title)).where(Episode.air_date >= custom_air_date, Episode.topic.is_(None))
        custom_query = session.scalar(statement_thirteen)
        # print(custom_query)
        
        practice_statement = select(Episode.id, Episode.title, Episode.air_date, Episode.topic).where(Episode.air_date >= custom_air_date, Episode.topic.is_(None))
        custom_query2 = session.execute(practice_statement).all()
        print(custom_query2)
        