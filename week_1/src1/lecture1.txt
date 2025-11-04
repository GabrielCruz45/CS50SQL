[MUSIC PLAYING] CARTER ZENKE: Well, hello, one and all and welcome back to CS50's Introduction to Databases with SQL. My name is Carter Zenke. And last we left off, we learned all about querying-- how to ask questions of data in a single table. 

Today, though, we'll take one step forward, and we'll have databases that have not just one table inside of them but, actually, multiple tables-- tables for authors, tables for books, and for publishers, and so on-- to represent all of these people who are part of the book industry. And you, too, can apply these same skills for whatever you want to represent as well. 

So let's pick up where we left off, which was with this database of books. And I'll come back to my computer over here. And if you recall, we had this data set that was the books that were longlisted for the International Booker Prize. To be longlisted means to be nominated for some prize in a given year. And the international Booker Prize is awarded every year to one book, but 13 are nominated. 

So in this data set, we have 13 books the past five years that were nominated for this prize. Now, I'll go ahead and open up this database once more. And if you remember, we used this command last time to open this data set-- sqlite3 space the file name, where our file name was longlist.db. And this is one example of our database management system-- this one called SQLite, and this one being the third version of SQLite. 

So let's re-open this database and let me show you what we have now in store. I'll type sqlite-- whoops, I'll type sqlite-- sqlite3 and then longlist.db. And I'll hit Enter. Now, my prompt changes. I no longer have this dollar sign. I now have the SQLite prompt. And here's what we saw last time-- I could write my SQL queries. 

Well, before we start, let's see the changes to this database. So if I want to get a feel for the tables that are inside of this database, I can use a command-- this one called .tables. Notice this is not a SQL keyword. This is a command particular to SQLite to show me what tables are inside this database. 

So I'll type enter here. And now I see I have more than one table. I have a table for authors, a table for books, for publishers, and even more. And now that we're working with not just one table but multiple, we're actually moving into this idea of a relational database. 

So no longer do we have a database with only one table inside of it. We now have multiple. And these tables, presumably, have some kind of relationship among them. You could think, for instance, of an author writing a book, or a publisher publishing a book, or even a translator translating a book. So we'll have these tables and these relationships among them. 

So let's look at one example of this kind of relationship among tables. I could have a table of authors and a table of books-- this simplified for now to one column in every table. Well, with my authors table, I have names. In my books table, I have titles. 

And we seem to be moving in the right direction. I could store more information about authors and books. But I've also created some problem. Like, how do I know, now, who wrote which book? Like, earlier, we saw that, maybe, Eva is right next to Boulder in a single table for authors and books. And we know that Eva wrote Boulder that way. 

But now, if I look at authors, I only see Eva and no information about books. So we seem to have this problem here. Well, one solution might be something like the honor system. I'm honest. And, presumably, so are you. We could say that. well, maybe the first row in authors will always correspond to the first row in books. So we always know Eva wrote Boulder because Eva's first in the authors table and Boulder is first in the books table. 

Similarly, let's say Han wrote The White Book because Han is in the second row and The White Book is in the second row in books. But I have to imagine, as good as I am at being honest and transparent, maybe I make a mistake. Maybe I add a row to books but not to authors. Or maybe I add a row to authors and not to books. 

I could change data and not update it to adhere to that standard. So let's actually take a step back and maybe think, well, is it better, then, to have this kind of situation, where we did have one table with authors and books? It might be. But let's think. 

This could work for a while. But let's say Olga is a prolific author. They like to write not just one book but two. They wrote not just Flights but also The Books of Jacob. Well, let's say Olga writes another book or another one too. What might be the problem with this arrangement now? And feel free to raise your hand, too, with your ideas. 

Well, I might run into some issues here if we only have one table of authors and books. 

SPEAKER: There is some redundancy, some repetition. 

CARTER ZENKE: Yeah, good idea. So you might notice there's some redundancy here. Olga is in here twice, which is maybe OK if Olga wrote two books. But, again, let's say Olga wrote three, or four, or five. Olga will be in here that many times. And so we could probably do a bit better than this. And let's actually just say this is going to be the most efficient idea for us. Let's go back to these multiple tables here and think about how we could relate these two tables, one to the other. 

Now before we get into the details of how we might do this technically, let's think about the kinds of relationships we could have between authors and books. Well, maybe, in our world, we have one author that writes one book. And maybe we could say every author only writes one book. And, similarly, one book is always written by one author. 

This could be true for some books and some authors. But, arguably, it's not the best assumption, right? We probably have authors writing more than one book or books being written by more than one author. So as it stands now, we could call this kind of relationship a one-to-one relationship. If this is our idea of authors and books, one author writes one book, and one book is written by one author. This is a one-to-one relationship. 

Well, as we know, authors can write more than one book. Olga, for example, didn't write just Flights. They also wrote another book. And so we could say, well, Olga wrote not just this book up top. They also wrote this book down below. And now we're moving from a one-to-one relationship to what we'll call a one-to-many relationship. There are many books that one author could write. 

But, of course, is this the full picture, too? Some books are only written by one author. But, presumably, some books are written by multiple authors. So we need to enhance our picture even further. Let's try that. 

Let me add another author into the mix here. This author wrote this book along with Olga, let's say. So notice how here we have one author writing more than one book, and we also have one book being written by more than one author. 

Well, this is called a many-to-many relationship. And it's called that because we have many books that can be written by many authors. So these, in general, are the kinds of relationships we'll have amongst our tables in a relational database-- one-to-one, one-to-many, and many-to-many. 

Now, thankfully, there are some tools we can use to visualize these kinds of relationships. We have at our disposal something called an Entity Relationship Diagram, something a bit like this. It's also called an ER diagram for short. 

And let me propose, just for now, that this is the diagram for our database. We have authors, and publishers, and translators, books, and ratings. These are our entities in our database, the things we're trying to represent. 

Now, you'll notice, though, that there's something more than just these boxes that have author, publisher, translator, and so on. There are all these lines among them. And they have verbs like wrote, and published, and translated. And maybe that makes sense to you. 

But at first glance, there's one line here that has three lines coming off of it, one line going across. This one has a circle on it. What does all that mean? This is kind of confusing at first glance. Well, this actually has some order to it, some rules that we can use. And let me show you what those rules are. 

So here, we have what's called a crow's foot notation, a way of trying to represent one-to-one, one-to-many, or many-to-many relationships using just lines and, in some cases, circles. So here, if you ever see this line with a circle on it, you could think of zero. This doesn't have to have anything related to it. 

You could think of this one with a bar going perpendicular as one. Something with this arrow has to have at least one thing that relates to it in some other table. And this one down below, the one that looks like a crow's foot-- well, this one means that some entity has many that could be related to it in some other table. 

So let's try this with an example. Here we have, again, our authors and our books. And here we can say that an author wrote one book. We read this left to right in this case. One author can have one book associated with them. We know it's one because we see this bar over our line here. 

Now we know, too, that books, at least in our world, could be written by one author. They must be written by at least one author. So let's try this. I'll include that arrow on the other side too. And I'll read this right to left. A book has to have at least one author. 

Now, I could add in more symbols too. We know that books could have more than one author and an author could write more than one book. So let's try enhancing our diagram even further. 

I could say-- adding in these crow's foot notation with the multiple lines here, now I could read it like this-- an author, going from left to right, can write at least one book, but they could write many books. They could write one or many books. And, similarly, a book could be written by at least one author but, certainly, also multiple too. 

So this is one example of an ER diagram for our database. And, hopefully, now you can see a bit more of this making sense to you. So we see that authors, here, could write many books. A book could be written by many authors. Books, actually, don't need to have a translator. They could have zero to many translators for their book here. But, in general, a translator should write-- or should translate at least one book or possibly many of them too. 

So let me pause here and ask, what questions do you have on these table relationships and these diagrams that we call ER Entity Relationship Diagrams? 

SPEAKER: Yeah, so, Carter, I want to ask that for any given database, how can we predetermine whether how the relationship between the tables are going to be? Because here we know that the author has some relationship to the books. But how can we determine whether those relationships are existent in the first place? 

CARTER ZENKE: A great question. If we have some database, how do we know the relationships among those entities or those things that are stored inside of it? Well, part of this is really up to you. When you're designing a database-- as we'll see in a future week of this course-- you have decisions to make. Do you want an author to be able to write only one book or multiple, for instance? 

Often, when I design a database, I might write a diagram like this so I could show this to somebody else who can know what tables I have and how they are related to one another. So if you're designing, you have the choice. But if you're taking a database from someone else, you could ask for a diagram like this that could show you those relationships among those tables. 

Let's see, what other questions do we have too on these tables and their relationships? 

SPEAKER: How do we determine that relationship? I mean, we know that it exists. But how we assign which author wrote which book or multiple books, or which book were written by what authors? 

