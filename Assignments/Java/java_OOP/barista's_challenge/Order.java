import java.util.ArrayList;

public class Order{

private String name;
private double total;
private boolean ready;
private ArrayList<Item> items;

public Order(){
    this.name="";
    this.items=new ArrayList<Item>();
}
// public Order(String nombre, boolean ready){
//     this.name=nombre;
//     this.ready=ready;
//     ArrayList<Item> items=new ArrayList<Item>();
// }
public Order(String nombre){
    this.name=nombre;
    this.items=new ArrayList<Item>();

}

public String getName(){
    return name;
}
public void setName(String name){
    this.name=name;
}
public double getTotal(){
    return total;
}
public void setTotal(double total){
    this.total=total;
}
public boolean getReady(){
    return ready;
}


public String getStatusMessage(){
    if(this.ready==true){
        return "Your order is ready";   
    }
    else {
        return "Thank you for waiting, your order will be ready soon";
    }
    
}


public double getOrderTotal(){
    double sum = 0.0;
    for(Item item : this.items){
        sum+=item.getPrice();

    }
    return sum;
    }

public void display() {
    
    System.out.println("customer :" + this.name);
    for (Item item : this.items) {
      System.out.println(item.getName() + " " +item.getPrice());
      
    }
    System.out.println("Total price is : " + this.getOrderTotal());
  }


  public void addItem(Item nItem) {
    this.items.add(nItem);
    
  }

  public void setReady(){
    this.ready=true;
  }
}