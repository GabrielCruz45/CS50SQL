
-- *** The Lost Letter ***
SELECT * FROM "packages"; -- See first hand how's the data expressed in the table "packages"
SELECT * FROM "addresses"; -- See first hand how's the data expressed in the table "addresses"
SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'; -- Check for the id of the address where the letter was "sent" from -900 Somerville Avenue
SELECT "id", "contents", "to_address_id" FROM "packages" WHERE "from_address_id" = ( 
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
); -- Get package_id, contents and to_address_id with previously found from_address_id
SELECT "id", "contents", "to_address_id" FROM "packages" WHERE "from_address_id" = ( 
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
)
AND
"contents" LIKE '%congratulatory%';-- Congratulatory letter package_id is 384, filter other packages sent with %congratulatory%
SELECT "id" FROM "packages" WHERE "from_address_id" = ( 
    SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
)
AND
"contents" LIKE '%congratulatory%'; -- Only need package id to run next "scans" query

SELECT * FROM "scans" WHERE "package_id" = (
    SELECT "id" FROM "packages" WHERE "from_address_id" = ( 
        SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
    )
    AND
    "contents" LIKE '%congratulatory%'
); -- Get full, correct scan info
-- Got back from preious query:

-- 54|1|384|432|Pick|2023-07-11 19:33:55.241794
-- 94|1|384|854|Drop|2023-07-11 23:07:04.432178
-- It was successfully dropped off, but where exactly?


SELECT "type", "address" FROM "addresses" WHERE "id" = (
    SELECT "address_id" FROM "scans" WHERE "package_id" = (
        SELECT "id" FROM "packages" WHERE "from_address_id" = ( 
            SELECT "id" FROM "addresses" WHERE "address" = '900 Somerville Avenue'
        )
        AND
        "contents" LIKE '%congratulatory%'
    )
); --Which address the letter was sent to and what type of address it is.
--Residential|900 Somerville Avenue




-- *** The Devious Delivery ***
SELECT * FROM "packages" WHERE "contents" LIKE '%duck%' OR '%rubber%'; -- Check which packages match available info. 

SELECT * FROM "packages" 
JOIN "scans" ON "packages"."id" = "scans"."package_id" 
JOIN "addresses" ON "scans"."address_id" = "addresses"."id" 
WHERE ("packages"."contents" LIKE '%duck%' OR "packages"."contents" LIKE '%rubber%') 
AND "scans"."action" = 'Pick'; --Combine tables to get more info on packages with previous available info.

--Realized had another piece of critical information ––the "from" address is NULL.-
SELECT * FROM "packages" WHERE "from_address_id" IS NULL; --Returned: ```5098|Duck debugger||50```

SELECT * FROM "scans" 
JOIN "packages" ON "scans"."package_id" = "packages"."id"
WHERE "packages"."from_address_id" IS NULL; --What happened with the package? These are the scans
-- 30123|10|5098|50|Pick|2023-10-24 08:40:16.246648|5098|Duck debugger||50
-- 30140|10|5098|348|Drop|2023-10-24 10:08:55.610754|5098|Duck debugger||50


SELECT "address_id" FROM "scans" 
JOIN "packages" ON "scans"."package_id" = "packages"."id"
WHERE "packages"."from_address_id" IS NULL
AND "scans"."action" = 'Drop';


--What type of address the package ended up on?
SELECT "type" FROM "addresses" WHERE id = (
    SELECT "address_id" FROM "scans"
    JOIN "packages" ON "scans"."package_id" = "packages"."id"
    WHERE "packages"."from_address_id" IS NULL
    AND "scans"."action" = 'Drop'
); -- 348's type address is 'Police Station'


--What is/are the package content/s?
SELECT "contents" FROM "packages"
JOIN "scans" ON "packages"."id" = "scans"."package_id"
WHERE "packages"."from_address_id" IS NULL
AND "scans"."action" = 'Drop'; --Duck Debbuger




-- *** The Forgotten Gift ***
SELECT * FROM "scans"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
WHERE "addresses"."address" = '109 Tileston Street';
-- Check for packages with given "from" address

-- Now this list needs to be filtered with given "to" address

SELECT * FROM "scans"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
JOIN "packages" ON "scans"."package_id" = "packages"."id"; --This double JOIN works so...

SELECT * FROM "scans"
JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
JOIN "packages" ON "scans"."package_id" = "packages"."id"
WHERE "addresses"."address" = '109 Tileston Street'
AND "packages"."to_address_id" = (
    SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place'
); --Filtered to only one 'Pick' entry ––we now need the driver's name and later the contents

SELECT "name" FROM "drivers" WHERE "id" = (
    SELECT "driver_id" FROM "scans"
    JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
    JOIN "packages" ON "scans"."package_id" = "packages"."id"
    WHERE "addresses"."address" = '109 Tileston Street'
    AND "packages"."to_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place'
    )
); --Driver's name -> Maegan


SELECT "contents" FROM "packages" WHERE "id" = (
    SELECT "package_id" FROM "scans"
    JOIN "addresses" ON "scans"."address_id" = "addresses"."id"
    JOIN "packages" ON "scans"."package_id" = "packages"."id"
    WHERE "addresses"."address" = '109 Tileston Street'
    AND "packages"."to_address_id" = (
        SELECT "id" FROM "addresses" WHERE "address" = '728 Maple Place'
    )
); --Contents -> Flowers
