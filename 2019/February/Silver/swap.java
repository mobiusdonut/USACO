import java.util.*;
import java.util.stream.IntStream;
import java.io.*;

public class swap {
  public static int[] cowarray;
  public static int[] swaparrayl;
  public static int[] swaparrayr;

  public static void swap(int start, int end) {
    for (int i = start; i < (start + end)/2 + 1; i++) {
      int s1 = cowarray[i];
      int s2 = cowarray[end - (i - start)];
      cowarray[i] = s2;
      cowarray[end - (i - start)] = s1;
    }
  }

  public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new FileReader("swap.in"));
    PrintWriter out = new PrintWriter(new FileWriter("swap.out"));

    StringTokenizer str = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(str.nextToken());
    int m = Integer.parseInt(str.nextToken());
    int k = Integer.parseInt(str.nextToken());

    swaparrayl = new int[m];
    swaparrayr = new int[m];
    cowarray = IntStream.range(1, n + 1).toArray();

    for (int i = 0; i < m; i++) {
      str = new StringTokenizer(br.readLine());
      swaparrayl[i] = Integer.parseInt(str.nextToken());
      swaparrayr[i] = Integer.parseInt(str.nextToken());
    }

    for (int i = 0; i < k; i++) {
      for (int j = 0; j < m; j++) {
        swap(swaparrayl[j] - 1, swaparrayr[j] - 1);
      }
    }

    for (int i = 0; i < n; i++) {
      out.println(cowarray[i]);
    }

		out.close();
		br.close();
	}
}
