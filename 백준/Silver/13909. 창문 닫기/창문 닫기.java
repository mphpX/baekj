import java.io.*;
import java.util.*;

public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int ans= 0;
		int n = Integer.parseInt(br.readLine());
		for(int i = 1; i<= Math.sqrt(n); i++) {
			ans+=1;
		}
		System.out.println(ans);
	}
}