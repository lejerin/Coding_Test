package day1;

public class Arrays1 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/

	}

	private class Solution {
		public int findMaxConsecutiveOnes(int[] nums) {

			int count = 0;
			int max = 0;
		

			for(int num : nums) {
				if(num == 1) {
					count ++;
				}else {
					count = 0;
				}
			}
			
			if(count > max) {
				max = count;
			}

			return max;

		}
	}
}

