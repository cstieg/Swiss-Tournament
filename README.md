# Swiss Tournament

A project by Christopher Stieg for the **Intro to Relational Databases** course,
which is part of the **Full Stack Nanodegree** from
[Udacity.com](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).
It uses the psycopg2 Python library to create a PostgreSQL database representing
a Swiss Tournament.  In the initial round of the tournament, players are seeded
randomly; on successive rounds, the players are matched with players with similar
win/loss records.

## Components
* _tournament.sql_ contains the SQL statements to create the database and tables.
* _tournament.py_ contains the code to add, count, and delete players; record
or delete match results; and return the pairings for the next round.
* _tournament_test.py_ is the test suite provided by Udacity to check proper functionality.

## Getting Started
* Make sure [Python](https://www.python.org/downloads/) 2.7 is installed.
* Install [PostgreSQL](https://www.postgresql.org/download/).
* Install [psycopg2](http://initd.org/psycopg/docs/install.html).
* In the command prompt, navigate to the directory where this repository is located.
* Open PostgreSQL from the command prompt by typing `psql`.
* Initialize the database by typing `\i tournament.sql` at the psql prompt.
* Verify the database has been initialized by typing `\c tournament`.
The table structure can be seen with the command `\dt`.
* Quit the psql environment by typing `\q`.
* Test the module by typing `python tournament_test.py` at the command prompt.
* If desired, use the module to create a frontend!

## License
This project is licensed under the MIT license.
