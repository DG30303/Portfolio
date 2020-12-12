
import java.awt.Color;
import doodlepad.Oval;
import doodlepad.Pad;
import doodlepad.Text;
import java.awt.event.KeyEvent;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

import doodlepad.Line;


public class MyConnectFour extends Pad {

	private static final int WIDTH = 700, HEIGHT = 650;

	private static final int P_WIDTH = WIDTH / 7;
	private Oval[][] pieces;
	private int num;
	private boolean playComputer;

	public MyConnectFour(boolean computer) {
		super(WIDTH,HEIGHT);
		playComputer = computer;
		pieces = new Oval[6][7];
		makeBoard();
	}

	private void makeHoles(int col) {
		int y = 0;
		int x = col * P_WIDTH;
		for(int r = 0; r < pieces.length; r++) {
			Oval hole = new Oval(x,y,P_WIDTH,P_WIDTH);
			hole.setFillColor(Color.WHITE);
			hole.setEventsEnabled(false);
			y+= P_WIDTH;
		}
	}

	private void makeBoard() {
		setBackground(0,0,0);
		for(int i = 0; i < pieces[0].length; i++)
			makeHoles(i);
	}

	public void computerTurn() {
		int r = (int)(Math.random()*7);
		while(!placePiece(r)) 
			r = (int)(Math.random()*7);
	}

	public boolean placePiece(int col) {
		Color color = Color.RED;
		boolean over = false;
		boolean piecePlayed = false;
		if(num%2 == 0)
			color = Color.BLUE;
		for(int i = pieces.length-1; i >= 0; i--) {
			if(pieces[i][col] == null) {
				Oval p = new Oval(col*P_WIDTH,i*P_WIDTH,P_WIDTH,P_WIDTH);
				p.setFillColor(color);
				p.setEventsEnabled(false);
				pieces[i][col] = p;
				num++;
				piecePlayed = true;
				over = gameOver(i,col);
				break;
			}
		}
		if(!piecePlayed)
			return false;
		if(!over && playComputer && num%2 == 1)
			computerTurn();
		return piecePlayed;
	}

	public void onMouseClicked(double x, double y, int button) {
		int col = -1;
		while(x >= 0) {
			x-= P_WIDTH;
			col++;
		}
		if(!placePiece(col))
			System.out.println("This column is full, pick another one");
	}

	public void endGame(Color c) {
		if(c == Color.RED) {
			Text t = new Text("RED WON!",100,20,100);
			t.setFillColor(c);
			t.setStrokeWidth(1);
			t.setStrokeColor(Color.WHITE);
		}
		else if(c == Color.BLUE) {
			Text text = new Text("BLUE WON!", 100,20,100);
			text.setFillColor(c);
			text.setStrokeWidth(1);
			text.setStrokeColor(Color.WHITE);
		}
		else {
			Text tie = new Text("YOU TIED!",100,20,100);
			tie.setFillColor(c);
			tie.setStrokeWidth(1);
			tie.setStrokeColor(Color.WHITE);
		}
		this.setEventsEnabled(false);
	}

	public boolean horizontalWin(int row, Color color) {
		int count = 0;
		for(int i = 0; i < pieces[row].length; i++) {
			if(pieces[row][i] != null && pieces[row][i].getFillColor() == color)
				count++;
			else
				count = 0;
			if(count == 4)
				return true;
		}
		return false;
	}

	public boolean verticalWin(int col, Color color) {
		int count = 0;
		for(int i = 0; i < pieces.length; i++) {
			if(pieces[i][col] != null && pieces[i][col].getFillColor() == color)
				count++;
			else
				count = 0;
			if(count == 4)
				return true;
		}
		return false;
	}

	public boolean checkDiagonalRight(int row, int col, Color color) {
		int count = 0;
		while(row >= 0 && col < pieces[0].length) {
			if(pieces[row][col] != null && pieces[row][col].getFillColor() == color)
				count++;
			else
				count = 0;
			if(count == 4)
				return true;
			row--;
			col++;
		}
		return false;
	}

	public boolean checkDiagonalLeft(int row, int col, Color color) {
		int count = 0;
		while(row < pieces.length && col < pieces[0].length) {
			if(pieces[row][col] != null && pieces[row][col].getFillColor() == color)
				count++;
			else
				count = 0;
			if(count == 4)
				return true;
			row++;
			col++;
		}
		return false;
	}

	public boolean diagonalWin(Color color) {
		if(checkDiagonalLeft(0,3,color) || checkDiagonalLeft(0,2,color) || checkDiagonalLeft(0,1,color) || checkDiagonalLeft(0,0,color) || checkDiagonalLeft(1,0,color) || checkDiagonalLeft(2,0,color))
			return true;
		if(checkDiagonalRight(3,0,color) || checkDiagonalRight(4,0,color) || checkDiagonalRight(5,0,color) || checkDiagonalRight(5,1,color) || checkDiagonalRight(5,2,color) || checkDiagonalRight(5,3,color))
			return true;
		return false;
	}

	public boolean gameOver(int row, int col) {
		if(horizontalWin(row,Color.BLUE) || verticalWin(col,Color.BLUE) || diagonalWin(Color.BLUE)) {
			endGame(Color.BLUE);
			return true;
		}
		if(horizontalWin(row,Color.RED) || verticalWin(col,Color.RED) || diagonalWin(Color.RED)) {
			endGame(Color.RED);
			return true;
		}
		for(int r = 0; r < pieces.length; r++) {
			for(int c = 0; c < pieces[0].length; c++) {
				if(pieces[r][c] == null)
					return false;
			}
		}
		endGame(Color.BLACK);
		return true;
	}

	public static void main(String[] args) {

		boolean playComputer = false;

		MyConnectFour f = new MyConnectFour(playComputer);

	}
}
