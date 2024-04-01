package poker;

public class OnePairRule implements Rule {
    private int priority;

    public OnePairRule(int priority) {
        this.priority = priority;
    }

    public int getPriority() {
        return this.priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public boolean evaluate(Hand hand) {
        // check if there is a pair of cards with the same value
        for (int i = 0; i < hand.cards.size(); i++) {
            for (int j = i + 1; j < hand.cards.size(); j++) {
                if (hand.cards.get(i).getValue() == hand.cards.get(j).getValue()) {
                    return true;
                }
            }
        }
        return false;
    }
}
