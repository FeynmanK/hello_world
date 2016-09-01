class student(object):
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
    def printfunction(self):
        print self.name,self.sex
def prime(x):
    for i in range(x):
        print i,
sb=student('sb','man')
sb.printfunction()