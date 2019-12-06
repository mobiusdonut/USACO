import java.io.*;
import java.util.*;

public class cowsignal {
  public static void main(String[] args)throws Exception {
    BufferedReader br = new BufferedReader(new FileReader("cowsignal.in"));
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter("cowsignal.out")));

    StringTokenizer str = new StringTokenizer(br.readLine());
    int m = Integer.parseInt(str.nextToken());
    int n = Integer.parseInt(str.nextToken());
    int k = Integer.parseInt(str.nextToken());

    char[][] signalArray = new char[m][n];

    String st;
    for (int i = 0; i < m; i++) {
      st = br.readLine();
      for (int j = 0; j < n; j++) {
        signalArray[i][j] = st.charAt(j);
      }
    }
    for (int i = 0; i < m; i++) {
      for (int l = 0; l < k; l++) {
        for (int j = 0; j < n; j++) {
          for (int o = 0; o < k; o++) {
            out.print(signalArray[i][j]);
          }
        }
        out.println();
      }
    }
    out.close();
  }
}
