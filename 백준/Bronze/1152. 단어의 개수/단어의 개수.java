import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String letter = sc.nextLine();
		String letter2 = letter.strip();
		
		int count = 0;
		
		for (int i=0;i<letter2.length();i++) {
			String s = Character.toString(letter2.charAt(i));
			if (s.equals(" "))
				count += 1;				
			}
		if (letter2 != "") {
			System.out.println(count + 1);
		} else {
			System.out.println(0);
		}
		
		sc.close();
		
	}

}
