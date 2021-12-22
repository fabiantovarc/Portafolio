class User extends Account {
    public User(String name, String document){
        super(name, document);
    }
    void printDataUser(){
        system.out.println("Name: " + name + " Document: " + document);
    }
}

