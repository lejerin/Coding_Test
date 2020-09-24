package array;

import java.util.HashSet;

public class Arrays8 {

	//https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
	
	
	private class Solution {
	    public boolean checkIfExist(int[] arr) {
	        
	    	HashSet<Integer> set = new HashSet<>();
	    	for(int a : arr) {
	    		if(set.contains(a*2) || (a%2 == 0 && set.contains(a/2))) return true;
	    		set.add(a);
	    	}
	    	return false;
	    }
	}
	
}
