import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int num =666;
		while(n!=1) {
			num+=1;
			if(Integer.toString(num).contains("666")) {
				n-=1;
				if(n==1) {
					break;
				}
			}
		}
		System.out.println(num);
	}
}