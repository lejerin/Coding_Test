package day1;

import java.util.ArrayList;

public class Arrays4 {

	public static void main(String[] args) {
		// https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/

		Solution anw = new Solution();
		int[] list = {1,0,2,3,0,4,5,0};
		anw.duplicateZeros(list);
	}
	
 static class Solution {
	    public void duplicateZeros(int[] arr) {
	        
	    
	    	  for(int i=0; i<arr.length-1; i++){
	    	        if(arr[i] == 0){
	    	            for(int j=arr.length-2; j>=i+1; j--){
	    	                arr[j+1] = arr[j];
	    	            }
	    	            arr[i+1] = 0;
	    	            i++;
	    	        }
	    	    }  
	    	}
	    	
	    
	   
	}

}
