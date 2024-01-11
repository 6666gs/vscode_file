import java.util.Scanner;

public class Hello1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Hello,world!");
		System.out.print("input:");
		String name = scanner.nextLine();
		System.out.println(" ");
		System.out.println("%s", name);

	}

}