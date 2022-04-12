import sqlite3
conn = sqlite3.connect('db/vending-machine.db')

conn.execute(''' Create Table IF NOT EXISTS product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    price INT NOT NULL,
    amount INT NOT NULL
)''')
conn.execute(''' DELETE FROM product ''')
conn.execute('''
    Insert into product(product_name,price,amount) 
    values
    ('coke',15,10),
    ('Pepsi',15,3),
    ('Seven Up', 13,10),
    ('แฟนต้าน้ำแดง', 13,3)
''')

conn.execute('''
    Create table if not exists wallet(
        wallet_id text primary key not null,
        coin_1 int not null,
        coin_5 int not null,
        coin_10 int not null,
        bank_20 int not null,
        bank_50 int not null,
        bank_100 int not null,
        bank_500 int not null,
        bank_1000 int not null
    )
''')
conn.execute(''' DELETE FROM wallet ''')
conn.execute('''
    insert into wallet values
    ("my_wallet",50,20,20,100,20,20,20,2)
''')
conn.commit()
conn.close() 