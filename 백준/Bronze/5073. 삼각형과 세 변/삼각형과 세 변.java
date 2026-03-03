import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] tri = new int[3];
		StringTokenizer st;
		while(true) {
			st = new StringTokenizer(br.readLine());
			int total = 0;
			for(int i = 0; i < 3; i++) {
				tri[i]= Integer.parseInt(st.nextToken());
				total+= tri[i];
			}
			if(total==0) {
				break;
			}
			int[] mx = {0, 0};
			for(int i = 0; i < 3; i++) {
				if(mx[1]< tri[i]) {
					mx[0]= i;
					mx[1]= tri[i];
				}
			}
			int s= 0;
			int remain = 0;
			for(int i = 0; i < 3; i++) {
				if(i==mx[0]) continue;
				s+=tri[i];
				if(mx[1]!= tri[i])remain= tri[i];
			}
			if(s <= mx[1]) System.out.println("Invalid");
			else {
				if(total == mx[1]*3) System.out.println("Equilateral");
				else if(remain*2+ mx[1]== total || remain+ mx[1]*2 == total) System.out.println("Isosceles");
				else System.out.println("Scalene");
			}
						
		}

	}
}
