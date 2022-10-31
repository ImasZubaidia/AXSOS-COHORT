import java.util.ArrayList;

public class Order{
    private String name;
    private double total;
    private boolean ready;
    private ArrayList<Item> items;

public Order(){
    this.name="Guest";
    this.items=new ArrayList<Item>();
}
public Order(String name){
    this.name=name;
    this.items=new ArrayList<Item>();
}

public void setName(String name){
    this.name=name;
}
public String getName(){
    return this.name;
}
public void setReady(boolean ready){
    this.ready=ready;
}
public boolean isReady(){
    return this.ready;
}
public ArrayList<Item> getItems(){
    return this.items;
} 
public  void setItems(ArrayList<Item> items){
    this.items=items;
}

public void addItem(Item item){
    this.items.add(item);
}

public String getStatusMessage(){
    if (this.ready){
       return "Your order is ready";
    }
    else{
       return "Thank you for waiting, your order will be ready very soon";
    }
}

public double getOrderTotal(){
    for(int i=0;i<items.size();i++){
        this.total+=items.get(i).getPrice();
    }
    return this.total;

}

public void display(){
    System.out.println("Customer name: "+getName());
    for(int i=0;i<items.size();i++){
        System.out.println(items.get(i).getName()+"- $"+items.get(i).getPrice());
    }
    System.out.println("Total: "+getOrderTotal());
}
}