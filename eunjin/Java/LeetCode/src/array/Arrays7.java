package array;

import java.util.Arrays;

public class Arrays7 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/

	}

	private class Solution {
	    public int removeDuplicates(int[] nums) {
	 
	    	int mem = Integer.MAX_VALUE;
	    	int count = 0;
	    	
	    	Arrays.sort(nums);
	    	for(int num: nums) {
	    		if(num != nums[count]) {
	    			nums[count++] = num;
	    		}
	    	}
	    	
	    	return count;
	    	
	    }
	}
}
