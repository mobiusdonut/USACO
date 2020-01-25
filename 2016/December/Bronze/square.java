import java.util.*;
import java.io.*;

public class square {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new FileReader("square.in"));
    PrintWriter out = new PrintWriter(new FileWriter("square.out"));
		StringTokenizer str = new StringTokenizer(br.readLine());
    int x1 = Integer.parseInt(str.nextToken());
    int y1 = Integer.parseInt(str.nextToken());
    int x2 = Integer.parseInt(str.nextToken());
		int y2 = Integer.parseInt(str.nextToken());
		str = new StringTokenizer(br.readLine());
    int x3 = Integer.parseInt(str.nextToken());
    int y3 = Integer.parseInt(str.nextToken());
    int x4 = Integer.parseInt(str.nextToken());
    int y4 = Integer.parseInt(str.nextToken());

		int xmin = Math.min(Math.min(x1, x2), Math.min(x3, x4));
		int xmax = Math.max(Math.max(x1, x2), Math.max(x3, x4));
		int ymin = Math.min(Math.min(y1, y2), Math.min(y3, y4));
		int ymax = Math.max(Math.max(y1, y2), Math.max(y3, y4));

		out.println((int) Math.pow(Math.max(xmax - xmin, ymax - ymin), 2));

		out.close();
		br.close();
	}
}
