package edu.depaul.se433;

public class StringUtil {

  public static String pluralize(String word) {
    if (word != null) {
      for (int i = 0; i < punct.length(); i++) { 
	if (word.indexOf(punct.charAt(i)) >= 0) 
	  throw new IllegalArgumentException();
      }

      int i;
      int len = uncountable.length;
      for (i = 0; i < len; i++) {
        if (word.equals(uncountable[i])) {
          return word;
        }
      }

      len = irregular.length;
      for (i = 0; i < len; i++) {
        String s1 = irregular[i][0];
        if (word.equals(s1)) {
          return irregular[i][1];
        }
      }

      len = plural.length;
      for (i = 0; i < len; i++) {
        String s1 = plural[i][0];
        if (word.endsWith(s1)) {
          int l = word.length() - s1.length();
          return (word.substring(0, l) + plural[i][1]);
        }
      }

      int l = word.length();
      char c1 = word.charAt(l - 1);
      char c2 = word.charAt(l - 2);
      if (c1 == 'y' &&
          (c2 != 'a' || c2 != 'e' || c2 == 'i' || c2 == 'o' || c2 == 'u')) {
        return (word.substring(0, l - 1) + "ies");
      }
      return (word + "s");
    }
    return null;
  }

  static final String[][] plural = { 
      { "axis", "axes" },
      { "octopus", "octopi" }, 
      { "virus", "viri" }, 
      { "sis", "ses" },
      { "s", "ses" }, 
      { "o", "oes" }, 
      { "ium", "ia" }, 
      { "f", "ves" },
      { "ox", "oxen" }, 
      { "x", "xes" }, 
      { "ch", "ches" }, 
      { "sh", "shes" },
      { "matrix", "matrices" }, 
      { "vertex", "vertices" },
      { "index", "indices" }, 
      { "mouse", "mice" }, 
      { "louse", "lice" },
      { "man", "men" }, 
      { "quiz", "quizzes" }, 
  };

  static final String[][] irregular = { 
      { "person", "people" },
      { "child", "children" }, 
  };

  static final String[] uncountable = { 
      "equipment", 
      "information", 
      "rice",
      "money", 
      "species", 
      "series", 
      "fish", 
      "sheep", 
  };

  static final String punct = ",./<>?;\':\"[]\\{}|~!@#$%^&*()_+-=";

  public static void main(String[] args) {
    String[] words = { "car", "woman", "house", "quality" };
    for (int i = 0; i < words.length; i++) { 
      System.out.println("The plural of " + words[i] + " is " + pluralize(words[i]));
    }
  }  

}
