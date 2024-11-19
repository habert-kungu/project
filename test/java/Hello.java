import java.util.Scanner;

//the scanner method is used to real input
class Hello {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int AgeInYears = 0;
    int AgeInDays = 0;
    boolean validInput = false;

    while (!validInput) {
      try {
        System.out.println("Please enter age in years(Less than 120): ");
        AgeInYears = scanner.nextInt();

        if (AgeInYears <= 0 || AgeInYears > 120) {
          System.out.println("Please input a number between 1 and 120");
        } else {
          AgeInDays = AgeInYears * 365;
          System.out.println("Your Age in days are " + AgeInDays);
          validInput = true;

        }

      } catch (Exception e) {
        System.out.println("Not an Integer");
        scanner.next();
      }

    }
    scanner.close();

  }
}
