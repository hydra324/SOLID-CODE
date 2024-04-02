package tictactoe;

public interface WinningStrategy {
    boolean evaluate(Board board, Move move);
}
