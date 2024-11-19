public class Work {

  public static void main(String[] args) {
    long hoursWorked = 40;
    double payRate = 10;
    double taxRate = 2.3;

    System.out.println("Hours Worked" + hoursWorked);
    System.out.println("Your pay is " + hoursWorked * payRate);
    System.out.println("Your payable tax is " + hoursWorked * payRate * taxRate);
  }
}
