package array;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Stack;


public class Arrays8 {

	private class Solution {
	   public int[] solution(String s, int[] idx) {
		   int[] answer = new int[idx.length];
		   
		   
		   Stack<Integer> stack = new Stack<>();
		   HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();//HashMap»ý¼º
		   
		   for(int i=0; i<s.length(); i++) {
			   char cur = (char) s.indexOf(i);
			   
			   if(cur == '{') {
				   stack.push(i);
			   }else if(cur == '}') {
				   int match = stack.pop();
				   map.put(i, match);
				   map.put(match, i);
			   }
		   }
		   
		   for(int i=0; i< idx.length; i++) {
			   answer[i] = map.get(idx[i]);
		   }
		   
		   return answer;
 	   }
	}
	
}
