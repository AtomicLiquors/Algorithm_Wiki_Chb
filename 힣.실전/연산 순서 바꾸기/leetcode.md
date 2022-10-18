- 
    
    Before : 2ms짜리
    
    ```java
    class Solution {
        public int[] sortArrayByParity(int[] nums) {
    		int pt1=0;
    		int pt2 = nums.length-1;
    		int tmp;
    		
    		while(pt1 != pt2) {
    			if (nums[pt1]%2==0) {
                    pt1++;
    			}else {
    				tmp = nums[pt2];
    				nums[pt2] = nums[pt1];
    				nums[pt1] = tmp;
    				pt2--;
    			}
    		}
    		
    		return nums;
    		
    	}
    }
    ```
    
    After : 1ms짜리
    
    ```java
    class Solution {
        public int[] sortArrayByParity(int[] nums) {
    		int pt1=0;
    		int pt2 = nums.length-1;
    		int tmp;
    		
    		while(pt1 != pt2) {
    			if (nums[pt1]%2==0) {
                    pt1++;
    			}else {
    				tmp = nums[pt2];
    				nums[pt2] = nums[pt1];
    				nums[pt1] = tmp;
    				pt2--;
    			}
    		}
    		
    		return nums;
    		
    	}
    }
    ```