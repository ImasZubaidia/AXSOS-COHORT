import java.util.ArrayList;
public class TestOrders{
    public static void main(String[] args){
        
        Item item1 = new Item("mocha", 4);
        Item item2 = new Item("latte", 3.5);
        Item item3 = new Item("drip coffee", 5);
        Item item4 = new Item("capuccino", 4.5);


        Order order1 = new Order("Cindhuri");

        order1.addItem(item1);
        order1.addItem(item3);
        Order order2 = new Order("Jimmy");
        order2.addItem(item4);
        order2.addItem(item3);
        Order order3 = new Order();
        Order order4 = new Order();
        // order1.name = "Cindhuri";
        // order2.name = "Jimmy";
        // order3.name = "Noah";
        // order4.name = "Sam";
        
        order2.addItem(item1);
        // order2.total+=item1.price;
        order3.addItem(item4);
        order3.addItem(item1);
        order4.getStatusMessage();
        // order3.total=item4.price;
        order4.addItem(item2);
        // order4.total=(item2.price)*2;

        
        order1.setReady();
        order2.setReady();
        System.out.println(order2.getStatusMessage());
        System.out.println(order1.getOrderTotal());
      
  }
    
}