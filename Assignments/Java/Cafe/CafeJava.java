public class CafeJava {
    public static void main(String[] args) {
        // APP VARIABLES
        // Lines of text that will appear in the app. 
        String generalGreeting = "Welcome to Cafe Java, ";
        String pendingMessage = ", your order will be ready shortly, ";
        String readyMessage = ", your order is ready, ";
        String displayTotalMessage = "Your total is $";

        
        // Menu variables 
        double mochaPrice = 3.5;
        double dripcoffeePrice = 4.5;
        double lattePrice = 5.5;
    
        // Customer name variables 
        String customer1 = "Cindhuri, ";
        String customer2 = "Jimmy, ";
        String customer3 = "Noah, ";
    
        // Order completions 
        boolean isReadyOrder1 = false;
        boolean isReadyOrder2 = true;
        boolean isReadyOrder3 = false;


        System.out.println(generalGreeting + customer1 + displayTotalMessage + mochaPrice); 
        System.out.println(pendingMessage + customer2 + displayTotalMessage + dripcoffeePrice );
        System.out.println(readyMessage + customer3 + displayTotalMessage + lattePrice );
        
    }
}

