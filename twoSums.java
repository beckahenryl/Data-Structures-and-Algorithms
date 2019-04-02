//solution of pair programmer 4/1/2019
//I did not solve this problem but learned about
//it from pair programmer
import java.util.*;

class Main {
  static public void main( String args[] ) {
    int[] arr = {2, 7, 11,15};
    int target = 13;
    int[] res = twoSum(arr, target);
    System.out.println(res[0] + ", " + res[1]);
    
  }
  
  public static int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) { //i = 0
          int num1 = nums[i]; // num1 = 2
          for (int k = i + 1; k < nums.length; k++) { // k = 1 2
            int num2 = nums[k]; //num2 = 7 11
            if (num1 + num2 == target) { // 9  13
              int[] res = {i, k};
              return res; 
            }
          }
        }
    return null;
    }
}

//https://leetcode.com/problems/two-sum/
//[2, 7, 11, 15] 9
// return [0, 1].


