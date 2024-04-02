package tictactoe;

public class DiagWinningStrategy implements WinningStrategy{

    @Override
    public boolean evaluate(Board board, Move move) {
        Cell lastChangedCell = board.getCell(move.getRow(), move.getCol());
        // basic check to test whether the changed cell is on diagonal
        if (lastChangedCell.getRow()!= lastChangedCell.getCol()) return false;
        // we have to check if the same player has all the cells in the diagonal has the same
        Player currentPlayer = lastChangedCell.getPlayer();
        if (currentPlayer==null) return false;
        for(int i=0;i<board.getSize();i++){
            if (board.getCell(i,i).getPlayer() != currentPlayer){
                return false;
            }
        }
        return true;
    }
}
