import java.util.ArrayList;

public class CoffeeKiosk{
    private ArrayList<Item> menu;
    private ArrayList<Order> orders;


public CoffeeKiosk(){
    this.menu=new ArrayList<Item>();
    this.orders=new ArrayList<Order>();

}

public void addMenuItem(String name, double price){
    Item item=new Item(name, price);
    this.menu.add(item);
    item.setIndex(menu.size()-1);
         
          //because we want to change the value             
}



public void displayMenu(){
    for (int i=0;i<menu.size();i++){
    System.out.println(i + " "+menu.get(i).getName()+"--$"+menu.get(i).getPrice());
    }
   }


    public void newOrder() {
        
    	// Shows the user a message prompt and then sets their input to a variable, name
        System.out.println("Please enter customer name for new order:");
        String name = System.console().readLine();
    
    	// Your code:
        // Create a new order with the given input string
        Order order=new Order(name);
        // Show the user the menu, so they can choose items to add.
        displayMenu();
        
    	// Prompts the user to enter an item number
        System.out.println("Please enter a menu item index or q to quit:");
        String itemNumber = System.console().readLine();
        
        // Write a while loop to collect all user's order items
        while(!itemNumber.equals("q")) {
            
            // Get the item object from the menu, and add the item to the order
            Item item =this.menu.get(Integer.parseInt(itemNumber));
            order.addItem(item);
            // Ask them to enter a new item index or q again, and take their input
            System.out.println("Please enter a menu item index or q to quit:");
            itemNumber = System.console().readLine();
        }
        // After you have collected their order, print the order details 
        order.display();//that was created in the order class//
    	// as the example below. You may use the order's display method.
        
    }
}