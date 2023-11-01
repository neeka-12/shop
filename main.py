import sqlite3

conn = sqlite3.connect("Mycontacts.db")
cursor = conn.cursor()

cursor.execute()

contacts_data = [
    ("John Doe",'+123456789','doehojhn@mail.com'),
    ('Marta Noi','+12736456','marta@gmail.com'),
    ('Rob Wizar','+12957434','robinro@gmail.com'),
    ('Linda Wowk','+1222834','lili12@mail.com')
]

cursor.executemany('INSERT INTO Contacts(name,phone_number,email) VALUES (?,?,?)',contacts_data)

conn.commit()

cursor.execute('SELECT * FROM Contacts')
all_contacts = cursor.fetchall()
print("All contacts:")
for contact in all_contacts:
    print(contact)

cursor.execute('SELECT name, phone_number FROM Contacts WHERE phone_number LIKE "+1%"')
contacts_with_country_code = cursor.fetchall()
print("\nContacts with country code +1:")
for contact in contacts_with_country_code:
    print(contact)

cursor.execute('SELECT * FROM Contacts WHERE email LIKE "%gmail%')
gmail_contscts = cursor.fetchall()
print("\nContacts with Gmail email:")
for contact in gmail_contscts:
    print(contact)

update_id = 1
new_name = 'Updated Name'
new_phone_number = '+99989999'
cursor.execute('UPDATE Contacts SET name = ?, phone_number = ? WHERE id = ?',(new_name,new_phone_number))
conn.commit()

delete_id = 3
cursor.execute('DELETE FROM Contacts WHERE id =?',(delete_id))
conn.commit()
conn.close()