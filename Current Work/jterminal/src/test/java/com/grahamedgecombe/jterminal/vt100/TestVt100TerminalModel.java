/*
 * Copyright (c) 2009-2011 Graham Edgecombe.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 * FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
 * DEALINGS IN THE SOFTWARE.
 */

package com.grahamedgecombe.jterminal.vt100;

import static org.junit.Assert.*;

import java.awt.Color;

import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.After;
import org.junit.Test;

import com.grahamedgecombe.jterminal.TerminalCell;
import com.grahamedgecombe.jterminal.TerminalModel;
import com.grahamedgecombe.jterminal.bell.BellStrategy;
import java.io.FileWriter; 
import java.io.IOException;
/**
 * A test for the {@link Vt100TerminalModel} class.
 * @author Graham Edgecombe
 */
public class TestVt100TerminalModel {

	/**
	 * The terminal model.
	 */
	private TerminalModel model;
	public static int test_count;
	public static FileWriter results_writer;

	/**
	 * Sets up the terminal model.
	 */
	@Before
	public void setUp(){
		model = new Vt100TerminalModel();
	}
	@BeforeClass
	public static void setUpWriter(){
		try {
		results_writer = new FileWriter("./Test_Results.txt");
		} catch (IOException e) {
		}
		test_count=1;
	}
	public void printTestOutput(int line_number, Object output){
		try {
		results_writer.write(line_number+","+test_count+" , "+output);
		results_writer.write("\n");
		results_writer.flush();
		
		} catch (IOException e) {
			System.out.println("An error occurred.");
			e.printStackTrace();
		}
		test_count++;
	}
	

	/**
	 * Tests the word wrapping.
	 */
	@Test
	public void testWordWrapping() {
		int width = model.getColumns();
		for (int i = 0; i < (width + 1); i++) {
			model.print("h");
		}
		printTestOutput(90,model.getCell(0, 1).getCharacter());
		////assertEquals('h', model.getCell(0, 1).getCharacter());//test1
	}

	/**
	 * Tests special ASCII characters.
	 */
	@Test
	public void testSpecialCharacters() {
		model.print("\u0000");
		printTestOutput(100,model.getCell(0, 0));//mycode
		
		//assertNull(model.getCell(0, 0));//test2

		model.print("a\rb\rc");
		printTestOutput(104,model.getCell(0, 0).getCharacter());
		//assertEquals('c', model.getCell(0, 0).getCharacter());//test3

		model.print("\na");
		printTestOutput(108,model.getCell(0, 0).getCharacter());
		//assertEquals('c', model.getCell(0, 0).getCharacter());//test4
		printTestOutput(110,model.getCell(0, 1).getCharacter());
		//assertEquals('a', model.getCell(0, 1).getCharacter());//test5

		model.print("\u007F");
		printTestOutput(114,model.getCell(0, 1));
		//assertNull(model.getCell(0, 1));//test6

		model.print("A\tB");
		printTestOutput(118,model.getCell(8, 1).getCharacter());
		//assertEquals('B', model.getCell(8, 1).getCharacter());//test7
	}

	/**
	 * Tests that the terminal scrolls once the buffer is full.
	 */
	@Test
	public void testBuffer() {
		model = new Vt100TerminalModel(model.getColumns(), 2, 2);
		model.print("This is line one.\r\n");
		model.print("This is line two. XXXXXX\r\n");
		model.print("And this is line three!");
		printTestOutput(131,model.getCell(0, 1).getCharacter());
		//assertEquals('A', model.getCell(0, 1).getCharacter());//test8
		printTestOutput(133,model.getCell(23, 1));
		//assertNull(model.getCell(23, 1));//test9
	}

	/**
	 * Tests the erase functionality.
	 */
	 /**
	@Test
	public void testErase() {
		model.print("Hello");
		model.print("\u009B2J");
		for (int i = 0; i < 5; i++) {
			printTestOutput(145,model.getCell(i, 0));
			//assertNull(model.getCell(i, 0)); //test10
		}
	}
	*/

