package poker;
import java.util.*;

// create a class called RuleAggregator
public class RuleAggregator {
    // priority queue with integer priority
    PriorityQueue<Rule> rules;

    public RuleAggregator() {
        this.rules = new PriorityQueue<>(Comparator.comparingInt(Rule::getPriority));
    }

    public RuleAggregator addRule(Rule rule) {

        this.rules.add(rule);
        return this;
    }

    public void removeRule(Rule rule) {
        if (!this.rules.contains(rule)){
            throw new IllegalArgumentException("Rule not in list");
        }
        this.rules.remove(rule);
    }
}
    