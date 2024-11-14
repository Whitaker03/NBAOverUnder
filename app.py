import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def get_team_data(name):
    """
    Retrieve a team's data from the database.
    """
    conn = sqlite3.connect('nba_teams.db')
    cursor = conn.cursor()

    cursor.execute('SELECT average_points_scored, average_points_allowed FROM teams WHERE name = ?', (name,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return {"name": name, "average_points_scored": result[0], "average_points_allowed": result[1]}
    else:
        return None

def calculate_projected_total(team1, team2):
    """
    Calculate the projected total score for the game based on the teams' averages.
    """
    team1_offense = team1['average_points_scored']
    team1_defense = team1['average_points_allowed']
    team2_offense = team2['average_points_scored']
    team2_defense = team2['average_points_allowed']

    projected_team1_score = (team1_offense + team2_defense) / 2
    projected_team2_score = (team2_offense + team1_defense) / 2
    total_projected_score = projected_team1_score + projected_team2_score

    return total_projected_score

def calculate():
    """
    Calculate the Over/Under suggestion based on user input.
    """
    team1_name = team1_var.get()
    team2_name = team2_var.get()
    over_under_line = over_under_var.get()

    if not team1_name or not team2_name or not over_under_line:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return

    try:
        over_under_line = float(over_under_line)
    except ValueError:
        messagebox.showerror("Input Error", "Over/Under line must be a valid number.")
        return

    team1 = get_team_data(team1_name)
    team2 = get_team_data(team2_name)

    if not team1 or not team2:
        messagebox.showerror("Database Error", "One or both teams not found in the database.")
        return

    projected_total = calculate_projected_total(team1, team2)

    result_text = f"Game: {team1_name} vs. {team2_name}\n" \
                  f"Projected Total: {projected_total:.2f}\n" \
                  f"Over/Under Line: {over_under_line}\n"

    if projected_total > over_under_line:
        result_text += "Suggestion: Bet Over"
    else:
        result_text += "Suggestion: Bet Under"

    result_label.config(text=result_text)

# GUI Setup
root = tk.Tk()
root.title("NBA Over/Under Prediction App")

# Variables
team1_var = tk.StringVar()
team2_var = tk.StringVar()
over_under_var = tk.StringVar()

# Fetch team list from database
conn = sqlite3.connect('nba_teams.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM teams")
teams = [team[0] for team in cursor.fetchall()]
conn.close()

# Widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Select Team 1:").grid(row=0, column=0, sticky=tk.W)
team1_dropdown = ttk.Combobox(frame, textvariable=team1_var, values=teams, state="readonly")
team1_dropdown.grid(row=0, column=1, sticky=tk.W)

ttk.Label(frame, text="Select Team 2:").grid(row=1, column=0, sticky=tk.W)
team2_dropdown = ttk.Combobox(frame, textvariable=team2_var, values=teams, state="readonly")
team2_dropdown.grid(row=1, column=1, sticky=tk.W)

ttk.Label(frame, text="Enter Over/Under Line:").grid(row=2, column=0, sticky=tk.W)
over_under_entry = ttk.Entry(frame, textvariable=over_under_var)
over_under_entry.grid(row=2, column=1, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = ttk.Label(frame, text="", foreground="blue", padding="10")
result_label.grid(row=4, column=0, columnspan=2)

# Run the app
root.mainloop()
