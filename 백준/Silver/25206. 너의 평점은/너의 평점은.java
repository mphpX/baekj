import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		String line;
		double down = 0;
		double top = 0;
		while((line = br.readLine())!= null) {
			st= new StringTokenizer(line);
			st.nextToken();
			double point = Double.parseDouble(st.nextToken());
			
			String str_grade= st.nextToken();

			if(str_grade.charAt(0)== 'P') continue;
			down+= point;
			if(str_grade.charAt(0)=='F') continue;
			double cur = 4- (str_grade.charAt(0)-'A');
			if(str_grade.charAt(1)== '+') cur+=0.5;
			top+=cur*point;
		}
		System.out.printf("%.6f\n",top/down);
		
	}
}