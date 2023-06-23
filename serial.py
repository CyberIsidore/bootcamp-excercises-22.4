class SerialGenerator:
    def __init__(self, start_num, next_num):
        self.start_num = start_num
        self.next_num = next_num
        print(start_num)


    def generate(self):
        if self.next_num is None:
            self.next_num = self.start_num + 1
        else:
            self.next_num = self.next_num + 1
        print(self.next_num)


    def reset(self):
        self.next_num = None
        print(self.start_num)


serial = SerialGenerator(start_num=100, next_num=None)

serial.generate()
serial.generate()
serial.generate()
serial.generate()
serial.generate()
serial.reset()

    # """Machine to create unique incrementing serial numbers.
    #
    # >>> serial = SerialGenerator(start=100)
    #
    # >>> serial.generate()
    # 100
    #
    # >>> serial.generate()
    # 101
    #
    # >>> serial.generate()
    # 102
    #
    # >>> serial.reset()
    #
    # >>> serial.generate()
    # 100
    # """
    #
