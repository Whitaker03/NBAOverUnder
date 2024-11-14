import sqlite3

def initialize_database():
    """
    Create the database and table if they don't already exist.
    """
    conn = sqlite3.connect('nba_teams.db')
    cursor = conn.cursor()

    # Create table for team data
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            average_points_scored REAL NOT NULL,
            average_points_allowed REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_team_data(name, average_points_scored, average_points_allowed):
    """
    Add or update team data in the database.
    """
    conn = sqlite3.connect('nba_teams.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO teams (name, average_points_scored, average_points_allowed)
        VALUES (?, ?, ?)
    ''', (name, average_points_scored, average_points_allowed))

    conn.commit()
    conn.close()

def populate_all_teams():
    """
    Populate the database with all 30 NBA teams and their average points scored/allowed.
    """
    teams = [
        {"name": "Atlanta Hawks", "average_points_scored": 116.2, "average_points_allowed": 121.2},
        {"name": "Boston Celtics", "average_points_scored": 121.3, "average_points_allowed": 110.5},
        {"name": "Brooklyn Nets", "average_points_scored": 111.1, "average_points_allowed": 113.9},
        {"name": "Charlotte Hornets", "average_points_scored": 107.6, "average_points_allowed": 112.6},
        {"name": "Chicago Bulls", "average_points_scored": 115.4, "average_points_allowed": 120.4},
        {"name": "Cleveland Cavaliers", "average_points_scored": 121.8, "average_points_allowed": 110.1},
        {"name": "Dallas Mavericks", "average_points_scored": 114.4, "average_points_allowed": 111.0},
        {"name": "Denver Nuggets", "average_points_scored": 120.9, "average_points_allowed": 118.0},
        {"name": "Detroit Pistons", "average_points_scored": 109.3, "average_points_allowed": 111.8},
        {"name": "Golden State Warriors", "average_points_scored": 121.3, "average_points_allowed": 110.1},
        {"name": "Houston Rockets", "average_points_scored": 111.3, "average_points_allowed": 106.2},
        {"name": "Indiana Pacers", "average_points_scored": 113.8, "average_points_allowed": 116.5},
        {"name": "Los Angeles Clippers", "average_points_scored": 109.7, "average_points_allowed": 109.0},
        {"name": "Los Angeles Lakers", "average_points_scored": 117.6, "average_points_allowed": 117.5},
        {"name": "Memphis Grizzlies", "average_points_scored": 121.1, "average_points_allowed": 112.9},
        {"name": "Miami Heat", "average_points_scored": 110.2, "average_points_allowed": 111.2},
        {"name": "Milwaukee Bucks", "average_points_scored": 111.0, "average_points_allowed": 113.5},
        {"name": "Minnesota Timberwolves", "average_points_scored": 112.0, "average_points_allowed": 109.3},
        {"name": "New Orleans Pelicans", "average_points_scored": 105.4, "average_points_allowed": 115.7},
        {"name": "New York Knicks", "average_points_scored": 114.9, "average_points_allowed": 111.3},
        {"name": "Orlando Magic", "average_points_scored": 107.4, "average_points_allowed": 103.7},
        {"name": "Philadelphia 76ers", "average_points_scored": 106.2, "average_points_allowed": 114.2},
        {"name": "Phoenix Suns", "average_points_scored": 114.3, "average_points_allowed": 113.8},
        {"name": "Portland Trail Blazers", "average_points_scored": 106.8, "average_points_allowed": 114.5},
        {"name": "Sacramento Kings", "average_points_scored": 116.5, "average_points_allowed": 112.5},
        {"name": "San Antonio Spurs", "average_points_scored": 109.8, "average_points_allowed": 109.2},
        {"name": "Toronto Raptors", "average_points_scored": 112.8, "average_points_allowed": 120.0},
        {"name": "Utah Jazz", "average_points_scored": 105.7, "average_points_allowed": 119.0},
        {"name": "Washington Wizards", "average_points_scored": 110.2, "average_points_allowed": 123.4},
    ]

    for team in teams:
        add_team_data(team["name"], team["average_points_scored"], team["average_points_allowed"])

def list_all_teams():
    """
    List all teams currently in the database.
    """
    conn = sqlite3.connect('nba_teams.db')
    cursor = conn.cursor()

    cursor.execute('SELECT name, average_points_scored, average_points_allowed FROM teams')
    teams = cursor.fetchall()
    conn.close()

    print("\nNBA Teams in the Database:")
    for team in teams:
        print(f"Name: {team[0]}, Avg Points Scored: {team[1]:.1f}, Avg Points Allowed: {team[2]:.1f}")

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Populate the database with all 30 teams and their stats
    populate_all_teams()

    # List all teams to verify
    list_all_teams()
