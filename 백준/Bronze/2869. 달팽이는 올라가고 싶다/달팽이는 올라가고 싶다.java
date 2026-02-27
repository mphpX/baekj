import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st= new StringTokenizer(br.readLine());
		int a = Integer.parseInt(st.nextToken());
		int b =Integer.parseInt(st.nextToken());
		int v =Integer.parseInt(st.nextToken());
		int days = (v-b + a-b -1)/(a-b);
		
		System.out.println(days);
	}
}