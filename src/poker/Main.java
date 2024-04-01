package poker;

public class Main {
    public static void main(String[] args){
        FlushRule flushRule = new FlushRule(2);
        OnePairRule onePairRule = new OnePairRule(1);
        RuleAggregator ruleAggregator = new RuleAggregator()
                .addRule(flushRule)
                .addRule(onePairRule);
        Hand hand1 = new Hand()
                .addCard(new Card(2,CardTypes.SPADES))
                .addCard(new Card(4,CardTypes.SPADES))
                .addCard(new Card(6,CardTypes.SPADES))
                .addCard(new Card(2,CardTypes.SPADES))
                .addCard(new Card(10,CardTypes.SPADES));
        Hand hand2 = new Hand()
                .addCard(new Card(2, CardTypes.SPADES))
                .addCard(new Card(2, CardTypes.HEARTS))
                .addCard(new Card(4, CardTypes.DIAMONDS))
                .addCard(new Card(8, CardTypes.SPADES))
                .addCard(new Card(10, CardTypes.SPADES));
        HandEvaluator handEvaluator = new HandEvaluator(ruleAggregator);
        Rule bestRule1 = handEvaluator.getBestRule(hand1);
        Rule bestRule2 = handEvaluator.getBestRule(hand2);
        System.out.println("Best rule for hand1: " + bestRule1.getClass().getName());
        System.out.println("Best rule for hand2: " + bestRule2.getClass().getName());
    }
    
}
