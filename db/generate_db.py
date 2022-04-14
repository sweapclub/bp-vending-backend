import sqlite3
conn = sqlite3.connect('./db/vending-machine.db')
try:
    conn.execute(''' DROP TABlE product ''')
except Exception as e:
    print(e)
conn.execute(''' Create Table IF NOT EXISTS product (
    product_id TEXT PRIMARY KEY,
    product_name TEXT NOT NULL,
    price INT NOT NULL,
    amount INT NOT NULL
)''')
conn.execute(''' DELETE FROM product ''')
conn.execute('''
    Insert into product(product_id,product_name,price,amount) 
    values
    ('1','coke',15,10),
    ('2','Pepsi',15,0),
    ('3','ป๊อกกี้ รสช็อกโกแลต', 18,10),
    ('4','ป๊อกกี๊ รสสตรอเบอร์รี', 18,10),
    ('5','ป๊อกกี้ รสคุกกี้และครีม', 18,10),
    ('6','ป๊อกกี้ รสมิลค์กี้มัทฉะ', 18,10),
    ('7','มาม่าหมูสับ', 16,10),
    ('8','Cetaphil', 240,10),
    ('9','เลย์ ลม', 20,10),
    ('10','แบรนด์ยกลัง',185,10),
    ('11','เพนนีโอ', 75,3),
    ('12','แก้วน้ำสูญญากาศ',315,5),
    ('13','Zebra Knife',239,2),
    ('14','หน้ากากอนามัยหนาพิเศษ',69,10),
    ('15','มีโอ',109,2)
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

try:
    conn.execute(''' DROP TABlE report ''')
except Exception as e:
    print(e)
conn.execute(''' create table if not exists report(
    report_ts real primary key not null,
    product_name text not null,
    product_price int not null,
    amount int not null,
    input_money int not null,
    change int not null
)
''')

conn.commit()
conn.close() 