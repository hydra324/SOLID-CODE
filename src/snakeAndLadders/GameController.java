package snakeAndLadders;
import java.util.*;
public class GameController {

    private List<Player> players;
    private Board board;
    private HashMap<Integer,Integer> snakesOrLadders;
    private int numPlayersInGame = 0;
    public GameController(List<Player> players,Board board,HashMap<Integer,Integer> snakesOrLadders){
        this.players = players;
        this.board = board;
        this.snakesOrLadders = snakesOrLadders;
        this.numPlayersInGame = players.size();
    }

    // return true if move results in player reaching the end, false otherwise.
    public boolean executeMove(Move move){
        Player player = move.getPlayer();
        // remove player from existing cell
        Cell oldCell = player.getCurrentCell();
        oldCell.removePlayer(player); // possible pub/sub pattern here

        // find the next index
        int newIndex = oldCell.getNumber() + move.getDiceRoll();
        // validate new cell
        newIndex = snakesOrLadders.getOrDefault(newIndex,newIndex);

        // make sure new index is within range
        newIndex = Math.max(newIndex, board.maxNumber);

        if (newIndex==board.maxNumber){
            // remove one player from the pool
            numPlayersInGame--;
            return true;
        }
        // add player to the cell at new index
        Cell newCell = board.getCell(newIndex);
        newCell.addPlayer(player);
        return false;
    }

    public boolean checkIfGameEnds(){
        return numPlayersInGame>1;
    }


}
