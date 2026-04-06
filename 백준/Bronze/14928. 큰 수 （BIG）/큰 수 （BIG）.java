import java.util.*;
import java.io.*;
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String num = br.readLine();
		long remain = 0;
		int l = num.length();
		for(int i = 0; i < l; i++) {
			remain =(remain*10 + (long)(num.charAt(i)-'0'))%20000303;
		}
		System.out.println(remain);
	}
}
