package array;

import java.util.Arrays;

public class Arrays5 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
		
	}

	private class Solution {
	    public void merge(int[] nums1, int m, int[] nums2, int n) {
	        
	    	for(int i=m; i<m+n; i++) {
	    		nums1[i] = nums2[i - m];
	    	}
	    	Arrays.sort(nums1);
	    }
	}
}
