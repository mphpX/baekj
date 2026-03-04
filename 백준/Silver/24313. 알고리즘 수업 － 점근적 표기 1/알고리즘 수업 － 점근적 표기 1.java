import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int ax = Integer.parseInt(st.nextToken());
		int a = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(br.readLine());
		int n = Integer.parseInt(br.readLine());
		if(ax <= c && ax*n + a <= c*n) {
			System.out.println(1);
		}else System.out.println(0);
	}
}
