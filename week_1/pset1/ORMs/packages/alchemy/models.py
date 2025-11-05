from database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


# CREATE TABLE IF NOT EXISTS "addresses" (
#     "id" INTEGER,
#     "address" TEXT,
#     "type" TEXT,
#     PRIMARY KEY("id")
# );

class Address(Base):
    __tablename__ = "addresses"
    
    id: Mapped[int]
    address: Mapped[str] = mapped_column(nullable=False)
    # 'type' column renamed  to 'address_label' to avoid keyword conflict
    address_label: Mapped[str] = mapped_column("type", nullable=False)
    
    
    sent_packages: Mapped[List["Package"]] = relationship(
        back_populates="from_address"
    )
    
    received_packages: Mapped[List["Package"]] = relationship(
        back_populates="to_address"
    )
    
    scanned_address: Mapped[List["Scan"]] = relationship(
        back_populates="address_scan"
    )


# CREATE TABLE IF NOT EXISTS "packages" (
#     "id" INTEGER,
#     "contents" TEXT,
#     "from_address_id" INTEGER,
#     "to_address_id" INTEGER,
#     PRIMARY KEY("id"),
#     FOREIGN KEY("from_address_id") REFERENCES "addresses"("id"),
#     FOREIGN KEY("to_address_id") REFERENCES "addresses"("id")
# );


class Package(Base):
    __tablename__ = "packages"
    
    id: Mapped[int]
    contents: Mapped[str]
    from_address_id: Mapped[int]
    to_address_id: Mapped[int]
    
    
    from_address: Mapped["Address"] = relationship(
        foreign_keys=[from_address_id],
        back_populates="sent_packages"
    )

    to_address: Mapped["Address"] = relationship(
        foreign_keys=[to_address_id],
        back_populates="received_packages"
    )
    
    tracking_scans: Mapped[List["Scan"]] = relationship(
        back_populates="scanned_package"
    )


# CREATE TABLE IF NOT EXISTS "drivers" (
#     "id" INTEGER,
#     "name" TEXT,
#     PRIMARY KEY("id")
# );

class Driver(Base):
    __tablename__ = "drivers"
    
    id: Mapped[int]
    name: Mapped[str]
    
    
    drivers_scan: Mapped[List["Scan"]] = relationship(
        back_populates="scans_driver"
    )
    

# CREATE TABLE IF NOT EXISTS "scans" (
#     "id" INTEGER,
#     "driver_id" INTEGER,
#     "package_id" INTEGER,
#     "address_id" INTEGER,
#     "action" TEXT,
#     "timestamp" NUMERIC,
#     PRIMARY KEY("id"),
#     FOREIGN KEY("driver_id") REFERENCES "drivers"("id"),
#     FOREIGN KEY("package_id") REFERENCES "packages"("id"),
#     FOREIGN KEY("address_id") REFERENCES "addresses"("id")
# );


class Scan(Base):
    __tablename__ = "scans"
    
    id: Mapped[int]
    driver_id: Mapped[int]
    package_id: Mapped[int]
    address_id: Mapped[int]
    action: Mapped[str]
    timestamp: Mapped[float]
    
    
    scans_driver: Mapped["Driver"] = relationship(
        foreign_keys=[driver_id],
        back_populates="drivers_scan"
    )
    
    scanned_package: Mapped["Package"] = relationship(
        foreign_keys=[package_id],
        back_populates="tracking_scans"
    )
    
    address_scan: Mapped["Address"] = relationship(
        foreign_keys=[address_id],
        back_populates="scanned_address"
    )
