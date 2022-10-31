import java.util.ArrayList;
public class Test{
    public static void main(String[] args){
        Order order1=new Order();
        Order order2=new Order();


        Order order3=new Order("Aseel");
        Order order4=new Order("Hadeel");
        Order order5=new Order("Shatha");


        Item item1=new Item("mocha",3.5);
        Item item2=new Item("latte",4);
        Item item3=new Item ("Coffee",4.5);


        order1.addItem(item3);
        order1.addItem(item3);

        order2.addItem(item2);
        //and so on
        order1.display();
        //no name except "guest"

        System.out.println(order1.getStatusMessage());
        order4.isReady();
        System.out.println(order4.getStatusMessage());


    
    /////////////coffee64//
CoffeeKiosk test=new CoffeeKiosk();
test.addMenuItem("coffee",1);
test.addMenuItem("latte",2);
test.addMenuItem("tea",3.5);
test.newOrder(); //or test.displayMenu();

 }
}