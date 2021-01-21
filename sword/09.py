class CQueue(object):

    def __init__(self):
        self.tmp_stack=[]
        self.value_stack=[]

    def conver_stack(self,x,y):
        for i in range(len(x)):
            y.insert(0,x.pop())


    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.conver_stack(self.value_stack,self.tmp_stack)
        self.value_stack.insert(0,value)
        self.conver_stack(self.tmp_stack,self.value_stack)
        # print self.value_stack



    def deleteHead(self):
        """
        :rtype: int
        """
        if self.value_stack:
            return self.value_stack.pop(0)
        else:
            return -1
        # print self.value_stack

if __name__ == '__main__':
    a=CQueue()
    print a
    print a.deleteHead()
    print a.appendTail(5)
    print a.appendTail(2)
    print a.deleteHead()
    print a.deleteHead()

