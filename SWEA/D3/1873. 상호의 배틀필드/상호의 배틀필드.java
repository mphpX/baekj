import java.io.*;
import java.util.*;
public class Solution {

	static char[][] graph;
	static int N, H, W;
	static int[] dx= {-1, 1, 0, 0};
	static int[] dy= {0, 0, -1, 1};
	static char[] dirs = {'^','v','<','>'};
	static int cur_x, cur_y;
	public static void move(int dir) {
		int next_x = cur_x + dx[dir];
		int next_y = cur_y + dy[dir];
		graph[cur_x][cur_y]= dirs[dir];
		if(0 <= next_x && next_x < H && 0 <= next_y && next_y < W) {
			if(graph[next_x][next_y]== '.') {
				graph[next_x][next_y]=  dirs[dir];
				graph[cur_x][cur_y]= '.';
				cur_x = next_x;
				cur_y = next_y;
			}
		}
	}
	public static void shoot(int dir) {
		int gox= dx[dir];
		int goy= dy[dir];
		int next_x = cur_x + gox;
		int next_y = cur_y + goy;
		while(0 <= next_x && next_x < H && 0 <= next_y && next_y < W) {
			char what = graph[next_x][next_y];
			if(what== '#') {
				break;
			}else if(what == '*') {
				graph[next_x][next_y]='.';
				break;
			}
			gox+=dx[dir];
			goy+=dy[dir];
			next_x = cur_x + gox;
			next_y = cur_y + goy;
		}
	}
	public static void main(String[] args) throws IOException {
		//---------솔루션 코드를 작성하세요.
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for(int tc = 1; tc<=T; tc++) {
			st= new StringTokenizer(br.readLine());
			H = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			graph = new char[H][W];
			for(int i = 0; i < H; i++) {
				String s= br.readLine();
				for(int j = 0; j < W; j++) {
					graph[i][j]= s.charAt(j);
				}
			}
            int idx = 0;
			for(int i = 0; i < H; i++) {
				for(int j = 0; j < W; j++) {
					char sth = graph[i][j];
					if(sth== '^' || sth == '<' || sth == '>'  || sth == 'v') {
                        if(sth == '^') idx = 0;
                        else if(sth == 'v') idx = 1;
                        else if(sth == '<') idx = 2;
                        else idx = 3;
						cur_x = i;
						cur_y = j;
                        
						break;
					}
				}
			}
			N = Integer.parseInt(br.readLine());
			String commands = br.readLine();
			
			for(int i = 0; i < N; i++) {
				char command= commands.charAt(i);
				if(command == 'U') {
					idx = 0;
					move(idx);
				}
				else if(command == 'D') {
					idx = 1;
					move(idx);
				}
				else if(command == 'L') {
					idx = 2;
					move(idx);
				}
				else if(command == 'R') {
					idx = 3;
					move(idx);
				}
				else if(command == 'S') {
					shoot(idx);
				}
			}
			BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
			bw.write('#'+Integer.toString(tc)+ ' ');
			
			for(int i = 0; i < H; i++) {
				for(int j = 0; j < W; j++) {
					bw.write(graph[i][j]);
				}
				bw.write('\n');
			}
			bw.flush();
		}
	}

}
