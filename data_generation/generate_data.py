import os
import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker
from sqlalchemy import create_engine

fake = Faker()
records = 5000
restaurants = 50
users = 300

def gen_restaurants(n):
    return [{'restaurant_id': i+1,
             'name': fake.company(),
             'category': random.choice(['Pizza', 'Sushi', 'Indian', 'Burgers', 'Salads'])}
            for i in range(n)]

def gen_users(n):
    return [{'user_id': i+1,
             'full_name': fake.name(),
             'phone': fake.phone_number()} for i in range(n)]

def gen_deliveries(m, users, restaurants):
    deliveries = []
    delivery_items = []
    for i in range(m):
        user = random.randint(1, users)
        rest = random.randint(1, restaurants)
        pickup = fake.date_time_between(start_date='-30d', end_date='now')
        duration = random.randint(10, 60)
        delivered = pickup + timedelta(minutes=duration)
        cancelled = random.random() < 0.07
        deliveries.append({'delivery_id': i+1,
                           'user_id': user,
                           'restaurant_id': rest,
                           'pickup_time': pickup,
                           'delivered_time': None if cancelled else delivered,
                           'is_cancelled': cancelled,
                           'delivery_fee': round(random.uniform(2, 8), 2)})
        items_count = random.randint(1, 5)
        for _ in range(items_count):
            delivery_items.append({'delivery_item_id': len(delivery_items)+1,
                                   'delivery_id': i+1,
                                   'item_name': fake.word(),
                                   'price': round(random.uniform(3, 15), 2),
                                   'quantity': random.randint(1,3)})
    return deliveries, delivery_items

def main():
    print("Generating synthetic food delivery data...")
    restaurants_df = pd.DataFrame(gen_restaurants(restaurants))
    users_df = pd.DataFrame(gen_users(users))
    deliveries_df, delivery_items_df = gen_deliveries(records, users, restaurants)
    deliveries_df = pd.DataFrame(deliveries_df)
    delivery_items_df = pd.DataFrame(delivery_items_df)

    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres:5432/food_delivery')
    restaurants_df.to_sql('restaurants', engine, if_exists='append', index=False)
    users_df.to_sql('users', engine, if_exists='append', index=False)
    deliveries_df.to_sql('deliveries', engine, if_exists='append', index=False)
    delivery_items_df.to_sql('delivery_items', engine, if_exists='append', index=False)
    print("Done!")

if __name__ == '__main__':
    main()
