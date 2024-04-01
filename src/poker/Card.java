package poker;



public class Card {
    public int value;
    public CardTypes cardType;

    public Card(int value, CardTypes cardType) {
        this.value = value;
        this.cardType = cardType;
    }

    public int getValue(){
        return this.value;
    }

    public CardTypes getCardType() {
        return cardType;
    }

    public void setCardType(CardTypes cardType) {
        this.cardType = cardType;
    }
}