-- init.sql: create tables for food delivery analytics
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id SERIAL PRIMARY KEY,
    name TEXT,
    category TEXT
);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name TEXT,
    phone TEXT
);

CREATE TABLE IF NOT EXISTS deliveries (
    delivery_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    restaurant_id INT REFERENCES restaurants(restaurant_id),
    pickup_time TIMESTAMP,
    delivered_time TIMESTAMP,
    is_cancelled BOOLEAN DEFAULT FALSE,
    delivery_fee NUMERIC(6,2)
);

CREATE TABLE IF NOT EXISTS delivery_items (
    delivery_item_id SERIAL PRIMARY KEY,
    delivery_id INT REFERENCES deliveries(delivery_id),
    item_name TEXT,
    price NUMERIC(6,2),
    quantity INT
);
