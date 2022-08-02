class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        middle = 0
        temp = x
    
        while(start < temp):
            middle = int((start+temp)/2)
            if(middle * middle == x):
                return middle
            if(x < middle * middle):
                temp = middle -1
            else:
                start = middle + 1
            
        return temp - 1 if x < temp * temp else temp
        
        