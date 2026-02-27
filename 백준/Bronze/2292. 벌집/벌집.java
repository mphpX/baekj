import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int x = 6;
		int idx = 1;
		int ct= 1;
		
		while(idx < n) {
			idx+=x;
			x+= 6;
			ct+=1;
		}
		System.out.println(ct);
	}
}
