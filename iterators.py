# creating my own interator

class Counter:
    def __init__(self,limit):
        self.limit=limit
        # built-in value
        self.current=0

    # Iterator protocol
    def __iter__(self):
        return (self)
    
    def __next__(self):
        if self.current<self.limit:
            self.current+=1
            return self.current
        else:
            raise StopIteration

ten=Counter(5)
# print(ten.__iter__())

# for i in ten:
#     print(i)

###### START: Iterator example No. 2 ######

class CountDown:
    def __init__(self, start):
        self.current = start # 5
        
    def __iter__(self): # 5
        # Return the iterator object (self)
        return self # object itself, indicating that it's the iterator.
        
    def __next__(self): # 5
        # Return the next value or raise StopIteration
        if self.current <= 0: # 5<=0
            raise StopIteration # for FOR loop
        self.current -= 1 # 5-1 = 4
        return self.current + 1 # 4+1

rand_num=CountDown(5)
# for num in rand_num:
#     print(num)
    
###### END: Iterator example No. 2 ######

###### START: Implementing Iterator protocol, No. 3 ######

class AKnumbers: # this class is Iterable and iterator!
    # def __init__(self):
        
    
# in Python, an iterator is an object that implements the __iter__ and __next__ methods. 
# So, by returning self, it's saying that the object itself is the iterator.    
    def __iter__(self):
        self.start=0 # not having RESET (self.start=0)  the ITERABLE is itself ITERATOR, otherwise I return a new iterator and can loop over as many times as needed. The itrable get exhausted and then reset again, so sme ITERABLE but a new iterator each time
        print("__iter__")
        return self
    
    def __next__(self):
        if self.start<=20:
            next_num=self.start
            self.start+=2
            return next_num
        else:
            raise StopIteration # 'raise' keyword was mi

    
myClassAK=AKnumbers()
# for iter in myClassAK: # here myClassAK becomes Iterator due to the method __iter__ in the AKnumber class, that returs iterator
#     print(iter)

# for iter in myClassAK:
#     print(iter)


###### END: Implementing Iterator protocol, No. 3 ######

###### START: Implementing Iterator protocol, No. 4 ######

# Separating Iterator and iterable:

# A separate iterable
class myIterable_AK:
    def __iter__(self):
        return myIterator_AK()

# A separate iterator
class myIterator_AK:
    def __init__(self):
        # print("In myIterator_AK invoiking __init__")
        self.start=0
    
    def __iter__(self):
        # print("In myIterator_AK invoiking __iter__")
        return(self)
    
    def __next__(self):
        nextNum=self.start
        # print("In myIterator_AK invoiking __next__")
        if self.start<=20:
            self.start+=2
            return nextNum
        else:
            # print("In myIterator_AK invoiking error: StopIteration")
            raise StopIteration
            
AK_iterable=myIterable_AK()

###### END: Implementing Iterator protocol, No. 4 ######