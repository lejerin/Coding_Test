package array;


import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;


public class Solution {
	

	 public int[] solution(String[] nums) {
		 
		 String isNumber = "^[0-9]+$";
		 
		   HashMap<String ,Integer> map = new HashMap<String,Integer>();
		   
		   for(int i=0; i<nums.length; i++) {
			   
			   String[] str = nums[i].split("-");
			   
			   if(str.length > 4) {
				   continue;
			   }
			   if(nums[i].charAt(nums[i].length()-1) == '-'){
				 
				   continue;
			   }
			  
			   boolean isOk = false;
			   String number = "";
			   int count = 0;
			   for(int j=0; j<str.length; j++) {
				  
				   
				   if(str[j].isEmpty()) {
					   isOk = true;
				   }else if(!str[j].matches(isNumber)) {
					   isOk = true;
				   }else {
					   number += str[j].length();
					   count += str[j].length();
				   }
			   }
			   
			
			   
			   if(!isOk && 11<= count && count <= 14) {
				   //유효한 경우에만
				   System.out.println(number);
				   if(map.containsKey(number)) {
					   map.put(number, map.get(number) +1 );
				   }else {

					   map.put(number, 1);
				   }
				   
			   }
			   
		   }
		   
		   Collection<Integer> values = map.values();
		   Integer[] answer = values.toArray(new Integer[0]);
		   Arrays.sort(answer, Collections.reverseOrder());
		   return  Arrays.stream(answer).mapToInt(Integer::intValue).toArray();
	   }

  
}