CARTER ZENKE: Yeah, a great question. So how do we try to assign, then, these relationships, perhaps, in our database? Look, we know that an author could write multiple books, but how do we represent that in our table, let's say. 

Well for this, let me just transition to the next part of what we'll talk about, which is going to be this idea of a key. So keys are this fundamental idea in databases that can help us relate tables one to the other. And for this, let's actually do a bit of an example, a bit of a roleplay here. 

So I will be your librarian today. And let's say that you're looking for a book. This one is called The Birthday Party. And I say, OK, I'll find you this book. I'll go to my computer here, and I will try to find you The Birthday Party. 

Here, though, I have two options. I seem to have The Birthday Party by Wendy Dranfield, and The Birthday Party by Laurent Mauvignier. So let me ask you-- if we're on the phone, perhaps-- which one do you want? I'm hearing , feel free to vote, which book should we search for-- the one by Wendy or the one by Laurent? 

I'm hearing, maybe, going for Laurent. So let's try Laurent over here. We'll search for the one by Laurent. So The Birthday Party by Laurent Mauvignier. OK, OK, let me find you that book. But-- well, now there's still two books I could choose from. Do you want it in hardcover or paperback? 

And so I could ask you, again, well, which one do you want? Do you want it in hardcover or paperback? And, again, feel free to vote-- which book do you want? OK, I'm hearing-- we're going for, I think, closer to paperback. Let's try that one. 

So we'll search for The Birthday Party by Laurent Mauvignier in paperback. And [SIGHS] there are still two of them. Which one do you want? We have first edition, and we have second edition. So I would ask you, again, which book do you really want? And you could keep voting here, but for the sake of just keeping this going, let's pause here and think of a better way to do this. 

My life, as a librarian, would be much easier if you had given me a simple number. This number is called an ISBN. And it turns out that every book has a unique identifier called an ISBN. Now, what is an ISBN really? Well, if it's the case that every book has a unique ISBN, and I can only find one book if I have an ISBN, this is what we call in database terms a primary key-- something that is going to be unique for our book or for any item that we have in our table. 

Now, here's one example of an ISBN. Notice how we have a 978-1-8042-- whatever it is. We could use this to uniquely identify, at least, our books. But we could extract this away and use this in more than one place-- not just for books but for publishers, for translators, for authors as well, giving them each some id that uniquely identifies them. 

So here's one example of our table. Let's say that I have a table of books. And I used to only have titles. But now, I actually have more than a title. I have an ISBN to uniquely identify each of these books. And this is handy for me if I wanted to look up some book and know exactly which one I was talking about. 

Now these are all fine and good in tables. They're very helpful. But we could do a little more with them. We could get to this question of, how do we actually relate these tables together? We could use these primary keys for that. 

Now, a primary key becomes useful for that kind of work when we treat it as a foreign key, let's call it. Well, what is a foreign key? Well, a foreign key is simply taking a primary key from one table and including it in the column of some other table. 

So here we have, in the ratings table, the ISBN column still. This is the primary key for the books table. But now notice how it's inside the ratings table. This is now a foreign key because it is outside of this books table and inside the ratings table. And what could I do with this? 

Well, I now see if I want to find all of the individual users ratings for Boulder, I could look-- what is the ISBN of Boulder and, then which ratings correspond to that ISBN in some other table? So this is an example of how we could represent these one-to-many relationships. 

I have, here, a table that has an ISBN, or a list of ISBNs, and I have another table that can tell me which ratings correspond to this ISBN, this primary key in this other table here. 

Well, that solves one picture here. How I can represent these one-to-many relationships? But we could also think about how we do the many-to-many relationships as well. And for this, we'll need to think about how we can improve our primary key here. 

So let me ask. This is an ISBN. But if I want to put this inside of a computer, like, over and over and over again as a primary key-- it's the unique identifier-- what problems do you think I might run into here, if any? What problems would I get by using this ISBN as my primary key? 

SPEAKER: You would, like, run out of memory. 

CARTER ZENKE: Run out of memory-- it's a good guess. If I had a lot of ISBNs-- so, let's say I had not just 78 books, but I had literally millions of books, this is a lot of data to store. If you treated each of these as an individual character, that's about 1 byte, 8 bits per character. That's, let's say, 13 plus four dashes-- 17 bytes per ISBN, which takes up a lot, a lot of space. 

So what if I, instead, said, I'll remove the dashes like we did before. And I'll treat it as a number. Well, in that case, I might also have a problem. Let's say an ISBN begins with 0. And if I convert that to a number, I'll lose that beginning 0 because it doesn't really mean anything in the context of being a number. And now I've lost my unique identifier. 

So we could improve this even further. And we can actually construct our very own primary key. This one, let's just say, will be called 1 for this book. And some other book, we could call it 2, some other book, maybe, 3. And it doesn't quite matter what number we choose so long as this number uniquely identifies the book that we choose and we don't use that number for any other book as well. 

So let's actually rethink this relationship of one-to-many here. Let's not just use ISBN. This is a lot of space to use, to someone point earlier. Let's go ahead and use the id. Let's make our own primary key in our books table and use that as the foreign key in ratings. So we freed up a good amount of space here. 

And notice, too, that maybe Boulder has the primary key, the id of 1. The White Book has the id of 74. Well, does it matter if it's 1, 2, 3, or 4? It doesn't as long as 74 uniquely identifies The White Book, we're OK. 

So here we have an example of a one-to-many relationship but now improved. And with this improvement, we could then think about many-to-many relationships as well. I could take the same idea and use it to relate authors and books. So let's think about this relationship now here too. 

Let's say I have a table of authors and a table of books. And, notably, each has a primary key. So I could use that primary key for authors and for books, and, perhaps, put it in some new table. This one, let's say, is called authored. And I'll have one column for author_id and one column for book_id. 

And based on the context clues here, what might it mean if I looked at the author table and saw 23 next to 1, where 23 is in the author_id column and 1 is in the book_id column? Feel free to raise your hand. What would it mean for me to see those two numbers next to each other? 

SPEAKER: Yeah, it would mean that the author that is read that has the id of 23 has authored the book 1. 

CARTER ZENKE: Yeah, a great instinct here. So if I look at author_id, I see 23. Well, I could consider that maybe the author with the id of 23 wrote the book with the id of 1. And I'll concede there's some extra work here. I have to figure out, now, who has this author idea of 23. Well, it turns out if I look in the author's table, it's Eva. 

Similarly, for the book_id, I now have to go through the process of figuring out, OK, well the book_id is 1. What, then, is the book title? And I'll look for that in my books table over here. So it brings in a bit more work for me. But, ultimately, I think we've solved our problem from the very beginning of lecture, trying to relate authors and books. We can now do that using both primary keys and foreign keys. 

So, let me ask, then, what questions do we have on these keys and how to use them? 

SPEAKER: So if the i-- can the id of the author and the book_id be the same? For example, can there be an author_id of 1 and a book_id of 1, or will they be mixed together? 

CARTER ZENKE: A really good question and good thinking here. So let's consider that, maybe, an author_id matches a book's id. Both authors-- both the author and the book have this id of 1. That's actually, I would say, OK in our case because we know that at least 1 refers to authors and 1 refers to books. 

And as we'll see in future lectures, too, when I make this join table, also called a joint table or a junction table, an associative entity, I could claim that this column called author_id references the primary key column in authors and that primary key only. 

I could do the same thing for the book side. I could say the numbers in here reference the primary keys in the books table and those ids only. So I could actually have authors and books with the same id so long as my tables know that if I have this column, I'm looking for author_ids; this column, I'm looking for book_ids. Great question. Let's go to one more here. 

SPEAKER: I was wondering-- it feels like having more and more tables because once you do this on a big scale, it adds up. It would use up a lot of space as well. How does it-- how do you deal with the tediousness of it adding up? 

CARTER ZENKE: Yeah, a good question here. So if we had a lot of these kinds of tables, wouldn't that take more space? And I think your answer-- the answer to that question is it would, but we do gain some things by being able to do it this way. 

So, for example, let me go back to my authors and books table. In our database, we'll see we have not just author names, but also the year they were born, the city they were born in, the place that they were living in certain periods of their life, and so on. So we could have much more information in these tables that we couldn't store as one table earlier because of all these redundancies we saw a little bit earlier. 

So, I think, although this might take up a little more space, use a little more tables, we can get around that-- as we'll see later on-- with some creativeness with our queries, too, to address that downside but a good question, a good thought for trade-offs here. Let's go to one more here. 

SPEAKER: So my question is that can the id be updated? And if so, does it automatically get updated in the one that has both the ids together? 

CARTER ZENKE: Yeah, good question. So maybe we want to change the id of some book or author. Could we do that? I would say you could, but it's kind of a dangerous game. If I changed Eva from 23, let's say, to-- so we change it to 27, well, I could get Eva confused with Gauz. And I need to be doubly sure that when I'm changing these ids, I'm making sure that I'm not making an id nonunique. I'm not making it an id that somebody else already has. 

