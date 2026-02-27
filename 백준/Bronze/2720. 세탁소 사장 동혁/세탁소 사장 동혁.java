import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] coins = {25, 10, 5, 1};
		int[] ans = new int[4];
		for(int i = 0; i < n; i++) {
			int x = Integer.parseInt(br.readLine());
			for(int j = 0; j < 4; j++) {
				System.out.printf("%d ", x/coins[j]);
				x%= coins[j];
			}
			System.out.println();
		}
	}
}
