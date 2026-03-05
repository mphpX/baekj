import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		String[] words = new String[n];

		for(int i = 0; i < n; i++) {
			words[i]= br.readLine();
		}
		Arrays.sort(words, (a,b)->{
			if(a.length()!= b.length()) return Integer.compare(a.length(), b.length());
			return a.compareTo(b);
		});
		bw.write(words[0]);
		bw.write("\n");
		for(int i = 1; i < n; i++) {
			if(words[i-1].equals(words[i])) continue;
			bw.write(words[i]);
			bw.write("\n");
		}
		bw.flush();
	}
}