And so for that reason, we very rarely change ids. In fact, we tend to just abstract them away. So we don't actually know the id of any particular author or the id of any particular book. We just use them in our queries, as we'll see in just a moment. 

So wonderful questions here. What we'll do is take a very short break and come back to see how we can use these same tools of keys to not just relate tables, but to query them, too, and find answers to our questions across these tables. We'll be back in just a minute. 

Well, we're back. And what we saw before was how to relate our tables using keys. We saw that we could have tables of authors, and translators, and books related to each other using primary keys and foreign keys. 

So what we'll do now is figure out how we can query these tables using different techniques that, in this case, might actually use primary keys and foreign keys within those same queries. 

Now one technique we could use is this one called subqueries, also called nested queries, too, that basically put one SQL query inside of another. And they're useful in a few different cases. But let's say I have one case of a one-to-many relationship. Maybe I have publishers that are publishing many books, for instance. 

Well, I could use subqueries to help me answer questions about these kinds of relationships in my table. To make it more concrete, let's say I have a table of books, and I want to figure out which of these books were published by Fitzcarraldo Editions, my favorite publisher, let's say. What's the problem here? 

I want to find the books published by Fitzcarraldo Editions, but what am I missing? Feel free to raise your hand and answer. 

SPEAKER: Well, we don't have the name of the publisher in the same table. And we haven't made the relationship with the other table to know the name of publisher. 

CARTER ZENKE: Yeah, good observation. So I want to find the books that are published by Fitzcarraldo Editions. And, as you noted, well, there's no publisher name. There's just the id. So I need to have some way of knowing what these ids correspond to. And thankfully, I do have a way of knowing that. 

I have a table called publishers. And this has a column called id and a column called publisher. And what do I notice? Well, I notice that Fitzcarraldo Editions has the id of 5. So I could probably solve this problem. But let me ask again, what queries might I need to answer this question? There are two queries that I need to do to answer the question of, which books were published by Fitzcarraldo Editions? What two queries are they? 

SPEAKER: I think it's SELECT and WHERE. Did you mean keywords or queries? 

CARTER ZENKE: Yeah, so keywords would be great. So I need to have some kind of SELECT involved. I need to probably select something from publishers and something from books. So could I ask you, what would I select from publishers, and what would I select from books then? Let's take either another hand or following up here. 

SPEAKER: OK, so we would take the publisher, so select publisher_id from , WHERE publisher equals, the publisher name we're looking for. And then we would nest this query inside the other one so we can find the name of the book published by this publisher, since we found the id. 

CARTER ZENKE: Yeah, some good ideas here. And let me propose to do it a bit visually here first. So I want to figure out, first, what is the id of Fitzcarraldo Editions? Well, I could write a query to find that. And I'll, say, get back 5 for Fitzcarraldo Editions. Well, that's one step. 

But my next step is then to say, what books fit that publisher_id? So I'll write another query, this one to determine which titles have a publisher_id of 5. And I'll get back, let's say, Minor Detail and Paradais. 

So let's make this more concrete, as you were doing yourself, Jean Paul. And let's write these queries out. Let's say I have this first one to determine what is the id of Fitzcarraldo Editions. I could say SELECT "id" FROM "publishers" WHERE the publisher is Fitzcarraldo Editions. And I'll get back from this query the number 5. 

Well, I could use that number in my next query. If we saw visually here, I could then say, SELECT "title" FROM "books" WHERE "publisher_id" = 5. And I would get, then, back many titles here. 

But here's another question. Why is this not very well-designed? At least, in the query I have here? What could I improve about it? Or what kind of smells wrong about it for you? 

SPEAKER: They are not connected. 

CARTER ZENKE: Yeah, so, Jean-Paul, as you said, too, they're not connected. And here I have this id of 5. But I don't want to remember this number. I don't want to have to keep it in my mind and use it later on in my queries. I, ideally, could use some other query to find this number for me more dynamically. 

And so SQL supports this idea of writing a subquery-- a query within a query. For example, I'll take this, and I'll convert it to the query we had before. I'll SELECT "title" FROM "books" WHERE "publisher_id" is equal to, well, the result of this query here. And notice how I have parentheses. This means the query furthest inside the parentheses will be run first. 

So first, this query is run. I get back 5. Then I could finish out my query and say, SELECT "title" FROM "books" WHERE "publisher_id" is equal to 5. So let me pause here before we do some practice in our SQLite terminal. What questions do we have on these kinds of subqueries so far? 

SPEAKER: I was wondering what would happen with those records that don't match in the subquery? 

CARTER ZENKE: Yeah, good question. So if the id doesn't match-- is that what you're asking? Yeah, I'm going to guess. So if the id doesn't match-- that's a good question. So we can treat it as we would a regular old SQL query that we learned about in last week. 

So we said SELECT "title" FROM "books" WHERE "publisher_id" is equal to, let's say, some value. And we'll then filter out all of those that don't have that particular value. So if we have a publisher_id of 6 or of 3, those won't be included anymore because we said WHERE "publisher_id" is equal to 5. 

And now looking at this query, too, well, let's say, I might write SELECT "id" FROM "publishers" WHERE "publisher" is or equal to 'Fitzcarraldo Editions'. Maybe that publisher doesn't exist. There's no publisher with that name. 

Well, in that case, this query would return nothing. And therefore, the next query would also return nothing. So we have queries dependent on the results of the other queries here. 

So let's actually try this using our SQLite terminal to get a better feel for what we can do with this kind of structure for our queries. I'll go back to my computer. And I'll hop into my SQLite environment. 

Let's say here I want to do a similar query, but I want to find those books that were published by MacLehose Editions-- or MacLehose Press, rather. So let me try to attempt this one-by-one going one step of the way, and then finally combining my queries into one I could use more dynamically. 

So to our point earlier, we have to first find the id of MacLehose Press. Let me try to find that. I'll say SELECT "id" FROM "publisher" where the publisher is equal to none other than 'MacLehose Press,' like this, and my quotes semicolon hit Enter. And hopefully-- oop-- I will see-- I'll see an error. And based on this error-- let me ask our group here-- what did I do wrong? 

SPEAKER: Judging by the error, I think you just mistyped the table name. 

CARTER ZENKE: Yeah, so I probably mistyped the table name. And we could probably parse this if I look at the error itself. So it says "Parse error-- no such table-- publisher." And that's true. There is no table called publisher. So let me fix this and run it again. 

I'll say SELECT "id" FROM the "publishers" table-- plural-- and we'll say WHERE the "publisher" is equal to 'MacLehose Press,' like this. And I'll hit a semicolon here. And now fingers crossed, this should work. I do see an id of 12. OK, So MacLehose Press-- the id is 12. Now I want to find the books that were published by this id. 

So let me go to my book table. I will say SELECT "title" FROM "books", in this case, WHERE the publisher id is equal to 12, as we saw before, semicolon. Now I'll hit Enter. And I'll see these are the books that MacLehose Press has published. 

But, again, as we saw before, I could improve this. I could make this better, more dynamic, by nesting my queries-- having a subquery, a query inside of a query. So let's redo this. 

I'll start at the end, essentially. I'll say SELECT "title" from my book table where the publisher id is or is equal to what? Well, let's say I don't know it's 12. I have to write another query here. So to do that, I could open up some parentheses-- is equal to a parentheses. 

And then I'll hit Enter to continue my query. I'll indent four spaces-- space, space, space, space-- just a style convention to keep things clean for me to show this query is inside of this other query. What I'll then do is finish out this query. 

I want to SELECT the "id" FROM the publisher's table WHERE-- let me just indent again-- WHERE the "publisher" is equal to-- not Fitzcarraldo Editions-- is equal to MacLehose Press, end quote. And now, let me close my parentheses. I have an open one here that I should close to show this subquery is done. 

I'll hit Enter, close my parentheses, and now my entire query is done. I can hit semicolon, hit Enter again. And now I'll see the very same results but more dynamic. No longer do I have to hardcode the id. I can make it more dynamic, and I can actually find it using my very own query here. 

Let's try a different context too. Maybe I want to find all of the ratings for this book called In Memory of Memory. Well, maybe I'll try it step-by-step. And what I'll first do is try to find the id for In Memory of Memory. 

I'll say SELECT "id" FROM-- let's go from the books table-- and let's say WHERE the title is In Memory of Memory, end quote, semicolon, hit Enter. And we'll see 33. So this book has the id 33. 

OK, let's now look in our ratings table for this id. I'll say SELECT-- let's go for SELECT "rating" FROM my ratings table WHERE the "book_id" is equal to 33, I believe it was. So now I'll hit Enter. And now I should see all of the ratings for this book. And there are quite a few that people have left on this book-- on the Goodreads website. 

