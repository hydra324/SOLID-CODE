package poker;
import java.util.Random;

public class Player {
    Hand hand;
    String name;
    public Player(String name) {
        this.name = name;
        this.hand = new Hand();
    }

    public void drawCard() {
        // draws a random card and adds it to hand
        Random rand = new Random();
        Card randomCard = new Card(rand.nextInt(11),CardTypes.values()[rand.nextInt(4)]);
        hand.addCard(randomCard);
    }
}
