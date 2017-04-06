class BinarySearch(list):
    
    def __init__(self, length, step): #constructor
        
        super(BinarySearch, self).__init__() # initialising the super class

        for item in range(1, length+1): # populating the class
            self.append(item * step)

        self.length = len(self) # get the length and assign it

    def search(self, val):
        
        # initialising the first and last indices, counter, 
        first = 0
        last = len(self) - 1
        value_index = 0
        found = False

        counter = 0

        # check if val is the first or last element
        if val == self[first]:
            value_index = first
            found = True
        elif val == self[last]:
            value_index = last
            found = True

        # check if val is not present in the list
        if val not in self:
            found = True
            value_index = -1

        # binary search algorithm using a while loop
        while first <= last and not found:
            mid = (first + last) // 2
            if self[mid] == val:
                found = True
                value_index = mid
            else:
                counter += 1  # update counter when an interaction occurs
                if val < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': counter, 'index': value_index}