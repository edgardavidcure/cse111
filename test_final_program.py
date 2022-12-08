from finalprogram import get_prices, select_department, get_order_number, compute_total_cart
import random
import pytest

groceries = {
    "bread" : 3.90,
    "egg": 0.80,
    "milk" : 4.99,
    "apple" : 2.19,
    "banana" : 1.49
}

#Appliances dictionary with items and prices included
appliances = {
    "microwave" : 199.99, 
    "fridge" : 1399.99, 
    "oven" : 799.99, 
    "blender" : 89.99, 
    "tv" : 1099.99

}

#Furniture dictionary with items and prices included
furniture = {
    "couch" : 1899.99, 
    "desk" : 499.99, 
    "chair" : 129.99, 
    "bed" : 899.99, 
    "carpet" : 139.99
}

def test_get_prices():
    department_prices = get_prices(groceries) 
    assert 3.90 in department_prices
    assert 0.80 in department_prices
    assert 2.19 in department_prices
    

    department_prices = get_prices(appliances) 
    assert 199.99 in department_prices
    assert 799.99 in department_prices
    assert 1099.99 in department_prices

    department_prices = get_prices(furniture) 
    assert 1899.99 in department_prices
    assert 499.99 in department_prices
    assert 139.99 in department_prices
    
    




def test_select_department():
    departments = ["groceries", "appliances", "furniture"]
    
    desired = select_department(1)
    assert desired in departments
    desired = select_department(2)
    assert desired in departments
    desired = select_department(3)
    assert desired in departments

def test_compute_total_cart():
    total = compute_total_cart()
    assert total >= 0
    assert isinstance(total, int)

def test_get_order_number():
    order_numbers = [ 3248549, 4358344, 4987934, 8783473, 8947359, 4353478, 9089585, 1238392]
    number = get_order_number()
    assert number in order_numbers


    
        

pytest.main(["-v", "--tb=line", "-rN", __file__])
















