package edu.depaul.se433;

import static org.junit.Assert.*;

import org.junit.Test;

import static edu.depaul.se433.StringUtil.*;

public class StringUtilTest {

    @Test
    public void testUncountable() {
        
        assertEquals("water", pluralize("water"));
        assertEquals("rice", pluralize("rice"));
}

    @Test
    public void testRegular() {
        
        assertEquals("cars", pluralize("car"));
        assertEquals("books", pluralize("book"));
        assertEquals("boys", pluralize("boy"));
}


    @Test
    public void testIrregular() {

        assertEquals("children", pluralize("child"));
        assertEquals("men", pluralize("man"));
        assertEquals("people", pluralize("person")); 
        assertEquals("mice", pluralize("mouse"));
}
    @Test
    public void testSpecialCases() {

        assertEquals("families", pluralize("family"));
        assertEquals("butterflies", pluralize("butterfly"));        

}
    @Test
    public void testSpecialCases1() {

        assertEquals("sandwiches", pluralize("sandwich"));
}

    @Test
    public void testSpecialCases2() {

        assertEquals("days", pluralize("day"));
        assertEquals("monkeys", pluralize("monkey"));
}

    @Test
    public void testSpecialCases3() {

        assertEquals("wives", pluralize("wife"));
        assertEquals("wolves", pluralize("wolf"));
}

    @Test
    public void testSpecialCases4() {


        assertEquals("potatoes", pluralize("potato"));
}

    @Test
    public void testAddition() {
        
        assertTrue(pluralize("sheep").equals("sheep"));
        assertTrue(pluralize("qunatity").equals("qunatities"));        
        assertTrue(pluralize(null).equals(null));
        assertEquals("equipment", pluralize("equipment"));
}



    @Test(expected = IllegalArgumentException.class)
    public void testException1() {
        assertEquals("Exception", pluralize("m;ma"));
    }
    @Test(expected = IllegalArgumentException.class)
    public void testException2() {
        assertEquals("Exception", pluralize("bo!ys"));
    }
    @Test(expected = IllegalArgumentException.class)
    public void testException3() {
        assertEquals("Exception", pluralize("bo y"));
    }
    @Test(expected = IllegalArgumentException.class)
    public void testException4() {
        assertEquals("Exception", pluralize(""));
    }
    @Test(expected = IllegalArgumentException.class)
    public void testException5() {
        assertEquals("Exception", pluralize(null));
    }
    @Test(expected = IllegalArgumentException.class)
    public void testException6() {
        assertEquals("Exception", pluralize("hfghgfsgdfgsgsgsgsgryfhfgegdgsdhjdgjshdgshjdgfjsdhgfsjdhgfjhgsdjhgfjsdhgfjgsdjgfjsdhg"));
    }


    @Test
    public void test2() {
        assertTrue(pluralize("cars").equals("cars"));
    }
}
