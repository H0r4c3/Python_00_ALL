my_list = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
        ]

print(sorted(my_list, key=lambda x : x['price'], reverse=True))