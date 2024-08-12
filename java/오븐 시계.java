import java.util.Scanner;

/*
 * min = 60 * h + m; // min = 60 * 시 + 분 
 * min = min + c; // 요리하는데 걸린 시간 더하기
 * h = (min / 60) % 24; // 시(24시 이상이 될 경우, 0시부터 시작하도록 한다) 
 * m = min % 60; // 분
 */
// BACKJOON 2525
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int h = sc.nextInt();
		int m = sc.nextInt();
		int c = sc.nextInt();
		int min = 60 * h + m;
		min = min + c;
		
		h = (min / 60) % 24;
		m = (min % 60);

		System.out.println(h + " " + m);
		sc.close();
	}
}