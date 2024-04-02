package tictactoe;
import java.util.List;

public class GameController {
    // responsibility of this class is to make high level executions
    private Board board;
    private List<Player> players;
    private List<WinningStrategy> allStrategies;
    public GameController(Board board,List<Player> players, List<WinningStrategy> allStrategies){
        this.board = board;
        this.players = players;
        this.allStrategies = allStrategies;
    }

    public void executeMove(Move move){
        Cell activeCell = this.board.getCell(move.getRow(), move.getCol());
        // change the player that is at this cell
        // also do validation, whether the cell is empty or not

        // set player at this cell
        activeCell.setPlayer(move.getPlayer());
    }

    public boolean checkGameState(Move lastMove){
        // we have to check this move against each strategy
        for(WinningStrategy strategy: allStrategies){
            if (strategy.evaluate(board,lastMove)) return true;
        }
        return false;
    }


}
