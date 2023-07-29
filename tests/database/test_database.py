import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)


@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_address_by_name('Sergii')

    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

#Тест для перевірки що значення є правильним типо данних
@pytest.mark.database
def test_incorect_customer_datatype():
    db = Database()
    id = db.select_customers_id(1)
    
    
    assert isinstance(id[0][0], int) #завдяки методу isinstance ми перевіряємо чи є наш обєкт певним типом данних


#Тест який перевіряє чи оновились дані у таблиці customers
@pytest.mark.database
def test_update_customer():
    db = Database()
    db.update_customer('Shtefan', 2)
    select_customer = db.select_customers_name_by_id(2)
    

    assert select_customer[0][0] == 'Shtefan'

#перевірка що QNT є числовим типом данних
@pytest.mark.database
def test_insert_incorect_product_datatype():
    db = Database()
    id = db.select_product_qnt_by_id(1)
    
    
    assert isinstance(id[0][0], int) #завдяки методу isinstance ми перевіряємо чи є наш обєкт певним типом данних


#Перевірка видалення користувача за його іменем
@pytest.mark.database
def test_delete_customer_by_name():
    db = Database()
    db.insert_customers_datatype(5757, 'Viktor', 'Bar 1', 'Bar', 1337, 'Ukraine')
    db.delete_customer_by_name('Viktor') 
    test = db.select_customers_id_by_name('Viktor')  

    assert len(test) == 0 

#Перевірка видалення продукта за його іменем
@pytest.mark.database
def test_delete_product_by_name():
    db = Database()
    db.insert_products(1234, 'тестові', 'дані', 4321)
    db.delete_product_by_name('тестові')  # Метод видалення. Вставляємо айдішку з попереднього запиту.
    test = db.select_product_quantity_by_name('тестові')  #Перевіряємо методом селект

    assert len(test) == 0 #якщо довжина ID == 0 значить що його нема, значить тест пройдений успішно

@pytest.mark.test
def test_select_all_customers():
    db = Database()
    res = db.select_customers_all()

    print("Customers", res)

@pytest.mark.test
def test_select_all_products():
    db = Database()
    res = db.select_products_all()

    print("Products: ", res)


@pytest.mark.test
def test_select_all_orders():
    db = Database()
    res = db.select_orders_all()

    print("Orders: ", res)



















    



