class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #1 is taken; 0 is empty
        for i in range(len(flowerbed)):
            #can plot if....
            #1)current plot is empty AND 
            #2)first plot OR previous plot is empty AND
            #3)last plot OR next plot is empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) -1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1 #can plant the flower in current plot
                n -= 1 #decrease count of new flowers to be planted
            if n <= 0:  #if we have NO more new flowers to be planted -> return true
                return True
        return False #if you iterated thru the whole flowerbed and still have new flowers left and theres no more space in plot, return False

                
