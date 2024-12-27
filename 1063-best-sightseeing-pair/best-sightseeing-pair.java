class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int n = values.length ;
        int maxi = Integer.MIN_VALUE;
        
        int a = values[0]-0 ;

        for (int j = 1 ; j < n ; j++){
            if ( values[j]- j + a > maxi){
                maxi = values[j] - j + a ;
            }

            if ( values[j]+ j > a ) 
                a = values[j] + j ;
        }

        return maxi ;


        
    }
}