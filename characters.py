#characters will have a name, level, and class
#characters will be stored in characters.db
#characters will be able to be created, deleted, and leveled up

def perform(input, command):
    #split the input into the name, level and class
    args = input.split()
    if len(args) != 3:
        return "Invalid input, please provide a name, level, and class"
    else:
        name = args[0]
        level = args[1]
        class_ = args[2]
        if command == "create":
            return createCharacter(name, level, class_)
        elif command == "levelup":
            return levelUp(name, level)
        elif command == "delete":
            return deleteCharacter(name)
        else:
            return "Invalid command"


def createCharacter(name, level, class_):
    import sqlite3
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    #check if the character already exists
    c.execute("SELECT * FROM characters WHERE name = ?", (name,))
    if c.fetchone() is not None:
        return "Character already exists"
    else:
        #create the character
        c.execute("INSERT INTO characters VALUES (?, ?, ?)", (name, level, class_))
        conn.commit()
        return "Character created"

def levelUp(name, level):
    import sqlite3
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    c.execute("SELECT * FROM characters WHERE name = ?", (name,))
    if c.fetchone() is None:
        return "Character does not exist"
    else:
        #update the level of that character
        c.execute("UPDATE characters SET level = level + 1 WHERE name = ?", (name,))
        conn.commit()
        return "Character level set to " + str(int(level)+1)

def deleteCharacter(name):
    import sqlite3
    conn = sqlite3.connect('characters.db')
    c = conn.cursor()
    c.execute("SELECT * FROM characters WHERE name = ?", (name,))
    if c.fetchone() is None:
        return "Character does not exist"
    else:
        #delete the character
        c.execute("DELETE FROM characters WHERE name = ?", (name,))
        conn.commit()
        return name + " deleted"


