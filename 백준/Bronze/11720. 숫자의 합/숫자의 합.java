import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int size = sc.nextInt();
		String inputs = sc.next();
		
		int sum = 0;
		for (int i=0;i<size;i++) {
			String letter = Character.toString(inputs.charAt(i));
			sum += Integer.parseInt(letter);
		}
		
		System.out.println(sum);

	}

}