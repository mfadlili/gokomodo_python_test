from Robot import Robot


if __name__ == '__main__':
    order = input("Please write the order for the robot!")
    print(f"Order: {order}")
    r1 = Robot(order)
    try:
        r1.run()
    except:
        print('Invalid order')