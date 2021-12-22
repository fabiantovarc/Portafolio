import java.util.Date;
public class CreditCard extends Payment{
    String id;
    String typeCreditCard;
    Date expirationDate;
    String cvv;
    public CreditCard(String id, String typeCreditCard, Date expirationDate, String cvv)    {
        super(id);
        this.typeCreditCard = typeCreditCard;
        this.expirationDate = expirationDate;
        this.cvv = cvv;

        this.printDataPayment();
    }
    
}
