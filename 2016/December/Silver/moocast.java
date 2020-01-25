import java.util.*;
import java.io.*;

public class moocast {

	public static int n;
	public static int[][] pts;

	public static void main(String[] args) throws Exception {

		Scanner stdin = new Scanner(new File("moocast.in"));
		n = stdin.nextInt();
		pts = new int[n][3];
		for (int i=0; i<n; i++)
			for (int j=0; j<3; j++)
				pts[i][j] = stdin.nextInt();

		int res = 0;
		for (int i=0; i<n; i++)
			res = Math.max(res, reach(i));

		PrintWriter out = new PrintWriter(new FileWriter("moocast.out"));
		out.println(res);
		out.close();
		stdin.close();
	}

	public static int reach(int v) {

		boolean[] used = new boolean[n];
		floodfill(v, used);

		int res = 0;
		for (int i=0; i<n; i++)
			if (used[i])
				res++;
		return res;
	}

	public static void floodfill(int v, boolean[] used) {
		used[v] = true;

		for (int i=0; i<n; i++) {
			if (used[i]) continue;

			if ((pts[i][0]-pts[v][0])*(pts[i][0]-pts[v][0]) + (pts[i][1]-pts[v][1])*(pts[i][1]-pts[v][1]) <= (long)pts[v][2]*pts[v][2])
				floodfill(i, used);
		}
	}
}
