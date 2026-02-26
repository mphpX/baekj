import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		int st = 0;
		int ed = str.length()-1;
		int ans = 1;
		while(st<ed) {
			if(str.charAt(st)!= str.charAt(ed)) {
				ans = 0;
				break;
			}
			st+=1;
			ed-=1;
		}
		System.out.println(ans);
	}
}
