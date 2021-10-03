
package edu.depaul.se433;

import org.junit.*;
import static org.junit.Assert.*;
import static edu.depaul.se433.StringUtil.*;

public class StringUtilTest {
    @Test
    public void test(){
        //Uncountable
        assertEquals("water",pluralize("water"));
        assertEquals("meat",pluralize("meat"));
        // regular
        assertEquals("cars",pluralize("car"));
        assertEquals("books",pluralize("book"));
        // -es after sibilants
        assertEquals("sandwiches",pluralize("sandwich"));
        assertEquals("fishes",pluralize("fish"));
        // Substitute y after consonant with -ies
        assertEquals("families",pluralize("family"));
        assertEquals("butterflies",pluralize("butterfly"));
        // Add -s after vowel + y
        assertEquals("days",pluralize("day"));
        assertEquals("monkeys",pluralize("monkey"));
        // Nouns on -f or -fe
        assertEquals("wives",pluralize("wife"));
        assertEquals("wolves",pluralize("wolf"));
        // Nouns on -o form the plural by adding -s or -es
        assertEquals("potatoes",pluralize("potato"));
        assertEquals("tomatoes",pluralize("tomato"));
        // Irregular plural forms
        assertEquals("men",pluralize("man"));  
        assertEquals("children",pluralize("child")); // Irregular plural forms
        
    }
    @Test(expected=IllegalArgumentException.class)
    public void test2(){
	   assertEquals("Exception",pluralize("m;ma"));
           assertEquals("Exception",pluralize(""));
           assertEquals("Exception",pluralize("1111"));           
           fail();
    }
}