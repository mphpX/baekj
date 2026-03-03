import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] tri = new int[3];
		int total = 0;
		for(int i = 0; i < 3; i++) {
			tri[i]= Integer.parseInt(br.readLine());
			total+=tri[i];
		}
		if(total!=180) {
			System.out.println("Error");
		}else {
			boolean isit = false;
			for(int i = 0; i< 3; i++) {
				for(int j = i+1; j <3; j++) {
					if(tri[i]== tri[j]) {
						isit= true;
						break;
					}
				}
			}
			if(isit && tri[0]== 60) {
				System.out.println("Equilateral");
			}else if(!isit) {
				System.out.println("Scalene");
			}else {
				System.out.println("Isosceles");
			}
		}
		
	}
}
