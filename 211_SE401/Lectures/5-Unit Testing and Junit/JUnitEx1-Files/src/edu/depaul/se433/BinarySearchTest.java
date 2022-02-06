package edu.depaul.se433;

import org.junit.*;
import static org.junit.Assert.*;

import static edu.depaul.se433.BinarySearch.*; 

public class BinarySearchTest {

    @Test
    public void test1() {
	Comparable [] a = new Integer[] { 1, 3, 5, 7};
	assertTrue(binarySearch(a, 3) == 1);
	assertTrue(binarySearch(a, 2) == -1);
    }

    @Test
    public void test2() {
	Comparable [] a = new Integer[] { 1, 3, 5, 7};
	assertTrue(binarySearch(a, 3) == 1);
	assertTrue(binarySearch(a, null) == -1);
    }

    @Test(expected=IllegalArgumentException.class)
    public void test3() {
	Comparable [ ] a = new Integer[] { 1, 3, 5, 7};
	assertTrue(binarySearch2(a, 3) == 1);
	assertTrue(binarySearch2(a, null) == -1);
	fail();
    }
}