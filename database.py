from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order
from app import app, db
from dotenv import load_dotenv
from random import randint
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    
    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)


    i = 1
    while i < 11:
        db.session.add(Table(number=i, capacity=randint(1, 20)))
        i += 1

    db.session.add(dinner)
    db.session.add(employee)
    db.session.commit()
