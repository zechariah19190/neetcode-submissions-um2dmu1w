class Solution {
    public int[] productExceptSelf(int[] nums) {

        int[] out = new int[nums.length];
        int x = 1;

        for(int i = 0; i < nums.length; i++){
                x = 1;
            for(int j = 0; j < nums.length; j++){
            
                if(j != i){
                    x *= nums[j];
                }


            }

            out[i] = x;

        }


        return out;
    }
}  
