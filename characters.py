def perform(input, command):
    # we want the ability to create, delete and modify characters
    import sqlite3
    conn = sqlite3.connect('characters.db')