So let me again try to improve this and make it just a little bit better. I'll be more dynamic about it and try to nest these queries. I'll say SELECT "rating" FROM "ratings". We'll start at the beginning. We ultimately want ratings. 

Well, I want those ratings WHERE the "book_id" is equal to some number, but I don't know what number yet. So I have to write my own nested query. I'll create a parentheses like this, Enter. I'll indent four spaces-- space, space, space, space. And then I'll say I want to find the "id" FROM the "books" table WHERE this "title" is equal to 'In Memory of Memory'. And that is my subquery now. 

So I'll close this out. I'll hit Enter, close my parentheses. Now I have a semicolon and hit Enter. And I see those very same ratings. Well, I could probably not get back the individual ratings. I want to kind of average them over time. So let's try that too. 

I'll say the same thing. SELECT "rating" FROM "ratings", but now, no longer do I want to select all the ratings. I want to average them. So I'll say SELECT the average "rating" of this book FROM "ratings". 

And now, let me go back over to my nested query. And I will hit Enter again. And I will hit the up arrow to get back access to my earlier parts of my SQLite environment. I'll hit Enter here, close it out, semicolon. And now I should see the average rating for this book. 

OK, so this is very handy for us. We're able to kind of replicate those queries we would have done with a single table but now using subqueries. And so far, we've seen this working for a relationship that is one-to-many. We could also use subqueries with many-to-many relationships, these tables that have many items over here and many items over there that relate in some way. 

Let's try it, let's say, with authors and books. And I want to figure out, let's say, which author wrote Flights-- which author wrote Flights. So let me ask, what should I figure out along the way to get to the author who wrote Flights? Could you walk me through what I might need to know for that query, 

SPEAKER: You need to know id of author and of that book. And based on that relation, you have to join all three tables together. 

CARTER ZENKE: Yeah, I have to know ids. And I have to kind of walk across the three tables, as you're saying. So let's go back to our tables. And I want to know, who wrote Flights? 

Well, a good place to start, to your point, is to say, let's start at Flights and find the id. Well, the id of this seems to be 78. Let me then look in our author table. And let me try to find the author id that corresponds with 78. Well, I find 78 here. What's next to it? Well, 58-- so the author id who wrote Flights is 58. Well, who is 58? I'll look in the author's table, and I'll see this is none other than Olga. 

So let's walk through trying to make this query happen but now using SQL keywords. I'll start first with trying to find the id of Flight. So I'll SELECT the "id" FROM the "books" table WHERE the "title" is equal to 'Flights". That's fair enough. 

Now, I could nest this query-- put it inside another query to find the author id of the person who wrote Flights. I'll do it a bit like this. I'll SELECT "author_id" FROM "authored" WHERE the "book_id" is equal to my prior query, SELECT "id" FROM "flights" WHERE "title" is equal to-- or From "books" WHERE "title" is equal to 'Flights'. 

And now I could go one step further. I could say I want to find the name of the person who has this author_id. Let me nest again. Let me put this query-- SELECT "name" FROM "authors" WHERE "id" = and put all the rest of it inside of the nested query here. So to be clear, I'll start from the middle, find the id of Flights. Then, I'll find the author_id for that book_id. And then I'll find the name of the author who wrote that book. 

OK, so a good number of steps here, but let's try it out ourselves in our SQLite terminal. I'll come back to my computer. And here, maybe I want to find all of those books-- or maybe not all of those books. I want to find the author of a particular book you might be familiar with called The Birthday Party from our librarian conversation a little earlier. 

Let me say, I want to first find the id of The Birthday Party. I'll say SELECT "id" FROM "books" WHERE "title" is equal to 'The Birthday Party'; Enter. Now, the id is 8. Let me keep that in mind. And, actually, I don't quite need to know this. Let me try to nest this query inside some other query to keep going towards my goal of finding the author of The Birthday Party. 

So the next thing to figure out, as we saw before, is finding the author_id. I'll say SELECT, let's say, the "author_id" from the "authored" table-- that table of authors who have written books. And I'll say WHERE the "book_id" is none other than the one I got back from this prior query. Let me indent and say SELECT "id" FROM "books" WHERE "title" is equal to 'The Birthday Party'-- not a semicolon yet-- end my parentheses, semicolon, hit Enter. And now I see 44. 

So we're getting there. But now I have to figure out who has the id of 44 in my author's table. Well, let's keep going. Let's clear our terminal using Control-L. And I will then say SELECT the "name" from the "authors" table. We're going to start at the begi-- or we're going to-- yeah, start at the beginning, the place we want to actually get to. 

Then I'll say WHERE the "id" of that author is equal to the result of this query-- what is the author_id associated with the book I want to find. So I'll SELECT "author_id" FROM "authored", and I'll say WHERE the "book_id" is equal to another subquery. Here I'll indent four times and four again. Now I'm nesting twice, right? 

So I'll then say SELECT "id" FROM "books", and I'll hit Enter just to kind of keep me on some good style here. I'll indent eight times total. And then I'll say WHERE-- WHERE-- let me just make sure I'm doing the right thing-- WHERE the "title" is 'The Birthday Party'. That was a lot. 

Now we'll close out our queries. I'll hit Enter, space, space, space again, semicolon-- or parentheses, Enter again, parentheses, semicolon, and, hopefully, after all this typing, we'll get back what we want. We see our friend Laurent Mauvignier. So this is an example of trying to find the author who wrote a particular book, although it's a bit long-winded using these kinds of subqueries. 

So let me pose questions, then. We've seen how to use these subqueries for one-to-many relationships and, also, many-to-many. What questions do you have about how to use these queries? 

SPEAKER: I remember you talking about books of the same name, and how they can have different versions, and et cetera. How would you get the id for the different versions if they are titled the same, as I'm guessing you wouldn't set up a foreign key to a title because they would be the primary. Or is it done differently? 

CARTER ZENKE: A good question here. So you could imagine a database that has more than one edition of a book inside of it. Like maybe I have two editions of The Birthday Party, or the hardcover and the paperback and all these other editions. Well, in that case, what I might do is try to-- actually, this is a good segue. I might have multiple ids that I'm searching for. 

Now let's say I don't care if it's the hardcover or paperback version. Well, I could look for the id of 55 and 56 and try to find the author of both of those. So let's, actually, keep going here. Let me show you a new keyword to use for those kinds of questions if you don't mind. 

Let me come back to my computer. And let's introduce this new keyword that can help us find the author of not just one book but, perhaps, multiple books, or different versions of the same book. Let me introduce this one. This one is called IN-- very simple, just I-N. And I can use IN to say, well, maybe some key or some column is IN some set of values, not just equal to 1, but IN some set of values. 

So let's see an example here. We're back at our authors, books, and authored tables. And maybe I want to find the books written by these two authors, Gauz and Olga. Well, I could select their ids. I could, say, get back 27 and 58. Now I have two ids. 

So I could look in author. And I could say, give me back all of the book ids that have an author_id of 27 and 58. I'll look here. And I'll get back both 4 and 78. So notice how earlier I was asking, show me the book ids where author_id is equal to some single value. Here, I'm asking find me the book ids where book_id has-- or the author_id is in some set of values-- more than one now. 

And, similarly, let me look at my books table. Let me say, OK, I want to find the titles for these books. Well, I'll find the titles that have book ids in this set of ids-- 4 and 78. So let's see this in action in our SQL terminal. I'll come back over here. And I'll write this query to find all of the books by a particular author named Fernanda Melchor. 

So I go back to my terminal. And Fernanda is more prolific than most. She's written, actually, two books that are on the longlist for the Booker Prize. So I'll say SELECT "id" FROM "authors" WHERE the "name" is equal to Fernanda-- 'Fernanda Melchor', semicolon. 

And this now is Fernanda's id-- 24. Let me find the ids of books that Fernanda has written. I will now say SELECT "book_id"-- if I can type-- SELECT "book_id" FROM the "authored" table WHERE the "author_id" is equal to the result of this query-- 1, 2, 3, 4 spaces here. 

And I'll say SELECT "id" FROM "authors" WHERE the "name" is equal to 'Fernanda Melchor', parentheses, semicolon. And I'll hit Enter. And I'll get back not one book id, but two. So if I want to find these titles, I should say, find me the titles where the book_id is not equal to, but is in this set of ids. 

So let's try that. Let me say SELECT "title" FROM "books" WHERE the "id" is IN some set of values-- is IN those two ids we saw earlier. So I'll say IN, Enter-- 1, 2, 3, 4, spaces. And then I'll say SELECT the "book_id" FROM "authored" WHERE-- let me actually space this again-- WHERE the "author_id" is equal to the result of this subquery. 

We can use equals here because there's only one author_id we care about. I'll hit Enter. Then I'll do space, space, space, space-- four spaces for one indentation-- and now four more spaces-- 1, 2, 3, 4-- to indent again to my next nested query. 

