package tictactoe;

public class CrossDiagWinningStrategy implements WinningStrategy{
    @Override
    public boolean evaluate(Board board, Move move) {
        Cell lastChangedCell = board.getCell(move.getRow(), move.getCol());
        // basic check to test whether the changed cell is on cross diagonal
        if (lastChangedCell.getRow()+lastChangedCell.getCol()!= board.getSize()) return false;
        // we have to check if the same player has all the cells in the cross diagonal has the same
        Player currentPlayer = lastChangedCell.getPlayer();
        if (currentPlayer==null) return false;
        for(int i=0;i<board.getSize();i++){
            if (board.getCell(i, board.getSize()-i).getPlayer() != currentPlayer){
                return false;
            }
        }
        return true;
    }
}
