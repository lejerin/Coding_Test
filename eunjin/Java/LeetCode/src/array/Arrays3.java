package array;

import java.util.Arrays;


public class Arrays3 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

	}

	private class Solution {
	    public int[] sortedSquares(int[] A) {
	        
	    	for(int i=0; i< A.length; i++) {
	    		A[i] = A[i]*A[i];
	    	}
	    	
	    	Arrays.sort(A);
	    	
	    	return A;
	    }
	}
}
