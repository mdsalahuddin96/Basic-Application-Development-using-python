class box:
    def __init__(self,w,h,d):
        self.width = w
        self.height = h
        self.depth=d
    def box_volume(self):
        return self.width*self.height*self.depth
mybox1 = box(10,10,10)
mybox2 = box(20,20,20)
mybox3 = box(30,30,30)

print("The volume of box1 is:",mybox1.box_volume())
print("The volume of box2 is:",mybox2.box_volume())
print("The volume of box3 is:",mybox3.box_volume())

