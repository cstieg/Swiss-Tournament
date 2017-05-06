#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
from appengine.api.search.ExpressionLexer import NUMBER

def connect():
    """Connect to the PostgreSQL database.  Returns a database cursor."""
    try:
        connection = psycopg2.connect("dbname=tournament")
        cursor = connection.cursor()
        return connection, cursor
    except:
        print "ERROR: Could not connect to the database!"


def deleteMatches():
    """Remove all the match records from the database."""
    connection, cursor = connect()
    cursor.execute("DELETE FROM contest;")
    connection.commit()
    connection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    connection, cursor = connect()
    cursor.execute("DELETE FROM player;")
    connection.commit()
    connection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    connection, cursor = connect()
    cursor.execute("SELECT COUNT(*) FROM player;")
    player_count = int(cursor.fetchone()[0])
    connection.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database. 
    The database assigns a unique serial id number for the player.
    
    Args:
      name: the player's full name (need not be unique).
    """
    connection, cursor = connect()
    cursor.execute("INSERT INTO player (Name) VALUES (%s) RETURNING PlayerID;", (name,))
    connection.commit()
    connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection, cursor = connect()
    cursor.execute("SELECT * FROM player_standings")
    standings = cursor.fetchall()
    connection.close()
    return standings
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection, cursor = connect()
    cursor.execute("INSERT INTO contest (Winner, Loser) VALUES (%s, %s);", (winner, loser))
    connection.commit()
    connection.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    number_of_players = len(standings)
    if number_of_players % 2 != 0:
        print "ERROR: Must have even number of players!"
    pairings = []
    for i in xrange(0, number_of_players, 2):
        evenStanding = standings[i]
        oddStanding = standings[i+1]
        pairings.append((evenStanding[0], evenStanding[1], oddStanding[0], oddStanding[1]))
    return pairings
