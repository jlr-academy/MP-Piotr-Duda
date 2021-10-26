GET_PRODUCTS_QUERY = 'SELECT product_ID, name, price, in_stock FROM products'
GET_COURIER_QUERY = 'SELECT courier_ID, name, phone FROM couriers'
GET_ORDER_QUERY = 'SELECT order_ID, customer_name, customer_address, customer phone, courier, status, items FROM orders'
SELECT_PRODUCTS_MATCHING_ID_QUERY = 'SELECT product_id, COUNT(*) FROM products WHERE product_id = %s'