I'll then say SELECT the "id" FROM "authors" WHERE the "name" is equal to 'Fernanda Melchor'. And now let me close out my queries. I'll hit Enter, space, space, space, again. And now I'll use parentheses to close out my middle subquery. I'll do the same. I'll hit Enter. And then I'll do another parentheses, and then semicolon here, hit Enter. And now I should see, finally, Fernanda's two books. 

So this is one example of using IN. What questions do you have on how to use this syntax? 

SPEAKER: Actually, my question was not regarding IN, but actually the indentation you use regarding the subqueries because while you are using the subqueries, you mentioned that you are giving four spaces. Is there any necessity of using, like, such kind of indentation while we are using subqueries? 

CARTER ZENKE: Yeah, a great question about style here, and let me try to pull up some slides that have an example of that style so we can talk about it. Let me try to find an example of our nested query. I'll pull this one up. 

And as you might remember, we had three queries here. And I tried to keep track of them by indenting them more and more and more. This isn't required. You could-- I mean, don't do this. But you could put it all on one line, which would just be crazy long to read. 

What we do instead is we will often try to hit Enter when it feels nice to have a break in the reading length. And we'll then indent some spaces to show that this query is a subquery of the prior one. The exact amount to indent might vary, but the idea of trying to break up your lines and trying to indent is going to be a good one for your own sake and for those who read your code. Let's take one more too. 

SPEAKER: When do we need to use IN in WHERE clause when we are doing subquerying? I suppose that we can also use subquerying without IN as well. 

CARTER ZENKE: You're right. So we saw an example using equals. And we all saw an example using IN. In general-- if you want just a rule of thumb to follow-- if you're looking to see if some id is part of a list of ids, or part of a set of ids that is more than one, you should use IN. IN is good for checking if something is inside of more than one item, let's say. 

Equals, though, is good if you know you have only one id. Let's say I have an id equal to 23 or equal to 25. That's a good place for equals. If, though, I had 23 or 25, I might use IN to match either/or of those in that set-- but good question. And let's take one more here too. 

SPEAKER: We have seen one-to-many relationships, one-to-one relationships, and many-to-many relationships. So how would many-to-one relationships be tackled? Suppose one book has three authors. Then how would that be represented in the tables? 

CARTER ZENKE: Yeah, let's look at the example of one book having three authors, for instance. And let's look at our authored table. So let me pull up that slide for you, and we'll talk about it in just a minute. 

I'll come back over here. And I will pull up our example of having authors, and books, and the authored table in the middle. And to your question of, how could I have, let's say, a book written by three authors? Well, we could imagine that this table-- let's say, let's talk about Boulder for instance. 

So Boulder has the id of 1. Let's say three people wrote Boulder. Well, in this case, we could adjust this. I could say this is no longer 74. This is 1. And same thing here-- this is not 4; this is 1. We have the book id 1 in here more than once. It's in here 1, 2, 3 times. 

But what we're saying each time is that, well, 23 was an author of 1. But 31 was an author of 1 as well, and so was 27. So I would not be afraid to have multiple instances of your foreign key inside of this table. What I wouldn't do is have it more than once in your primary key here. 

Here it actually has some information-- who authored which book. Here it is strictly a unique id that should be only a one-to-one relationship. Every key has to be unique for the items in that table. Good questions. 

So we've seen subqueries. But there is one more technique we could use to solve some of these problems of querying across tables. And this one is going to be called a JOIN. So let's dive into JOINs. And the whole idea behind JOIN is trying to take a table and combine it with some other table. 

And, actually, for this, we have some-- I don't know-- maybe some guests for our class. We have these very cute sea lions. And we'll use a database of sea lions to understand how JOINs actually work. 

So if you're not familiar, sea lions are sometimes native to the coast of California. And they like to travel. They like to travel really far. They go from the southern part of California all the way up to Washington State. This is many, many miles of traveling for these adorable sea lions. 

So there are data sets that involve sea lions and their migration patterns. Here's one for example. Here we have a table of sea lions. And here we have a table of their migrations. A distance column tells us how far they went in miles, and a days column tells us how long it took them to travel, of course, in days. 

Well, here, if we were researchers, maybe we're keeping track of some number of sea lions. We're keeping track of Ayah, and Spot, and Tiger, Mabel, Rick, and Jolee. But we have data on many sea lions, perhaps some we aren't even tracking anymore. 

This would be our migrations table. Now it could come to pass that I want to figure out, well, how far did Spot travel? And how far did Tiger travel? And what I could do is I could use nested queries for this. But perhaps, better yet, I could try to join these tables to see the data all in one table. 

Now to do that, how can I try to take a row from this side and kind of attach it to or extend the row here? What idea could I use to put the right rows together in this case? 

SPEAKER: Could you use the primary key, the id, to kind of join them together using the prime key and the foreign key? 

CARTER ZENKE: Yeah, a good idea. So you might notice that we actually have two columns here, both called id, which is handy for us. And notice how we have them kind of sort of matching, and matching in the sense that some of these ids are actually inside of this column too. 

So we could use the primary key in literally both tables here, and try to match it together to figure out how these rows could be extended to add more columns. We could join these tables together to make this table, ultimately, showing us where Ayah has traveled and how long it took them to get there. 

So the keyword for doing these kinds of manipulations with data in SQL is called JOIN-- kind of straightforward. But let's take a peek at what JOIN can do for us inside of this database. 

So I'll go to my computer here. And I'll pull up this database of sea lions that I prepared for us today. I will clear up my terminal. I'll type Control-L. And I'll get out of my longlist database. To do that, I can type dot quit, a SQLite command, to leave this environment. I'll hit Enter. 

And then what I can do is I can type sqlite3 space sea_lions.db. That is just the name of this database. I'll hit Enter. Now, let's make sure I'm in the right place. I could type dot tables to see what tables are inside of this environment-- .tables, Enter. I see both tables-- migrations and sea lions-- which is promising for me here. 

So we could see what data is inside of these tables. I could say SELECT * FROM "sea_lions"; hit Enter. Now I see all of these adorable sea lions inside of this lovely table. What if I wanted to find migration? So I could do that too. 

I could say SELECT * FROM "migrations"; Enter. Now I see my data on migrations. And notice how, again, some sea lions are in the sea lions table. And we have some ids in our migrations table that actually aren't in our sea lions table. So we're keeping track of only a subset of sea lions. And this data might have some sea lions we kept track of in the past, so not all of them as well. 

So let's try joining these tables to determine where have our sea lions been in our sea lions table. I'll say SELECT * FROM "sea_lions". But now I don't want to end this query here. I want to expand this table with the data inside of the migrations table. So what could I do? 

I'll hit Enter, just as a style thing here, to now consider how can we make a query a bit longer? I'll want to JOIN the migrations table to the sea lions table. And to do that, I can type JOIN. 

I'll say JOIN, then space. And I want to say the table I want to JOIN. In this case, the table is called migrations. I'll say "migrations", and I have to tell it one more thing. I have to tell it what we saw visually earlier, which is that the id column in sea lions matches the id column in migrations. I have to tell SQL which two columns to try to JOIN these tables by. 

So let me do that. I'll say JOIN "migrations" ON-- which is a SQL keyword-- what two columns should correspond? I'll now say "migrations" dot "id"-- this means the id column inside of migrations table-- is equal to, or is going to be joined with, this "sea_lions" table and the "id" column within that. 

Again, these two columns should have some matching values that we could use to make these rows longer with more columns. Let me then hit semicolon here. And, hopefully, we'll see all of our data now combined. I can tell you how far Tiger went, and how many days it took them to do it because I've joined these two tables together. 

So in doing this kind of JOIN, just a regular old JOIN, what we're really doing is part of this family of JOINs. They're called an INNER JOIN. You may have seen this idea of an INNER JOIN or an OUTER JOIN. The usual JOIN, at least in SQLite, is going to be an INNER JOIN. And what do we mean by INNER JOIN? 

Well let's visualize it a little more slowly here and see the process of which we might use to understand this JOIN. I'll have, again, my two tables but now simplified. I have name and id, and just distance and id. And to JOIN these, I could literally kind of nudge them together and draw a line down the middle, a bit like this. 

But what do you notice? This one seems to match this id. And this id seems to match this id. But these two-- well, they don't match. I mean poor Jolee down here-- we don't know how far Jolee went. 

And if we don't know this data-- if these ids don't match-- is if we can not find a match for this id or for this id, well, let's sadly just get rid of the row. It's not part of our joined table anymore. It's gone from our memory. We now have only these tables-- or these rows that we could actually JOIN together with the row and the other table here. So, this is our example, then, of an INNER JOIN. Let me ask, what questions do you have on these JOINs so far? 

