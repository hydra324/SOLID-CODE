package poker;

public class FlushRule implements Rule {
    private int priority;

    public FlushRule(int priority) {
        this.priority = priority;
    }

    public int getPriority() {
        return this.priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public boolean evaluate(Hand hand) {
        // check if all cards have the same card type
        CardTypes cardType = hand.cards.get(0).getCardType();
        for (Card card : hand.cards) {
            if (card.getCardType() != cardType) {
                return false;
            }
        }
        return true;
    }
}