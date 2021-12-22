class Main {
    public static void main(String[] args) {
        /*System.out.println("Hola Mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "AND123"));
        car.passegenger = 4;
        car.printDataCar();

        Car car2 = new Car("QWE567", new Account("Andrea Herrera", "ANDA876"));
        car2.passegenger = 3;
        car2.printDataCar();*/

        System.out.println("UberX....");
        UberX uberX = new UberX("AMQ123", new Account("Andres Herrera", "AND123"), "Chevrolet", "Spark");
        uberX.passegenger = 4;
        uberX.printDataCar();
    }
}