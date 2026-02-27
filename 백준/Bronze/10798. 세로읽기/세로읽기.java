import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String[] words = new String[5];
		for(int i = 0; i < 5; i++) {
			words[i]= br.readLine();
		}
		for(int i = 0; i < 15; i++) {
			for(int j = 0; j < 5; j++) {
				if(words[j].length() > i) {
					bw.write(words[j].charAt(i));
				}
			}
		}
		bw.flush();
	}
}
