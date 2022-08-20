class Robot:
    def __init__(self, message):
        message_list = message.split(' ')
        try:
            position = message_list[1].split(',')
            self.order = message_list[2:]
            self.X = int(position[0])
            self.Y = int(position[1])
            self.direction = position[2].upper()
            self.degree = self.direction_to_degree()
        except:
            print('Syntax Error')

    def direction_to_degree(self):   
        if self.direction == 'NORTH':
            return 0
        elif self.direction == 'EAST':
            return 90
        elif self.direction == 'SOUTH':
            return 180
        elif self.direction == 'WEST':
            return 270
    
    def degree_conv(self):
        if self.degree >= 360 :
            self.degree -= 360
            return self.degree_conv()
        elif self.degree < 0 :
            self.degree += 360
            return self.degree_conv()
        elif self.degree >= 0 and self.degree < 360:
            return self.degree

    def degree_to_direction(self):
        if self.degree == 0:
            return 'NORTH'
        elif self.degree == 90:
            return 'EAST'
        elif self.degree == 180:
            return 'SOUTH'
        elif self.degree == 270:
            return 'WEST'
    
    def move_robot(self):
        for i in self.order:
            if i.lower() == 'move':
                if self.direction == 'EAST' and self.X<5:
                    self.X += 1
                elif self.direction == 'WEST' and self.X>0:
                    self.X -= 1
                elif self.direction == 'NORTH' and self.Y<5:
                    self.Y += 1
                elif self.direction == 'SOUTH' and self.Y>0:
                    self.Y -= 1

            elif i.lower() == 'left':
                self.degree -= 90 
            elif i.lower() == 'right':
                self.degree += 90
            
            self.degree = self.degree_conv()
            self.direction = self.degree_to_direction()
        
    def run(self):
        self.move_robot()
        print('Robot Last Position:')
        print(f'{self.X},{self.Y},{self.direction}')

    def new_order(self, new_order):
        self.order = new_order.split(' ')
        self.run()
