import java.io.*;
import java.util.*;
public class Main {
	static Stack<Integer> stack;
	public static void num(int a) {
		stack.push(a);
	}
	public static void pop() {
		stack.pop();
	}
	public static void inv() {
		int a =stack.pop();
		stack.push(-a);
	}
	public static void dup() {
		int a = stack.peek();
		stack.push(a);
	}
	public static void swp() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		for(int i = 0; i < 2; i++) {
			stack.push(tmp[i]);
		}
	}
	public static boolean add() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		long result = (long)tmp[0]+ tmp[1];
		if(-1000000000 > result || result > 1000000000) {
			return true;
		}
		stack.push((int)result);
		return false;
	}
	public static boolean sub() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		long result = (long)tmp[1]- tmp[0];
		if(-1000000000 > result || result > 1000000000) {
			return true;
		}
		stack.push((int)result);
		return false;
	}
	public static boolean div() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		if(tmp[0]==0) return true;
		int result = Math.abs(tmp[1]/tmp[0]);
		stack.push((tmp[1]<0)^(tmp[0]<0) ? -result : result);
		return false;
	}
	public static boolean mul() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		long result = (long)tmp[1]* tmp[0];
		if(-1000000000 > result || result > 1000000000) {
			return true;
		}
		stack.push((int)result);
		return false;
	}
	public static boolean mod() {
		int[] tmp = new int[2];
		for(int i = 0; i < 2; i ++) {
			tmp[i]= stack.pop();
		}
		if(tmp[0]==0) return true;
		int a = Math.abs(tmp[1]/tmp[0]);
		a= (tmp[1]<0)^(tmp[0]<0) ? -a : a;
		stack.push(tmp[1]- tmp[0]*a);
		return false;
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		String com = br.readLine();
		int N;
		ArrayList<String> commands;
		String line;
		boolean err= true;
		while(!com.equals("QUIT")) {
			commands = new ArrayList<>();
			while(!com.equals("END")) {
				commands.add(com);
				com= br.readLine();
			}
			N= Integer.parseInt(br.readLine());
			for(int i = 0; i < N; i++) {
				stack = new Stack<>();
				stack.push(Integer.parseInt(br.readLine()));
				err= false;
				for(int j = 0; j < commands.size(); j++) {
					if(err) break;
					line = commands.get(j);
					st = new StringTokenizer(line);
					com = st.nextToken();
					switch(com) {
					case "NUM":
						num(Integer.parseInt(st.nextToken()));
						break;
					case "POP":
						if(stack.isEmpty()) {
							err= true;
						}else {
							pop();
						}
						break;
					case "INV":
						if(stack.isEmpty()) {
							err= true;
						}else {
							inv();
						}
						break;
					case "DUP":
						if(stack.isEmpty()) {
							err= true;
						}else {
							dup();
						}
						break;
					case "SWP":
						if(stack.size()<2) {
							err=true;
						}else {
							swp();
						}
						break;
					case "ADD":
						if(stack.size()<2) {
							err=true;
						}else {
							err = add();
						}
						break;
					case "SUB":
						if(stack.size()<2) {
							err=true;
						}else {
							err= sub();
						}
						break;
					case "MUL":
						if(stack.size()<2) {
							err=true;
						}else {
							err= mul();
						}
						break;
					case "DIV":
						if(stack.size()<2) {
							err=true;
						}else {
							err= div();
						}
						break;
					case "MOD":
						if(stack.size()<2) {
							err=true;
						}else {
							err= mod();
						}
						break;
					}
				}
				if(stack.size()!=1 || err) {
					bw.write("ERROR\n");
				}else {
					bw.write(stack.pop()+"\n");
				}
			}
			bw.write("\n");
			com= br.readLine();
			com= br.readLine();
		}
		bw.flush();
	}
}	