class Driver extends Account {
    public Driver(String name, String document) {
        super(name, document);
    }
    void printDataUser(){
        system.out.println("Name: " + name + " Document: " + document);
    }
}