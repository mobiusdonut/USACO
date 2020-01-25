import java.util.*;
import java.io.*;

public class moobuzz {
  public static int n;
  public static long numIndex(long n) {
    return n - (n - n % 3) /3 - (n - n % 5) / 5 + (n - n % 15) / 15;
  }
  public static long binarySearch(long low, long high) {
    long mid = (low + high) / 2;
    //System.out.println(low + " " + mid + " " + high);
    if (numIndex(mid) == n) {
        while (numIndex(mid) == n) {
          mid = mid - 1;
        }
        return mid + 1;
    }
    else if (numIndex(low + 1) == (high)) {
        if (numIndex(low) == n) return low;
        else return high;
    }
    else if (numIndex(mid) < n) {
        return binarySearch(mid, high);
    }
    else if (numIndex(mid) > n) {
        return binarySearch(low, mid);
    }
    return binarySearch(low, high);
  }
  public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new FileReader("moobuzz.in"));
    PrintWriter out = new PrintWriter(new FileWriter("moobuzz.out"));
		n = Integer.parseInt(br.readLine());

    out.println(binarySearch(0, 1000000000000L));

		out.close();
		br.close();
	}
}