SPEAKER: So the confusion for me right now is, where were the ids generated? Was it on the sea lions table or on the migrations table? And what kind of problem can that pose, like, maybe, in the real world? So that's the question I have, maybe not directly to JOINs itself. 

CARTER ZENKE: No, that's a great question and good to clarify. So we have sea lions with some id. And we see here that one id is 10484. Another id is 11728. And to your good question-- which is, how do we get these ids-- well, these actually came to us from researchers, perhaps, who are researching sea lions. 

And if you're not familiar, let me go back to our slide with sea lion migrations on it. Researchers might often want to keep track of where sea lions have been. And to do so, they will noninvasively apply some tag to this animal that has some unique id on it. And they'll track where that tag goes to understand where this particular sea lion went. 

So they will make up their very own primary keys, their very own unique ids, to identify these sea lions. We can then use those same ids in our table to understand where these sea lions are going. And just to be clear, too, let me find our full data set here. 

Here, we have those sea lions that we're now interested in, those we're now tracking. But you could imagine that we also have some sea lions that we no longer track, and maybe they've gone on. They're doing something else now. They're not part of our data set. So that's why we might see some over here but not over here. I hope that answers your question about the sources of this data. So let's take one more. 

SPEAKER: When we join together the two migration [INAUDIBLE] the id definitely is repeating. So I just want this and travel distance. I don't want to repeat the table of id. Is that possible? 

CARTER ZENKE: Yeah, and I think-- if I'm understanding correctly-- we want to try to not just JOIN these tables, but maybe remove the duplicate id in them. Like, if I showed you this JOINs table right here, id appears in here twice. There is a way to do this. And we'll see it towards the end of our exploration of JOINs. We'll come back to that in just a minute. 

So we've seen INNER JOIN so far-- this way of combining tables and only keeping the data that actually matches between them. But let's try a new way of joining. This one that might not be so strict. We have a few options here. 

We have what we're going to call a LEFT JOIN, a RIGHT JOIN, and a FULL JOIN. And you could imagine, based on the names here, what each one might do. You could think of our tables-- one being on the left, one being on the right, and trying to JOIN them, prioritizing either the left table or the right table or maybe even both per a FULL JOIN. 

So let's get a feel for what kinds of tables we get back from these different commands. And we'll talk about-- we'll visualize how is this actually happening underneath the hood. Let's go back to our computer here. And let's try to do a LEFT JOIN using our two data sets. 

Now a LEFT JOIN will prioritize, so to speak, the data on my "left table"-- "left" being quote, unquote, because there is no left or right in a database. But left here means the first table that I start with. 

So let's try this. I'll say SELECT *-- and let me just make sure I'm typing the right things here. Let me try SELECT * FROM the "sea_lions" table. And now, I don't want to just do a regular old JOIN. I want to do a LEFT JOIN. I want to, no matter what, always have the data on my left table, this sea lions table here-- LEFT JOIN. 

And I'll JOIN "migrations". I have to say the same thing. Which column in "migrations" corresponds to which column in "sea_lions"? I'll say LEFT JOIN "migrations" ON "migrations" dot "id" = "sea_lions" dot "id" as well. 

Now, I think that's just about it for my JOIN. So I'll say semicolon, Enter. And notice the difference here. Let me walk to this board so we can see it in it's entirety. I have all of my sea lions now in this table. Where we left off Jolee earlier, we've now kept Jolee in, even though Jolee doesn't have a distance or a number of days. We actually haven't tracked that data yet for Jolee, but we still see them in this table. 

Let's now try a RIGHT JOIN to see the difference between this and the RIGHT JOIN. I'll come back over here. And let's try prioritizing our rightmost table. This one, perhaps, being the migrations table. 

So I'll say SELECT * FROM "sea_lions". This will, again, be our left, quote, unquote, table, just because it comes first. Now I'll say JOIN-- not just JOIN. I'll say RIGHT JOIN "migrations" ON, again, "migrations" dot "id" = "sea_lions" dot "id"; now let's see the difference here. 

Well, what have we done? We've actually left off a few sea lions now. We only have those whose ids were in the right table. Again, the right table being that second one we used. And even if we don't have any names for these sea lions, we'll still include them in our data set. We can see, though, that this data is missing and that, as we'll see, it has some special value called null. 

So we have a LEFT JOIN and a RIGHT JOIN. A FULL JOIN, though, allows us to see the entirety of both tables and which values are missing. Let's try that now. I'll come back over here. And I'll do a FULL JOIN. 

I'll say SELECT * FROM "sea_lions" FULL JOIN "migrations" ON "migrations"-- oh, "migrations" dot "id" is equal to "sea_lions" dot "id"; Enter. And now what do we see? Well, we see both tables in their entirety. 

We have Jolee here still, even though Jolee doesn't have a distance or some number of days. We also have our sea lions-- our mystery sea lions down below-- who don't have any name but are still included in our migration table too. So LEFT JOIN, FULL JOIN, and RIGHT JOIN. 

So let's, then, visualize this to understand what's happening along the way. I'll go back to some slides here. And let's look first at these LEFT JOINS as well. So, really, all of these-- LEFT JOIN, RIGHT JOIN, and FULL JOIN-- these are all part of this family called an OUTER JOIN. 

An OUTER JOIN lets you keep some data even if the JOIN is not going to quite work out for you as much as you would want it to in an INNER JOIN. By that, I mean you might have some null or empty values in this JOIN after you run it. So let's visualize it. 

Here I have a LEFT OUTER JOIN. And I want to combine this left table with this right table. I'll do a LEFT OUTER JOIN. I'll put them together. And notice how these two don't match. Well, because they don't match, I'll fill in these values with the value that signifies empty or null. In this case, it is, literally, null. There's nothing here. 

So because I did a LEFT JOIN, what I should do is prioritize this left table as data. Even if this doesn't have any match here, I'll still keep this row. But notice down below that this id has no match in the left table. I'll omit that. And in the end, I'll delete this bottom row. I'll be left with Jolee, who might or may not have data in the right table. 

Let's try the RIGHT JOIN-- RIGHT OUTER JOIN. I'll do the same thing-- combine them. And they'll do the same exact kind of orientation. I have some null values here that I don't quite know how to match up. 

What I can do instead is say, well, I want to prioritize the data on this right-most table. Even though this id has no match, I want to keep it because it's inside this right table. OK, let me delete this row because it has no match in my right table. And I'll be back to this type of JOIN, keeping every id in the right table. 

A FULL JOIN, a bit more simple-- I'll take this same data, JOIN it together, and I'll simply say, I don't care if there are no values involved. I'll leave them be. So this is a lot of visualizing. Let me ask, what questions do we have on these JOINs? 

SPEAKER: Could I see how it would work with multiple tables? Is there, you know, if I have three tables, which one is the left one? Which one is the right one? And what's the third one? 

CARTER ZENKE: Yeah, good question. So we've seen two tables so far. And this was deliberate kind of pedagogically because it would be a lot to see three JOINs all at once. If you're thinking about joining three tables, though, and you're asking which one is your left table, which one is your right table-- always it will be that the table that comes first-- before your JOIN command, your keyword, will be the left table. And the table that's involved in your JOIN keyword, like JOIN "migrations", let's say, that will be your right table. 

And so you can imagine three tables where for the first two, the first one's on the left; the first one's on the right. For the next two, though, the middle one's on the left and the next one is on the right, if that helps you visualize without having much on the board here. Good question. Let's take one more. 

SPEAKER: When we perform the JOIN function, do we get under the hood? Do we have, like, a separate table that's created which we can reference later down in the code? Or do we need to write that entire JOIN command again? 

CARTER ZENKE: Yeah, good question. And so I believe you're asking, do we get back a separate table that we could use? For this I might want to doublecheck myself. But just to kind of show you what we've been doing so far, I'll go back to my SQLite terminal here. 

And I will ask, SELECT * FROM "sea_lions", and let's do a FULL JOIN with "migrations" on "migrations" dot "id" is equal to "sea_lions" dot "id". And I think what you're asking is, do we get back a separate kind of table here? We could consider it as a kind of separate table. 

If I hit Enter here, this is kind of something we're going to call a temporary table, which you could also call a result set. We can use this table for the duration of our query. What we haven't done, though, is made this table accessible in our database itself. This is only there for the duration of this query. So, hopefully, that helps answer it with a bit of fact-checking if you need to as well. 

OK, let's show one final type of JOIN here, this one called a NATURAL JOIN. A NATURAL JOIN kind of allows me to omit the part of my previous JOINs where I was saying "migrations" dot "id" = "sea_lions" dot "id". NATURAL JOIN says, both these columns are called "id". I could just assume that I want you to JOIN by these two columns. 

So let's try a NATURAL JOIN and see what we get back. I'll come back over here. And we'll try a NATURAL JOIN with our sea lions table and our migrations table. I'll say SELECT * FROM "sea_lions". Then I'll NATURAL JOIN "migrations" here. And I no longer need to say "migrations" dot "id" = "sea_lions" dot "id". 

