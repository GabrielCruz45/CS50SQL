# players_orm.py
import datetime
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    select,
    func,
    or_,
    and_
)
from sqlalchemy.orm import declarative_base, Session

# --- Boilerplate Setup ---
engine = create_engine("sqlite:///week_0/pset0/alchemy/players/players.db")
Base = declarative_base()


# --- ORM Model Definition ---
# This class maps to the 'players' table.
class Player(Base):
    """SQLAlchemy ORM model for the 'players' table."""

    __tablename__ = "players"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    bats = Column(String)
    throws = Column(String)
    weight = Column(Integer)
    height = Column(Integer)
    debut = Column(Date)
    final_game = Column(Date)
    birth_year = Column(Integer)
    birth_month = Column(Integer)
    birth_day = Column(Integer)
    birth_city = Column(String)
    birth_state = Column(String)
    birth_country = Column(String)

    def __repr__(self):
        """Provides a developer-friendly representation of a Player object."""
        return (
            f"<Player(id={self.id}, first_name='{self.first_name}', "
            f"last_name='{self.last_name}')>"
        )


# --- Main Execution Block ---
if __name__ == "__main__":
    with Session(engine) as session:
        print("Players ORM Exercises")

        # 1. Find the hometown of Jackie Robinson.
        statement_one = select(
            Player.birth_city, 
            Player.birth_state, 
            Player.birth_country
        ).where(
            Player.first_name == 'Jackie', 
            Player.last_name == 'Robinson'
        )
        
        jackie_town = session.execute(statement_one).all()
        # print(jackie_town)

        # 2. Find the side Babe Ruth hit.
        statement_two = select(Player.bats).where(Player.first_name == 'Babe', Player.last_name == 'Ruth')
        babe_bats = session.scalar(statement_two)
        # print(babe_bats)

        # 3. Find the ids of rows for which 'debut' is missing.
        statement_three = select(Player.id).where(Player.debut.is_(None))
        null_ids = session.scalars(statement_three).all()
        # print(null_ids)

        # 4. Find the first and last names of players not born in the USA.
        statement_four = select(
                Player.first_name, 
                Player.last_name
            ).where(
                Player.birth_country.is_not('USA')
            ).order_by(
                Player.first_name, 
                Player.last_name
            )
            
        not_usa_players = session.execute(statement_four).all()
        # print(not_usa_players)

        # 5. Return the first and last names of all right-handed batters.
        statement_five = select(
                Player.first_name, 
                Player.last_name
            ).where(
                Player.bats == 'R'
            ).order_by(
                Player.first_name, 
                Player.last_name
            )
        right_handed_bats = session.execute(statement_five).all()
        # print(right_handed_bats)


        # 6. Return the first name, last name, and debut of players born in Pittsburgh, PA.
        statement_six = select(
                Player.first_name, 
                Player.last_name, 
                Player.debut
            ).where(
                Player.birth_city == 'Pittsburgh',
                Player.birth_state == 'PA'
            ).order_by(
                Player.debut.desc(),
                Player.first_name,
                Player.last_name
            )

        pitt_players = session.execute(statement_six).all()
        # print(pitt_players)
        
        # 7. Count players who bat right/throw left, or vice versa.
        statement_seven = select(func.count(Player.first_name)).where(
            or_(
                and_(Player.bats == 'R', Player.throws == 'L'),
                and_(Player.bats == 'L', Player.throws == 'R')
            )
        )
        bats_throws_diff = session.scalar(statement_seven)
        # print(bats_throws_diff)

        # 8. Find the average height and weight of players who debuted on or after Jan 1st, 2000.
        date_eight = datetime.date(2000, 1, 1)
        statement_eight = select(
            func.round(func.avg(Player.height), 2), 
            func.round(func.avg(Player.weight), 2)
        ).where(
            Player.debut > date_eight
        )
        avg_hw = session.execute(statement_eight).all()
        # print(avg_hw)
        
        # 9. Find players whose final game was in 2022.
        statement_nine = select(
            Player.first_name, 
            Player.last_name
        ).where(
            Player.final_game.like('2022%')
        ).order_by(
            Player.first_name, 
            Player.last_name
        )
        
        final_game = session.execute(statement_nine).all()
        print(final_game)

        # 10. Your own custom query.
        start_date = datetime.date(1919, 12, 31)
        end_date = datetime.date(1930, 1, 1)
        
        statement_ten = select(
            Player.first_name, 
            Player.last_name, 
            Player.bats
        ).where(
            Player.debut.between(start_date, end_date)
        ).order_by(Player.birth_country)
        
        custom = session.execute(statement_ten).all()
        
        print(custom)