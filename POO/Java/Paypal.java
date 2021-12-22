public class Paypal extends Payment {
    String reference;
    String branchOffice;
    public Paypal(String id, String reference, String branchOffice) {
        super(id);
        this.reference = reference;
        this.branchOffice = branchOffice;
        
        this.printDataPayment();
    }
}
    
    

