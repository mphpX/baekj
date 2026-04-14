import java.io.*;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException{
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		Map<String, String> map = new HashMap<>();
		map.put("Algorithm", "204");
		map.put("DataAnalysis", "207");
		map.put("Network", "303");
		map.put("ArtificialIntelligence", "302");
		map.put("CyberSecurity", "B101");
		map.put("Startup", "501");
		map.put("TestStrategy", "105");
		for(int i = 0; i < n; i++){
			String name = br.readLine();
			bw.write(map.get(name)+"\n");
		}
		bw.flush();
    }
}