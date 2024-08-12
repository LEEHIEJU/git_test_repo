import java.util.Scanner;

// BAEKJOON 3003번
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int king = 1;
		int queen = 1;
		int ro = 2;
		int bi = 2;
		int ni = 2;
		int pon = 8;
		
		king = king - sc.nextInt();
		queen = queen - sc.nextInt();
		ro = ro - sc.nextInt();
		bi = bi - sc.nextInt();
		ni = ni - sc.nextInt();
		pon = pon - sc.nextInt();
		
		System.out.println(king + "");
		System.out.println(queen + "");
		System.out.println(ro + "");
		System.out.println(bi + "");
		System.out.println(ni + "");
		System.out.println(pon + "");
		
		
		sc.close();
	}

}