I can just hit semicolon, and now I can hit Enter. So we'll see that the JOIN worked just as we wanted it to. And we didn't even have to specify which id column corresponded to which other id column because these were named the same column name id. Notice, too, we don't get a duplicate id column. 

In some prior JOINs, we had an id column here and an id column here. Now, we've just combined them into one single column, or we've only kept one column among this JOIN here. 

So many kinds of JOINs to use. Many ways to query our tables. What we've seen so far is how to organize our data, build connections between them, and now how to query this data using both subqueries and JOINS. We'll take a quick break here and come back to see how we can use sets and groups to, again, kind of refine our queries and ask more interesting questions too. 

Well, we're back. And now we're going to focus on this idea of sets in SQL. So when you run a query, you get back some results. And those results are often called a result set, some set of values that you've gotten back from your table. 

So let's take a look at what sets are and how we could use them to refine our queries and to find relationships among different groups of people, places, or even things. So let me ask a question of you. Maybe in this world, we have authors and we have translators, at least in the publishing industry, right? If you're in this set, you are an author. If you are in this set, then you are a translator. But what would it be, then, if you were in this set? What does this set mean? 

SPEAKER: It means that you are both the author and the other one-- the translator. 

CARTER ZENKE: Yeah, you're right. So this means you are both an author and a translator. You're in the middle of these two overlapping circles. In SQL, we could represent this kind of relationship using our INTERSECT operator, which we'll see in just a moment. We'll take authors, perhaps, and INTERSECT them with those who are our translators and find those who are both authors and translators. 

Let's do another one then. Let's think of this set. Who are you? Or at least, what does this set represent as a whole? 

SPEAKER: It means that you're either an author or a translator. 

CARTER ZENKE: Nice. You're either an author or a translator. You could be both, too, but you're in either camp. You're either an author or a translator. And for this, we could use a SQL keyword called UNION. I'll take my set of authors and combine them with my set of translators and get back, in this case, the entirety of these two sets. 

Let's look at this one too. If you are in this set, who is included there? 

SPEAKER: Only authors will be included. Authors which are also translators are not being included here. 

CARTER ZENKE: Yeah, good. So here, only authors are included. We see that those who are also translators aren't included. In fact, if you are an author and only an author, then you are in this set. And to get this kind of result, we would use our SQL keyword called EXCEPT. I'll take my set of authors but subtract, or remove, or EXCEPT my set of translators. 

Similarly, I could say, take my set of translators and EXCEPT the set of authors-- subtract them, remove them. And I could do that with translators EXCEPT authors. We'll see these keywords in just a moment. 

Now, I'll have one final question here, which is, how could you represent this? One, I mean, who are you if you are in either this set or this set? And how would you get that kind of set? I actually saved that one for you to do as homework, if I may, before we move on to seeing these in our actual terminal environment. 

So let's take this idea of sets and apply it to authors and translators, this time in our database. I'll come back over to our SQLite terminal. And let me now leave our database of sea lions, sadly. I'll type dot quit and go back to my regular old terminal. 

Now, I want to open back up our longlist.db database-- longlist.db, hit Enter. And now I'm back in the place where I have authors, and books, and publishers inside of this database. I'll type Control-L to clear my terminal. And let's first try to find all of those who are either translators or authors. 

Well, what can I do? I could try this. Let me try SELECT-- SELECT "name" FROM "translators", like this, from my translators table-- semicolon, Enter. These are all of my translators. Now, I want to find authors. 

I could then say SELECT "name" FROM "authors"; hit Enter. Now I have all of my authors. If I wanted, though, to combine these results, these results sets, I could do so using UNION. So let's try it. 

I'll say SELECT "name" FROM "translators" and not finish my query yet. I'll hit Enter, just for style's sake. And I'll say UNION-- UNION with some other result I'll get back from some separate query. I'll hit Enter. 

Now I'll say SELECT "name" FROM-- let's go for "authors" now, end quote, semicolon, hit Enter. And now I'll see both authors and translators. And we should see here that every author and every translator is in here only once. We can assume that we have unique names for these authors and translators. And I could scroll through and figure out who is either an author or a translator-- actually see them both in the same set. 

If I wanted, I could distinguish between "authors" and "translators" by adjusting my query just a little bit. I could say SELECT-- let's go for SELECT 'author', the string, AS "profession" and also select "name" FROM the author's table, semicolon. 

This would give me back not just one column of names, but also another column called profession that has just author inside of it I'll hit Enter. And I'll see I, indeed, have this column-- if I scroll all the way up-- called profession. And I have the value being author. 

Let's combine these. Let's UNION this set with the set of translators and give them their profession too. I'll say SELECT "authors" AS "profession" and then, also, "name" FROM the authors table. And now I'll hit Enter. 

And I'll say UNION that set with the set of translators. I'll say SELECT 'translator', the string, AS the column "profession". Then I'll say "name" FROM the "translators"-- "name" FROM the "translators" table, quote, unquote, semicolon, hit Enter. 

And now I could actually see who is a translator and who is an author. If I scroll through here, I'll see translators. And now, I'll also see authors. So I've combined these two sets into one that works for me here. 

So this is how to UNION, or combine, our sets. But what if we wanted to find only those who are authors and translators, kind of a unique niche group of folks. But who is part of this set? Well, let's try to find out. 

I could SELECT "names" FROM the "authors" table, as I did before. Now, instead of UNION, let me INTERSECT these names with those that will be in the translators column. I'll say INTERSECT and SELECT "name" FROM "translators". And now I'll hit semicolon, Enter. And I'll see one. His name is Ngugi, who is both an author and a translator. They translated their own book into English for the International Booker Prize. 

So let's try now to find those who aren't just translators and authors, but only those who are, perhaps, translators, or only those who are authors. So let's try this. I'll say SELECT "name" FROM "authors", hit Enter. And now I want to EXCLUDE those who are also translators. I'll say EXCEPT, in this case, SELECT "name" FROM "translators", hit semicolon. 

And now I should see-- if I pay close enough attention-- that Ngugi is not in this list. They are an author, and they were in the author set of names. But because they're also a translator, they're not inside this set of list. So this is finding-- good for finding who is in one list, who is in some other list, and who is in-between them. 

But it's also nice for trying to find books people have collaborated on, let's say. Maybe I want to find the books that both Sophie Hughes and Margaret Costa have written together, jointly. So I could try to find, first, the books that Sophie Hughes has translated. 

Let's say SELECT "book_id" FROM the "translated" table-- this table that has translated-- which has translators and books inside of it. And then I'll say WHERE the "translator_id" is equal to this subquery. I'll find Sophie Hughes's id as a translator. 

I'll say SELECT "id" FROM "translators" WHERE the "name" is 'Sophie Hughes', semicolon to end. And these are the book ids that Sophie Hughes has translated because Sophie Hughes is a translator. 

Well, let's see, maybe they have translated some books with Margaret Costa as well. I could try to find out. I'll say SELECT "book_id"-- we'll try to find Sophie's books again. I'll say SELECT "book_id" FROM "translated" WHERE the "translator_id" is equal to, again, Sophie Hughes's "translator_id"-- SELECT "id" FROM "translators" WHERE the "name" is 'Sophie Hughes' like this. 

Now, I'll close out this part of my query. But I want to find the intersection-- the set of book ids that are the same between Sophie Hughes's translated works and Margaret Costa's translated works too. So I'll continue. 

I'll say INTERSECT this result with some other query I'll write now. Let me SELECT the "book_id" FROM the "translated" table WHERE the "translator_id" is equal to a different kind of query. This one will get back the id for Margaret Costa. 

I'll say SELECT "id" from "translators" WHERE the "name" is equal to-- and I believe in this particular case, they go by 'Margaret Jull Costa', like this. Now I'll hit Enter, close out this subquery, and finally, I can hit semicolon. This is the end of my query-- semicolon here. 

And now I'll see the book_id they have collaborated on. You could imagine going beyond this to find the title of this book_id using another nested query. But I won't spend time on that, at least for now, because I'd have to write all this text back out for you. 

So we've seen UNION. . We've seen EXCEPT. We've seen INTERSECT. What questions do you have on these sets and how they work? 

SPEAKER: You've got three JOINs. I just wondered if there was a default that you chose if you didn't know what the situation was, like, which one to use? 

CARTER ZENKE: Yeah, so we saw different kinds of JOINs. We saw LEFT JOIN, RIGHT JOIN, FULL JOIN. And the default, as we saw a little before, is just the simple. JOIN and that JOIN is an example of an INNER JOIN. It'll only take those rows where the ids actually match up. 

You could get more specific and have a LEFT or a RIGHT JOIN or a FULL JOIN. But we'll leave that for you to try out on your own and see the results of, as we did before too, but great question. 

