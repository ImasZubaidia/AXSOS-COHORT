import java.util.ArrayList;

public class ExceptionsList {
    static ArrayList myList = new ArrayList<Integer>();
    public static void main(String[] args) {

        // Create a hardcoded array list with strings and integers
        myList.add("13");
        myList.add("hello world");
        myList.add(48);
        myList.add("Goodbye World");

        // Looping through the array list, it tries to assign each item to an integer object
        for(int i = 0; i < myList.size(); i++) {
            try {
                int castedValue = (Integer) myList.get(i);
            }
            // If the item is not an integer, it will catch the exception
            // and print that it is an exception along with what the exception was
            catch(ClassCastException exception){
                exception.printStackTrace();
                System.out.println("Caught exception: " + myList.get(i));
            }
        }
    }
}