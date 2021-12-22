class Paypal extends Payment{
    constructor(id,reference,TypeCredicard){
        super(id);
        this.reference = reference;
        this.TypeCredicard = TypeCredicard;
    }	
}