SPEAKER: You mentioned that the ids from both tables were used to match the two tables and we didn't have to whatever duplicate column from id. 

So I was wondering, in a situation whereby the primary key, actually, like, for instance, let's say you're trying to JOIN [? return ?] that table, [? where ?] [? your ?] [INAUDIBLE] is [INAUDIBLE] like a foreign key, how would you go about doing that? 

Because it seems we didn't specify the ids where we wanted to make the JOINs on with the NATURAL JOIN. So I just needed some clarification on that front. 

CARTER ZENKE: Yeah, and let me make sure I'm understanding correctly. So I think you're trying to think about how you would JOIN a table that has a different kind of column name from the other one. And for that, you could use the equals there. And you could say-- we said "migrations" dot "id" = "sea_lions" dot "id". 

But let's say the sea lions id was actually called sea lion underscore id, like the full thing spelled out-- I could say JOIN "migrations" ON "migrations" dot "id" equals "sea_lions" dot "sealions_id" to spell out the column name for SQL. Good question, too. 

SPEAKER: Can I use the INTERSECT and the UNION together between more than two tables, three tables, or four tables? 

CARTER ZENKE: Yeah, you could use intersect more than once, let's say, to intersect more than one set. You absolutely could. And here-- I don't have a good example planned for this. But you could have one query that does one thing-- give you some set. And you type INTERSECT after it. Then you get back the next query. And you find the intersection of that. 

You could then type INTERSECT again to get the intersection of all of these three sets. You can keep going, going, as you'd like to. The key thing here, though, is that in your INTERSECTs, or in your UNIONs, or in your EXCEPT, you always have to have the same number and the same type of columns. 

So if I was trying to combine, let's say, author names with book titles, I can't INTERSECT or UNION those quite well because they have different kind of meanings. They're different kinds of things. So if you're trying to JOIN multiple thing-- trying to JOIN multiple tables or INTERSECT multiple tables, make sure you always have those same column names and those same column types-- the type of data that's stored inside. 

So we've seen sets now. And we're going to conclude by looking at this idea of groups. Well, groups will allow us to recreate some of what we tried to do a little bit of last week, trying to understand the average rating of some books. 

So let's take a look at groups now. Well, you could imagine that I have my ratings table. And in this ratings table, I have book_ids. And I also have ratings. Here, I see that the book-id of 1 has several ratings from people who gave the book a rating. It has 4, 3, and 4. 

And similarly, book-id with 2 has two ratings from folks-- 2 and 3. Now, I want to find the average rating across these ratings for each book_id. So let me try that in my terminal. Come back over here and let me, first, try to find the average rating for each of these books. 

So I'll go back. And I'll say, why don't I SELECT average "rating" FROM my "ratings" table. And I think this should be good enough, so I'll hit semicolon. And I'll see, well, 3.83644. And this seems to be an average. But I wanted the average of each book. So what did I do wrong here? What am I actually seeing in this case? 

SPEAKER: Isn't it an average of all books in the entire table? 

CARTER ZENKE: Yeah, good instinct. So let me try to put back our table here, and we can see what's actually going on. I'll come back over here. And I will show us, again, this table. So we had a table of ratings. And we had the rating column that has individual ratings inside of it. 

When I say SELECT the average rating from this table, well, what am I getting? I'm getting the average of all of these ratings not grouped by book_id. So if I want to find the average rating for each book, I need to employ this idea of groups. And, I mean, wouldn't it be nice if I could do something like this? I could kind of highlight the rows that are part of each group, and then try to average those. 

I could say, take all the books with id 1 and all the books with id 2 and just collapse their ratings, like this. And once you do that, find the average for me, and give me that back as a table. That would be kind of nice. And, luckily, we actually have the capacity to do that with SQL using this GROUP BY keyword. 

So we'll see this in action. I'll come back over here. And let's try to redo this query to find the right answer. I'll come back. And I'll say let's SELECT, in this case, the book_ids and also their average rating. I'll SELECT "book_id". that's one column I want. And I also want the average rating from this column, from this table. 

Now I'll say, let me title this, perhaps, AS "average rating". So I'll get the average rating and just title that column "average rating" exactly. I want to SELECT this FROM the "ratings" table. 

But now, I don't want to simply hit Enter. I'll get back the same thing I did before, which is the average of all the ratings in the ratings table. What I want is for these ratings-- the average ratings-- to be grouped by the book_id. 

So I'll say GROUP BY "book_id"; hit Enter. And now I should be able to see the results I wanted. Let me scroll to the top and notice how using GROUP BY, I was able to take each book_id, collapse the rows-- the ratings that were associated with this book-- and find the average of that rating-- 3.77, 3.97, 3.04-- for each book, so kind of handy here. 

Let me try to improve this and show you one additional thing we could do as well. I'll come back. And why don't I try to replicate what we did last time, which was find the books that have a certain rating or higher. Let's try that. 

I'll say SELECT the "book_id". And let's get, now, the rounded rating-- the rounded average rating. I'll ROUND the average "rating" to two decimal places. And I'll call this "average rating" as a column. 

I'm going to SELECT this FROM my "books" table-- FROM my "ratings" table, sorry. And now I want to GROUP BY the "book_id" to find the average rating for each "book_id". 

Now, though, let's say I only want those books that are pretty well rated, greater than 4.0 out of 5.0 stars. To include a WHERE clause, I could try following up on this GROUP BY. And you might think, I could say, well, WHERE the average-- WHERE "average rating"-- that new column I created-- is greater than or equal to 4.0. 

But I can't because these are now not individual rows. They are groups. SQL uses a different keyword for conditions on groups than for conditions on individual rows. And this keyword is called HAVING-- H-A-V-I-N-G. Let me try that-- H-A-V-I-N-G. I want to GROUP BY the "book_id" and only keep those that have an average rating of greater than 4.0. 

I will scroll over here, and I'll hit Enter. And now I should see a much smaller list. I see "book_id" 5 has a 4.06. 10 has a 4.04, and so on. And now the next step is-- you can imagine me, perhaps, joining these book_ids with another table that has titles inside of it, too, to find the average rating given some title as well. 

So GROUPs allow us to take these columns, collapse some rows, and find aggregate statistics across each of those GROUPs. Let me ask, then, what questions do we have on GROUPs? 

SPEAKER: What if I don't want to see the average rating of a book, but how many ratings does it have? 

CARTER ZENKE: Oh, a good one. So I want to know not the average rating, but the number of reviews, let's say, the number of ratings it was given in my table. Well, for that, I could just modify my query a little bit. I could change average to COUNT because COUNT counts up the number of rows that I have. So let me try that here. 

I'll come back to my laptop. And let me try this one I will SELECT "book_id", and I will also SELECT the COUNT of "book_id" in my-- no, I'll also select the COUNT of "ratings," we're gonna say how many ratings there are-- inside my ratings table-- COUNT("rating") FROM let's say the "ratings" table, like this. 

Now I want to GROUP this data-- GROUP the counting by book_id. So I'll say Group By "book_id"-- give me a count of the ratings for each book_id. And now, I could just hit semicolon and Enter. And now, I'll see how many ratings each book actually has. Let me go to the top here. And I'll see book id 1 has 2,779 ratings. Book_id 2 has 176 ratings, and so on-- a good question. Let's take one more too. 

SPEAKER: So considering these new having syntax, how could we couple that with the ORDER BY? 

CARTER ZENKE: Yeah, where does it fit in with ORDER BY? Like, let's say I want to sort this data, too, at the end of the day. Well, I could do that as well. Let me show you one example. I'll come back to my terminal. 

And I could try this. Let me come back to find the average ratings. So I'll say SELECT "book_id" and the rounded average rating to two decimal places, calling that column "average rating". And I'll SELECT this FROM the "ratings" table. 

Well, now, we want not just to find the average rating. We also want to SORT by that column too. And in fact, use HAVING to only find those books that have 4.0 or higher. Well, let's try this. 

I'll say FROM "ratings", and I'll still GROUP BY "book_id". Now, I'll say I only want to filter to those groups that have a "average rating" of greater than 4.0. And finally, after I've filtered out all of these rows, I want to order them. I want to sort them. 

So I'll order them by "average rating", this column I made up top. And I'll say order them in descending order. I want biggest to smallest. And fingers crossed-- I'll hit Enter, and we'll see our ratings sorted for us-- so great question here to re-implement much of what we did last time. 

And now, indeed, we've kind of come full circle here. We've taken these ideas, and we've seen them in single tables, as we did last week. We-- this week, took our tables, and expanded them into multiple tables-- different authors, different publishers, different ratings, and so on. And we learned how to query those tables using subqueries and using JOINs. 

What we'll see next time is putting you in the driver's seat, having you actually create your own tables, define your own relationships, and build a database to your own liking, so all that and more next time. We'll see you there. 