-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

CREATE TABLE player (
	PlayerID 			SERIAL PRIMARY KEY,
	Name				VARCHAR(30)
);

CREATE TABLE tournament (
	TournamentID		SERIAL PRIMARY KEY,
	TournamentName		VARCHAR(30),
	TournamentLocation	VARCHAR(30),
	TournamentDate		DATE
);

CREATE TABLE contestant (
	ContestantID		SERIAL PRIMARY KEY,
	PlayerID			INTEGER REFERENCES player(PlayerID),
	TournamentID		INTEGER REFERENCES tournament(TournamentID)
);

CREATE TABLE contest (
	ContestID			SERIAL PRIMARY KEY,
	TournamentID		INTEGER REFERENCES tournament(TournamentID),
	Winner				INTEGER REFERENCES player(PlayerID),
	Loser				INTEGER REFERENCES player(PlayerID)
);

