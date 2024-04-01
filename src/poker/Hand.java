package poker;

import java.util.*;

public class Hand {

    List<Card> cards;

    public Hand() {
        this.cards = new ArrayList<>();
    }

    public Hand addCard(Card card) {
        this.cards.add(card);
        return this;
    }

    public boolean removeCard(Card card) {

        // check if card actually exists in hand
        if (!this.cards.contains(card)){
            throw new IllegalArgumentException("Card not in hand");
        }
        this.cards.remove(card);
        return true;
    }
}
