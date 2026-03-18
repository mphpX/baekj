import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		Stack<Integer> temp = new Stack<Integer>();
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i< n; i++) {
			arr[i]= Integer.parseInt(st.nextToken());
		}
		int left = 1;
		int idx = 1;
		temp.push(arr[0]);
		boolean isit = true;
		while(idx< n) {
			while(!temp.isEmpty() && temp.peek()== left) {
					left+=1;
					temp.pop();
				}
			temp.push(arr[idx++]);
		}
		
		while(!temp.isEmpty()) {
			if(temp.pop() != left) {
				isit= false;
				break;
			}else {
				left++;
			}
		}
		System.out.println((isit) ? "Nice": "Sad");
		
	}
}	