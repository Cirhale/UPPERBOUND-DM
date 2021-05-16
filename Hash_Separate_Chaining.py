class chainHashTable:            #We use List for scratch idea
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
            
    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))
    
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = [key]
            self.data[hashvalue] = [data]
        else:
            dup = False
            for i in range(len(self.slots[hashvalue])):
                if self.slots[hashvalue][i] == key:
                    self.data[hashvalue][i] = data #replace
                    dup = True
                    break
            if dup == False:
                self.slots[hashvalue].append(key)
                self.data[hashvalue].append(data)
      
    def get(self,key):
        hashvalue = self.hashfunction(key,len(self.slots))
      
        data = None
        for i in range(len(self.slots[hashvalue])):
            if self.slots[hashvalue][i] == key:
                data = self.data[hashvalue][i] #replace
                return(data)
                break
            
    
    def hashfunction(self,key,size):
        return key%size
    
    def rehash(self,oldhash,size):
        return (oldhash+1)%size   
    
def main(): 
    
    H=chainHashTable()
    
    H.put(54,"cat")
    H.put(26,"dog")
    H.put(93,"lion")
    H.put(17,"tiger")
    H.put(77,"bird")
    H.put(31,"cow")
    H.put(44,"goat")
    H.put(55,"pig")
    H.put(20,"chicken")    
    
    print(H.slots)        
    print(H.data)
    print(H.get(20))
    
    H.put(20,"duck")
    
    print(H.slots)        
    print(H.data)    
    print(H.get(20))
main()            