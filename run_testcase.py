from Robot import Robot

test_data = []
with open('test.txt', 'r') as file:
    test = file.readlines()
    for row in test:
        test_data.append(row.strip())

for order in test_data:
    print(f"Order: {order}")
    r1 = Robot(order)
    r1.run()
    print('*'*50)