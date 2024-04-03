package snakeAndLadders;

public class Dice {
    private int maxRoll;
    private int minRoll = 1;

    public Dice(int maxRoll) {
        this.maxRoll = maxRoll;
    }

    public int roll(){
        int currentRoll = 0;
        do {
            currentRoll += minRoll + (int) (Math.random() * (maxRoll-minRoll + 1));
        } while (currentRoll % maxRoll ==0);
        return currentRoll;
    }
}
