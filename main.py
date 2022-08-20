from Robot import Robot


if __name__ == '__main__':
    r1 = Robot(input())
    try:
        r1.run()
    except:
        print('Invalid order')