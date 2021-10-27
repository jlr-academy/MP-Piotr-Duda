#PRODUCTS
GET_PRODUCTS_QUERY = 'SELECT product_ID, name, price, in_stock FROM products'
GET_PRODUCT_NAME_QUERY = 'SELECT name FROM products'
GET_PRODUCT_BY_ID_QUERY = 'SELECT product_ID, name, price, in_stock FROM products WHERE product_id = %s'
UPDATE_PRODUCT_NAME_QUERY = 'UPDATE products SET name = %s WHERE product_id = %s'
UPDATE_PRODUCT_PRICE_QUERY = 'UPDATE products SET price = %s WHERE product_id = %s'
UPDATE_PRODUCT_STOCK_QUERY = 'UPDATE products SET in_stock = %s WHERE product_id = %s'
DELETE_PRODUCT_QUERY = 'DELETE FROM products WHERE product_id = %s'
ADD_PRODUCT_QUERY = 'INSERT INTO products (name, price, in_stock) VALUES (%s, %s, %s)'
#COURIERS

GET_COURIER_QUERY = 'SELECT courier_ID, name, phone FROM couriers'
GET_COURIER_BY_ID_QUERY = ' SELECT courier_ID, name, phone FROM couriers WHERE courier_id = %s'
GET_COURIER_NAME_QUERY = 'SELECT name FROM couriers'
ADD_COURIER_QUERY = 'INSERT INTO couriers (name, phone) VALUES (%s, %s)'
UPDATE_COURIER_NAME_QUERY = 'UPDATE couriers SET name = %s WHERE courier_id = %s'
UPDATE_COURIER_PHONE_QUERY = 'UPDATE couriers SET phone = %s WHERE courier_id = %s'
DELETE_COURIER_QUERY = 'DELETE FROM couriers WHERE courier_id = %s'
GET_CUSTOMERID_FOR_ORDER_QUERY = 'SELECT courier_id FROM orders WHERE order_id = %s'

#ORDERS
GET_ORDER_QUERY = 'SELECT orders.order_id, customers.customer_name, customers.customer_address, customers.customer_phone, couriers.name as courier, orders.status, SUM(order_products.quantity) AS items FROM orders LEFT JOIN customers ON orders.customer_id = customers.customer_id LEFT JOIN couriers ON orders.courier_id = couriers.courier_id LEFT JOIN order_products ON orders.order_id = order_products.order_id GROUP by orders.order_id;'
ADD_ORDER_QUERY = 'INSERT INTO orders(customer_id, courier_id, status) VALUES(%s, %s, %s)'
UPDATE_ORDER_COURIER = 'UPDATE orders SET courier_id = %s WHERE order_id = %s'

#CUSTOMERS
GET_CUSTOMERID_FOR_ORDER_QUERY = 'SELECT customer_id FROM orders WHERE order_id = %s'
GET_CUSTOMER_QUERY = 'SELECT * FROM customers'
ADD_CUSTOMER_QUERY = 'INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES(%s, %s, %s)'
UPDATE_CUSTOMER_NAME_QUERY = 'UPDATE customers SET customer_name = %s WHERE customer_id = %s'
UPDATE_CUSTOMER_ADDRESS_QUERY = 'UPDATE customers SET customer_address = %s WHERE customer_id = %s'
UPDATE_CUSTOMER_PHONE_QUERY = 'UPDATE customers SET customer_phone = %s WHERE customer_id = %s'
DELETE_CUSTOMER_QUERY = 'DELETE FROM customers WHERE customer_id = %s'

#OTHER
GET_ORDER_PRODUCTS_QUERY = 'SELECT order_products.product_id, products.name, order_products.quantity FROM order_products LEFT JOIN products ON order_products.product_id = products.product_id WHERE order_id = %s;'
SELECT_PRODUCTS_MATCHING_ID_QUERY = 'SELECT product_id, COUNT(*) FROM products WHERE product_id = %s'
DELETE_PRODUCTSORDERS_QUERY = 'DELETE FROM order_products WHERE order_id = %s'





