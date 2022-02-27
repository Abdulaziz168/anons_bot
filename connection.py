import sqlite3
from sqlite3 import Error


def connect():
    conn = sqlite3.connect('Datas')

    print("Opened database successfully")

    conn.execute("INSERT INTO personal_details (name, last_name, phone_number, description, age) \
          VALUES ('GGGGGGGG', 'UrinbGGGGGGGGoyev', 4545454545, 'Muammo yoq',22)");


    conn.commit()
    print("Table created successfully" )
    conn.close()


if __name__ == '__main__':
    connect()