import sqlite3


class Database():

    def __init__(self) -> None:
        self.connection = sqlite3.connect('C:\\Users\\User\\Valentyn_QA_AUTO\\become_qa_auto.db') #це потрібно для взаємодії з БД
        self.cursor = self.connection.cursor() #А це виконує наші команди в БД


    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
#Методи для індивідуального завдання
    def insert_products_datatype(self, id, name, description, quantity):
        insert_incorect = f"INSERT  OR REPLACE INTO products (id, name, description, quantity) \
        VALUES ({id}, '{name}', '{description}', {quantity})"
        self.cursor.execute(insert_incorect)
        self.connection.commit()

    def select_product_all_by_id(self, product_id):
        sqlite_select = f'SELECT * FROM products WHERE id = {product_id}'
        self.cursor.execute(sqlite_select)
        result = self.cursor.fetchall()

    def update_customer(self, new_customer_name, customer_id):
        update_customer = f'UPDATE customers SET name = "{new_customer_name}" WHERE id = {customer_id}'
        self.cursor.execute(update_customer)
        self.connection.commit()

    def select_customers_all_by_id(self, product_id):
        sqlite_select = f'SELECT * FROM customers WHERE id = {product_id}'
        self.cursor.execute(sqlite_select)
        result = self.cursor.fetchall()

        return result
    
    def select_customers_name_by_id(self, product_id):
        sqlite_select = f'SELECT name FROM customers WHERE id = {product_id}'
        self.cursor.execute(sqlite_select)
        result = self.cursor.fetchall()

        return result

    def insert_customers_datatype(self,id, name, address, city, postalCode, country):
        insert_incorect_customers = f"INSERT  OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
        VALUES ({id}, '{name}', '{address}', '{city}', {postalCode}, '{country}')"
        self.cursor.execute(insert_incorect_customers)
        self.connection.commit()

    
    def delete_customer_by_name(self, customer_name):
        delete = f'DELETE FROM customers WHERE name = "{customer_name}"'
        self.cursor.execute(delete)
        self.connection.commit()   
    
    def select_customers_id_by_name(self, customer_id):
        sqlite_select = f'SELECT id FROM customers WHERE name = "{customer_id}"'
        self.cursor.execute(sqlite_select)
        result = self.cursor.fetchall()

        return result
    
    

    def delete_product_by_name(self, product_name):
        delete = f'DELETE FROM products WHERE name = "{product_name}"'
        self.cursor.execute(delete)
        self.connection.commit()

    def select_product_quantity_by_name(self, product_name):
        sqlite_select = f'SELECT quantity FROM products WHERE name = "{product_name}"'
        self.cursor.execute(sqlite_select)
        result = self.cursor.fetchall()

        return result

    def insert_products(self, product_id, name, description, quantity):
        # insert = f'INSERT INTO products (id, name, description, quantity) \
        #     VALUES ({product_id}, "{name}" , "{description}" , {quantity})' #Якщо в форматі юзаєш STR то навіть формат треба брати в лапки
        #Отут знизу інсерт лише втсавляє дані. Знизу запит спробує вставити дані, якщо унікальність порушена то він просто замінить ті дані
        insert = f'INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, "{name}" , "{description}" , {quantity})' #Якщо в форматі юзаєш STR то навіть формат треба брати в лапки
        self.cursor.execute(insert)
        self.connection.commit() #підтвердження змін в БД

    def select_customers_all(self):
        select = 'SELECT * FROM customers'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    def select_customers_all(self):
        select = 'SELECT * FROM customers'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    def select_products_qnt_by_id(self, id):
        select = f'SELECT quantity FROM products where id = {id}'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    def select_customers_id(self, id):
        select = f'SELECT {id} FROM products'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    def select_products_all(self):
        select = 'SELECT * FROM products'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    def select_orders_all(self):
        select = 'SELECT * FROM orders'
        self.cursor.execute(select)
        result = self.cursor.fetchall()

        return result
    
    









