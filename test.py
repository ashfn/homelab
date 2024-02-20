class int:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        print(other)
        return (self.val*2)+other
    

x = int(4)
print(x+5) # 13