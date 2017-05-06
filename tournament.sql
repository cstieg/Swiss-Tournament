-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DELETE DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE player (
	PlayerID 			SERIAL PRIMARY KEY,
	Name				VARCHAR(30)
);

CREATE TABLE contest (
	ContestID			SERIAL PRIMARY KEY,
	Winner				INTEGER REFERENCES player(PlayerID) ON DELETE CASCADE,
	Loser				INTEGER REFERENCES player(PlayerID) ON DELETE CASCADE
	CHECK (winner <> loser)
);

CREATE VIEW player_standings AS \
SELECT player.PlayerID, player.name, \
                    COUNT(CASE contest.Winner WHEN player.PlayerID THEN 1 END) as wins, \
                    COUNT(CASE WHEN player.PlayerID = contest.Winner \
                               OR player.PlayerID = contest.Loser THEN 1 END) as matches \
                    FROM player \
                    LEFT JOIN contest ON player.PlayerID = contest.Winner \
                                      OR player.PlayerID = contest.Loser \
                    GROUP BY player.PlayerID, player.name \
                    ORDER BY wins DESC;