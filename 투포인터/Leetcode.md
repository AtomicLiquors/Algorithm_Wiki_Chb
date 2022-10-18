- 릿코드 Squares of a Sorted Array
    
    [https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/discuss/221922/Java-two-pointers-O(N)](https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/discuss/221922/Java-two-pointers-O(N))
    
- 릿코드 Duplicate Zero
    
    Before:
    
    ```java
    class Solution {
        public void duplicateZeros(int[] arr) {
          
    		int[] temp = new int[arr.length];
    		int max = arr.length;
    		int cnt = 0;
    		int value;
    		for (int i = 0; i < arr.length; i++) {
    			value = arr[i];
    			temp[cnt] = value;
    			cnt++;
    
    			if (value == 0 && cnt != max) {
    
    				temp[cnt] = 0;
    				cnt++;
    			}
    
    			if (cnt == max)
    				break;
    		}
            
            for (int i = 0; i < arr.length; i++) {
                arr[i] = temp[i];
            }
        }
    }
    ```
    
    After:
    
    ```java
    class Solution {
        public void duplicateZeros(int[] arr) {
            for(int i=0;i<arr.length;i++){
                if(arr[i]==0){
                    for (int j=arr.length-1;j>i;j--)
                        arr[j]=arr[j-1];
                    i++;
                }
            }
        }
    }
    ```
    
- 릿코드 Valid Mountain Array
    
    ```java
    if(arr.length < 3) 
    			return false;
    		
    		int start = 0;
    		int end = arr.length - 1;
    		
    		while(start < end) {
    			if (arr[start+1] > arr[start]) {
    				start++;
    			}else if(arr[end - 1] > arr[end]){
    				end--;
    			}else {
    				break;
    			}
    		}
    		return start != 0 && end != arr.length-1 && start == end;
    ```