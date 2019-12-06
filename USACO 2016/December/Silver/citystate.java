import java.util.*;
import java.io.*;

public class citystate {

	public static void main(String[] args) throws Exception {

		int[][] freq = new int[676][676];

		BufferedReader stdin = new BufferedReader(new FileReader("citystate.in"));
		int n = Integer.parseInt(stdin.readLine().trim());

		for (int i=0; i<n; i++) {
			StringTokenizer tok = new StringTokenizer(stdin.readLine());
			String city = tok.nextToken();
			String state = tok.nextToken();
			freq[convert(city)][convert(state)]++;
		}

		long res = 0;

		for (int i=0; i<676; i++)
			for (int j=i+1; j<676; j++)
				res += ((long)freq[i][j]*freq[j][i]);

		PrintWriter out = new PrintWriter(new FileWriter("citystate.out"));
		out.println(res);
		out.close();
		stdin.close();
	}

	public static int convert(String s) {
		return 26*(s.charAt(0)-'A') + s.charAt(1) - 'A';
	}
}
