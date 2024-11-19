public class Main {
  public static void main(String[] args) {
    Car myCar = new Car("red", "subaru", 2003);
    Car myCar1 = new Car("blue", "porche", 2022);
    Car myCar2 = new Car("red", "toyota", 2005);
    myCar.displayInfo();
    myCar1.displayInfo();
    myCar2.displayInfo();
  }

}

class Car {
  // this are called attributes or field names
  private String colour;
  private String model;
  private int year;

  // this is a constructor and its not a class but a method
  public Car(String colour, String model, int year) {
    this.colour = colour;
    this.model = model;
    this.year = year;

  }

  public void displayInfo() {
    System.out.println(year + " " + model + " in " + colour + " colour.");
  }

  public String getModel() {
    return model;
  };

  public void setModel(String model) {
    this.model = model;
  };

  public String getColour() {
    return colour;
  };

  public void setColour(String colour) {
    this.colour = colour;
  };

  public int getYear() {
    return year;
  };

  public void setYear(int year) {
    this.year = year;
  };

}
