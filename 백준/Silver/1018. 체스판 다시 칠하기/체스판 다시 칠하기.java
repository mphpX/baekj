import java.io.*;
import java.util.*;
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		char[][] chess= new char[n][m];
		String ch;
		for(int i = 0; i < n; i++) {
			ch = br.readLine();
			for(int j = 0; j < m; j++) {
				chess[i][j]= ch.charAt(j);
			}
		}
		char[][][] ans = {
				{{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'}},
				{{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'},{'B','W','B','W','B','W','B','W'},{'W','B','W','B','W','B','W','B'}}};
		int mn = 64;
		int cur= 0;
		for(int x = 0; x < n-7; x++) {
			for(int y = 0; y < m-7; y++) {
				for(int i=0; i <2;i++) {
					cur = 0;
					for(int j = 0; j <8; j++) {
						for(int k = 0; k < 8; k++) {
							if(chess[x+j][y+k]!= ans[i][j][k]) {
								cur+=1;
							}
						}
					}
					mn = Math.min(mn, cur);
				}
			}
		}
		System.out.println(mn);
	
	}
}