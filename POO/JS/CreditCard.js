class Credicard extends Payment{
    constructor(id,reference,TypeCredicard, CVV){
        super(id);
        this.reference = reference;
        this.TypeCredicard = TypeCredicard;
        this.CVV = CVV;
    }	
}