	/**
	 * Tests moving the cursor.
	 */
	@Test
	public void testMoveCursor() {
		model.print("\u009B5B");
		printTestOutput(156,model.getCursorRow());
		//assertEquals(5, model.getCursorRow());//test11

		model.print("\u009B3A");
		printTestOutput(160,model.getCursorRow());
		//assertEquals(2, model.getCursorRow());//test12

		model.print("\u009B7C");
		printTestOutput(164,model.getCursorColumn());
		//assertEquals(7, model.getCursorColumn());//test13

		model.print("\u009B4D");
		printTestOutput(168,model.getCursorColumn());
		//assertEquals(3, model.getCursorColumn());//test14

		model.setCursorColumn(15);
		model.setCursorRow(0);

		model.print("\u009B3E");
		printTestOutput(175,model.getCursorColumn());
		//assertEquals(0, model.getCursorColumn());//test15
		printTestOutput(177,model.getCursorRow());
		//assertEquals(3, model.getCursorRow());//test16

		model.setCursorColumn(7);

		model.print("\u009BF");
		printTestOutput(183,model.getCursorColumn());
		//assertEquals(0, model.getCursorColumn());//test17
		printTestOutput(185,model.getCursorRow());
		//assertEquals(2, model.getCursorRow());//test18

		model.print("\u009B4;8H");
		printTestOutput(189,model.getCursorRow());
		//assertEquals(3, model.getCursorRow());//test19
		printTestOutput(191,model.getCursorColumn());
		//assertEquals(7, model.getCursorColumn());//test20
	}

	/**
	 * Tests the SGR escape sequence.
	 */
	@Test
	public void testSgr() {
		model.print("\u009B2;33;41mX");

		TerminalCell cell = model.getCell(0, 0);
		printTestOutput(203,cell);
		//assertNotNull(cell);//test21
		printTestOutput(205,cell.getCharacter());
		//assertEquals('X', cell.getCharacter());//test22
        printTestOutput(207,cell.getBackgroundColor());
		//assertEquals(Color.RED, cell.getBackgroundColor());//test23
		printTestOutput(209,cell.getForegroundColor());
		//assertEquals(Color.YELLOW, cell.getForegroundColor());//test24

		model.print("\u009B0m\rX");

		cell = model.getCell(0, 0);
        printTestOutput(215,cell);
		//assertNotNull(cell);//test25
		printTestOutput(217,cell.getCharacter());
		//assertEquals('X', cell.getCharacter());//test26
        printTestOutput(219,cell.getBackgroundColor());
		//assertEquals(model.getDefaultBackgroundColor(), cell.getBackgroundColor());//test27
		printTestOutput(221,cell.getForegroundColor());
		//assertEquals(model.getDefaultForegroundColor(), cell.getForegroundColor());//test28
	}

	/**
	 * Tests saving and restoring the cursor.
	 */
	@Test
	public void testSaveAndRestoreCursor() {
		model.setCursorColumn(3);
		model.setCursorRow(17);

		model.print("\u009Bs");

		model.setCursorColumn(5);
		model.setCursorRow(23);

		model.print("\u009Bu");
        printTestOutput(239,model.getCursorColumn());
		//assertEquals(3, model.getCursorColumn());//test29
		printTestOutput(241,model.getCursorRow());
		//assertEquals(17, model.getCursorRow()); //test30
	}

	/**
	 * Tests the printing of a simple message.
	 */
	@Test
	public void testPrint() {
		model.print("Hi");
		printTestOutput(251,model.getCell(0, 0).getCharacter());
		//assertEquals('H', model.getCell(0, 0).getCharacter()); //test31
		printTestOutput(253,model.getCell(1, 0).getCharacter());
		//assertEquals('i', model.getCell(1, 0).getCharacter()); //test32
		printTestOutput(255,model.getCell(2, 0));
		//assertNull(model.getCell(2, 0)); //test33
	}

	/**
	 * Tests that the bell is sounded.
	 */
	@Test
	public void testBell() {
		final int[] counter = new int[1];

		BellStrategy strategy = new BellStrategy() {
			/*
			 * (non-Javadoc)
			 * @see com.grahamedgecombe.jterminal.bell.BellStrategy#soundBell()
			 */
			@Override
			public void soundBell() {
				counter[0]++;
			}
		};

		model.setBellStrategy(strategy);

		model.print("\u0007");
		printTestOutput(280,counter[0]);
		//assertEquals(1, counter[0]); //test34

		model.print("Hello, \u0007World!\u0007\r\n");
		printTestOutput(284,counter[0]);
		//assertEquals(3, counter[0]); //test35
	}

}

