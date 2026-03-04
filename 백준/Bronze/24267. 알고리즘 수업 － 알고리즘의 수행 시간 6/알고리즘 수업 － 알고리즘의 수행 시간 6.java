import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long n = Integer.parseInt(br.readLine());
		System.out.printf("%d\n3", (n-2)*(n-1)*(2*n-3)/12 + n*n*(n-2)/2 - n*(n-2)/2+ (1-2*n)*(n-2)*(n-1)/4);
	}
}