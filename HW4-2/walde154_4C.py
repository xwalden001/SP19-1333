class Money:
    def __init__(self,dollars =0,cents=0):
        self.dollar = dollars
        self.cent = cents
        self.cleanup()

    def __repr__(self):
        self.cleanup()
        if(self.dollar+self.cent) < 0:
            return '-$%d.%.2d'%(self.dollar*-1,self.cent)
        else:
            return '$%d.%.2d'%(self.dollar,self.cent)

    def cleanup(self):
        if self.dollar < 0:
            self.dollar = (self.dollar)+1
            self.cent = 100 - self.cent % 100
        if self.cent >= 100:
            self.dollar = self.dollar + self.cent // 100
            self.cent = self.cent%100
        else:
            self.cent = self.cent

    def addPenny(self):
        self.cent = self.cent + 1
        self.cleanup()
        return Money(self.dollar,self.cent)

    def __add__(self,obj):
        self.dollar = self.dollar + obj.dollar
        self.cent = self.cent + obj.cent
        self.cleanup()
        return Money(self.dollar,self.cent)

    def __sub__(self,obj):
        self.cent = self.cent - obj.cent
        if self.cent < 0:
            self.dollar -=1
            self.cent = 100 + self.cent
            self.dollar = self.dollar - obj.dollar
        else:
            self.dollar = self.dollar + self.cent//100
            self.cent = 100 - self.cent%100
            self.cleanup()
        return Money(self.dollar, self.cent)


