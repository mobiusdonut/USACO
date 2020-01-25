import java.util.*;
import java.io.*;
import java.lang.Math;

public class meetings {
  static class cow implements Comparable<cow>{
    int weight;
    int location;
    int velocity;
    boolean barn = false;
    int numCows = 0;
    boolean collided = false;

    @Override
    public int compareTo(cow c) {
      if(this.location > c.location)
          return 1;
      else if (this.location == c.location)
          return 0;
      return -1 ;
    }
  }

  public static int n, l;
  public static ArrayList<cow> points = new ArrayList<cow>();
  public static double barnWeight = 0;
  public static double sumWeight = 0;
  public static int meetings = 0;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new FileReader("meetings.in"));
    PrintWriter out = new PrintWriter(new FileWriter("meetings.out"));
		StringTokenizer str = new StringTokenizer(br.readLine());
    int n = Integer.parseInt(str.nextToken());
    int l = Integer.parseInt(str.nextToken());
    int collides = 0;

    cow b1 = new cow();
    b1.weight = -1;
    b1.location = 0;
    b1.velocity = 0;
    b1.barn = true;
    points.add(b1);

    cow b2 = new cow();
    b2.weight = -1;
    b2.location = l;
    b2.velocity = 0;
    b2.barn = true;
    points.add(b2);

    for (int i = 2; i < n + 2; i++) {
            cow c = new cow();
            str = new StringTokenizer(br.readLine());
            c.weight = Integer.parseInt(str.nextToken());
            c.location = Integer.parseInt(str.nextToken());
            c.velocity = Integer.parseInt(str.nextToken());
            points.add(c);
            sumWeight += c.weight;
    }

    Collections.sort(points);

    while (barnWeight < sumWeight / 2) {
        barnWeight = 0;
        for (int i = 1; i < n + 1; i++) {
            if (!points.get(i).barn) {
                if (points.get(i).velocity == -1 && points.get(i).collided == false) {
                    cow left = points.get(i - 1);
                    if (left.velocity == 1 && points.get(i).location - left.location <= 1 && !points.get(i - 1).barn) {
                      System.out.println("cows " + i + " and " + (i - 1) + " collide at " + ((points.get(i).location + left.location)/2));
                      points.get(i).collided = true;
                      points.get(i - 1).collided = true;
                      collides += 1;
                    }
                }
                else if (points.get(i).velocity == 1 && points.get(i).collided == false) {
                    cow right = points.get(i + 1);
                    if (right.velocity == -1 && right.location - points.get(i).location <= 1 && !points.get(i + 1).barn) {
                      System.out.println("cows " + i + " and " + (i + 1) + " collide at " + ((points.get(i).location + right.location)/2));
                      points.get(i).collided = true;
                      points.get(i + 1).collided = true;
                      collides += 1;
                    }
                }
                if (points.get(i).collided == true || points.get(i).location == 0 || points.get(i).location == l) {

                }
                else {
                  points.get(i).location += points.get(i).velocity;
                }
            }
        }

        System.out.println("");
        for (int i = 1; i < n + 1; i++) {
            System.out.println(points.get(i).location + " " + points.get(i).velocity + " " + points.get(i).collided);
          if (points.get(i).collided) {
            points.get(i).velocity = points.get(i).velocity * -1;
            points.get(i).collided = false;
          }
          if (points.get(i).location == 0 || points.get(i).location == l) {
            System.out.println("cow with weight " + points.get(i).weight + " has reached barn");
            barnWeight += points.get(i).weight;
          }
        }
        System.out.println(barnWeight);
        System.out.println("");
    }

    out.println(collides);

    out.close();
		br.close();
  }
}
