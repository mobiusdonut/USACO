import java.util.*;
import java.io.*;
import java.lang.Math;

public class berries {
  public static int trees, baskets;
  public static int[] berries;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new FileReader("berries.in"));
    PrintWriter out = new PrintWriter(new FileWriter("berries.out"));
		StringTokenizer str = new StringTokenizer(br.readLine());
    int trees = Integer.parseInt(str.nextToken());
    int baskets = Integer.parseInt(str.nextToken());
    berries = new int[trees];
    str = new StringTokenizer(br.readLine());
    for (int i = 0; i < trees; i++) {
        berries[i] = Integer.parseInt(str.nextToken());
    }
    Arrays.sort(berries);
    int minber = 0;
    for (int j = trees - baskets; j < trees - baskets / 2; j++) {
        minber += berries[j];
    }
    //System.out.println(minber);
    int maxber = minber;
    for (int k = 0; k < baskets / 2; k++) {
        minber += berries[trees - k - 1] / 2;
        minber -= berries[trees - baskets + k];
        //System.out.println(minber);
        if (maxber < minber) {
          maxber = minber;
        }
    }
    System.out.println(maxber);
    out.println(maxber);

    out.close();
		br.close();
  }
}
