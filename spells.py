def findSpell(spellName):
    import sqlite3
    conn = sqlite3.connect('spells.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM spells WHERE name = ?", (spellName,))
    spell = curs.fetchone()
    conn.close()
    if(spell == None):
        return "Spell Not Found"
    return spell

#test the findSpell function
#print(findSpell("Bane"))
