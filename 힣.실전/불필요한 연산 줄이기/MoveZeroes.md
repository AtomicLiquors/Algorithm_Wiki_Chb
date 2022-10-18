- 릿코드 Move Zeroes
    
    **Before:**
    
    ```java
    class Solution {
        public void moveZeroes(int[] nums) {
            int i = 0;
    		int j = 0;
    		
    		while(j < nums.length){
    			//첫 항이 0인 경우.
            	//첫 항이 0이 아닌 경우.
            	if(nums[j] != 0) {
            		nums[i] = nums[j];
            		i++;
            	}
            	j++;
    
            	//j가 끝까지 탐색하면
            	//i부터 j까지 i++, 0을 채운다.
    		}
    		
    		while (i < nums.length) {
    			nums[i] = 0;
    			i++;
    		}
        }
    }
    ```
    
    i를 굳이 바꿀 필요가 없는데도 바꾸는 연산을 할 때가 있다.
    
    **After:**
    
    ```
    class Solution {
        public void moveZeroes(int[] nums) {
            for (int i = 0, s = 0; i < nums.length; i++) {
                if (nums[i] != 0 && s++ < i) {
                    nums[s-1] = nums[i];
                    nums[i] = 0;
                }
            }
        }
    }
    ```