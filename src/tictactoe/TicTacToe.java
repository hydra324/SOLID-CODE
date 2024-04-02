package tictactoe;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class TicTacToe {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Please enter board size:");
        int boardSize = scanner.nextInt();
        Board board = new Board(boardSize);
        List<Player> allPlayers = new ArrayList<>();
        int numPlayers = 2;
        for(int i=0;i<numPlayers;i++){
            System.out.println(String.format("Please enter player %s name:",i));
            String name = scanner.nextLine();
            System.out.println(String.format("Please enter player %s character:",i));
            String character = scanner.nextLine();
            allPlayers.add(new Player(name,character));
        }
        List<WinningStrategy> allStrategies = new ArrayList<>();
        allStrategies.add(new RowWinningStrategy());
        allStrategies.add(new ColumnWinningStrategy());
        allStrategies.add(new DiagWinningStrategy());
        allStrategies.add(new CrossDiagWinningStrategy());
        GameController gameController = new GameController(board,allPlayers,allStrategies);
        int currentPlayer = 0; // start with first player
        String winner = null;
        while(true){
            System.out.println(String.format("Please enter player %s move in space separated integers",currentPlayer));
            String moveString = scanner.nextLine();
            List<Integer> moveList = Arrays.stream(moveString.split(" ")).map((Integer::parseInt)).toList();
            Move lastMove = allPlayers.get(currentPlayer).createMove(moveList.get(0),moveList.get(1));
            gameController.executeMove(lastMove);
            if (gameController.checkGameState(lastMove)){
                winner = lastMove.getPlayer().getName();
                break;
            }
        }

        System.out.println(String.format("the winner is %s",winner));
    }
}
