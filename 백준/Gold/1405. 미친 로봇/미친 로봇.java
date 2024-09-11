import java.util.Scanner;

public class Main {
    // 입력부
    static int N, east, west, south, north;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int[] direction;
    static boolean[][] visited = new boolean[29][29];

    // DFS
    static double[] DFS(int X, int Y, int idx, double point) {
        // 단순하지 않은 경로임
        if (visited[X][Y]) return new double[]{0, point * Math.pow(100, N - idx)};
        // 단순한 경로임
        if (idx == N) return new double[]{point, point};

        // 탐색
        visited[X][Y] = true;

        // 다음 탐색
        double dansun = 0, total = 0;
        for (int i = 0; i < 4; i++) {
            int X_ = X + dx[i], Y_ = Y + dy[i];
            double[] result = DFS(X_, Y_, idx + 1, point * direction[i]);
            dansun += result[0];
            total += result[1];
        }

        // backtracking
        visited[X][Y] = false;

        return new double[]{dansun, total};
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        east = sc.nextInt();
        west = sc.nextInt();
        south = sc.nextInt();
        north = sc.nextInt();
        
        direction = new int[]{east, west, south, north};

        // 함수 호출 및 출력부
        double[] result = DFS(14, 14, 0, 1.0);
        System.out.println(result[0] / result[1]);
        
        sc.close();
    }
}