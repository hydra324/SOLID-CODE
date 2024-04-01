package poker;

public class HandEvaluator{
    RuleAggregator ruleAggregator;
    public HandEvaluator(RuleAggregator ruleAggregator){
        this.ruleAggregator = ruleAggregator;
    }
    public Rule getBestRule(Hand hand){
        // return the best rule
        for (Rule rule : ruleAggregator.rules){
            if (rule.evaluate(hand)){
                return rule;
            }
        }

        return null;

    }
}