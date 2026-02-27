import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int ans = 1;
		for(int i = 0; i < n; i++) {
			ans*=4;
		}
		int point = (int)Math.sqrt(ans) +1;
		System.out.println(point* point);
	}
}
