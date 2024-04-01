package poker;

interface Rule {
    // priority of the rule
    int getPriority();
    // set the priority of the rule
    void setPriority(int priority);
    // evaluates whether the rule is true or false for a given hand
    boolean evaluate(Hand hand);
}
