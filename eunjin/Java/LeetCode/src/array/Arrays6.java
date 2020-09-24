package array;


import java.util.Arrays;
import java.util.List;


public class Arrays6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

	private class Solution {
	    public int removeElement(int[] nums, int val) {
	        int count = 0;
	       
	        for(int num : nums) {
	        	if(num != val) {
	        		nums[count++] = num; 
	        	}
	        }
	        
	        return count;
	    	
	    }
	}
}
