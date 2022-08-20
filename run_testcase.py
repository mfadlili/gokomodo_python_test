from Robot import Robot


test_data = []
with open('test.txt', 'r') as file:
    test = file.readlines()
    for row in test:
        test_data.append(row.strip())

if __name__ == '__main__':
    for order in test_data:
        print(' ')
        print(f"Order: {order}")
        r1 = Robot(order)
        try:
            r1.run()
        except:
            print('Invalid order')
        