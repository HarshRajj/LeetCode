class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        triplets = set()  # Use a set to avoid duplicate triplets
        
        for i in range(n - 2):  # Fix the first element
            target = -arr[i]
            seen = set()  # Hash set to store complements
            
            for j in range(i + 1, n):  # Iterate through remaining elements
                complement = target - arr[j]
                if complement in seen:
                    # Add the triplet to the set in sorted order
                    triplets.add((arr[i], arr[j], complement))
                seen.add(arr[j])
        
        # Convert the set of tuples to a sorted list of triplets
        return sorted(list(triplets))