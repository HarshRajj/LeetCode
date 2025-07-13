class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort() 
        count = 0
        n = len(players)
        m = len(trainers)
        i = 0
        j = 0
        while i<n and j<m :

            if players[i] <= trainers[j] :
                count += 1
                j+=1 
                i+=1

            else :
                j+=1 
            

        return count 


        

            

        