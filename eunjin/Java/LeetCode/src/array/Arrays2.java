package array;

public class Arrays2 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/

	}

	private class Solution {
	    public int findNumbers(int[] nums) {
	        int count = 0;
	    	
	        
	        for(int num : nums) {
	        	
	        	int digit = (int) (Math.log10(num)+1);
	        	if(digit % 2 == 0) {
	        		count++;
	        	}
	        }
	       
	    	
	        
	        return count;
	    }
	}
	
}
