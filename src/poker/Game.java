package poker;
import java.util.ArrayList;
import java.util.List;
public class Game {
    List<Player> players;
    RuleAggregator ruleAggregator;
    public Game(RuleAggregator ruleAggregator){
        this.players = new ArrayList<>();
        this.ruleAggregator = ruleAggregator;
    }

    public Game addPlayer(Player player){
        this.players.add(player);
        return this;
    }

    public boolean isDone(){
        // checks whether any player has won
        for(Player player: this.players){

        }
        return false;
    }

    public void simulate(){
        // simulates playing the game
//        while(this.isDone()) {
//            for(Player player: players){
//
//            }
//        }
    }
}
