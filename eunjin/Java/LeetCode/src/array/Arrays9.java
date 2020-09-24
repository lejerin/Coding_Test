package array;

public class Arrays9 {

	//https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

	private class Solution {

		public boolean validMountainArray(int[] A) {

			int up = 0;
			


			for(int i = 1; i<A.length; i++) {

				if(up == 0) {
					if(A[i] > A[i-1]) {
						
						up =1;
					}else {
						return false;
					}
				
				}else if(up == 1) {
					if(A[i] > A[i-1]) {
					
					
					}else if(A[i] < A[i-1]) {
						up = 2;
					}else {
						return false;
					}	
				}else {
					//내려갈 때
					if(A[i] < A[i-1]) {
						
						
					}else {
						return false;
					}
					
				}
		
			}
			
			if(up != 2) {
				return false;
			}
			

			return true;

		}
	}
}
