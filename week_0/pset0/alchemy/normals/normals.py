# normals_orm.py
import sqlalchemy
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    Float,
    String,
    select,
    func
)
from sqlalchemy.orm import declarative_base, Session

# --- Boilerplate Setup ---
engine = create_engine("sqlite:///week_0/pset_0/alchemy/normals/normals.db")
Base = declarative_base()


# --- ORM Model Definition ---
# This class maps to the 'normals' table.
class Normal(Base):
    """SQLAlchemy ORM model for the 'normals' table."""

    __tablename__ = "normals"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)
    # Column names like '0m' are not valid Python identifiers.
    # We map a valid attribute name (e.g., temp_0m) to the actual column name.
    temp_0m = Column("0m", Float)
    temp_5m = Column("5m", Float)
    temp_10m = Column("10m", Float)
    temp_50m = Column("50m", Float)
    temp_100m = Column("100m", Float)
    temp_200m = Column("200m", Float)
    temp_225m = Column("225m", Float)
    # ... add other depth columns as needed for your queries

    def __repr__(self):
        """Provides a developer-friendly representation of a Normal object."""
        return (
            f"<Normal(lat={self.latitude}, lon={self.longitude}, "
            f"temp_0m={self.temp_0m})>"
        )


# --- Main Execution Block ---
if __name__ == "__main__":
    with Session(engine) as session:
        print("Normals ORM Exercises")

        # 1. Find the normal ocean surface temperature at 42.5° latitude and -69.5° longitude.
        statement_one = select(Normal.temp_0m).where(Normal.latitude == 42.5, Normal.longitude == -69.5)
        normal_surface_temp = session.scalar(statement_one)
        # print(normal_surface_temp)

        # 2. Find the normal temperature of the deepest sensor (225m) at the same coordinate.
        statement_two = select(Normal.temp_225m).where(Normal.latitude == 42.5, Normal.longitude == -69.5)
        normal_bottom_temp = session.scalar(statement_two)
        # print(normal_bottom_temp)

        # 3. Find the normal temperature at 0m, 100m, and 200m for a location of your choice.
        statement_three = select(
                            Normal.temp_0m, 
                            Normal.temp_100m, 
                            Normal.temp_200m
                        ).where(
                            Normal.latitude == 18.5, 
                            Normal.longitude == -67.5
        )
        normal_temp_at = session.execute(statement_three).all()
        print(normal_temp_at)

        # 4. Find the lowest normal ocean surface temperature.
        statement_four = select(Normal.temp_0m).order_by(Normal.temp_0m).limit(1)
        lowest_normal_temp = session.scalar(statement_four)
        # print(lowest_normal_temp)

        # 5. Find the highest normal ocean surface temperature.
        statement_five = select(Normal.temp_0m).order_by(Normal.temp_0m.desc()).limit(1)
        highest_normal_temp = session.scalar(statement_five)
        # print(highest_normal_temp)
    
        # 6. Return all normal ocean temperatures at 50m within the Arabian Sea coordinates.
        statement_six = select(Normal.temp_50m).where(
            Normal.latitude.between(0, 20), 
            Normal.longitude.between(55, 75), 
            Normal.temp_50m.is_not(None)
        )
        arabian_sea = session.scalars(statement_six).all()
        # print(arabian_sea)

        # 7. Find the average ocean surface temperature along the equator.
        statement_seven = select(func.round(func.avg(Normal.temp_0m), 2)).where(Normal.latitude.between(-0.5, 0.5))
        avg_equator_temp = session.scalar(statement_seven)
        # print(avg_equator_temp)

        # 8. Find the 10 locations with the lowest normal ocean surface temperature.
        statement_eight = select(Normal.latitude, Normal.longitude, Normal.temp_0m).order_by(Normal.temp_0m, Normal.latitude).limit(10)
        lowest_temp_locations = session.execute(statement_eight).all()
        # print(lowest_temp_locations)

        # 9. Find the 10 locations with the highest normal ocean surface temperature.
        statement_nine = select(Normal.latitude, Normal.longitude, Normal.temp_0m).order_by(Normal.temp_0m.desc(), Normal.latitude).limit(10)
        highest_temp_locations = session.execute(statement_nine).all()
        # print(highest_temp_locations)

        # 10. Determine how many points of latitude have at least one data point.
        statement_ten = select(func.count(Normal.latitude.distinct()))
        latitude_points = session.scalar(statement_ten)
        # print(latitude_points)
        