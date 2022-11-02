package com.imas.axsos;

import java.text.SimpleDateFormat;
import java.util.Date;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class HomeController {
    @RequestMapping("/")
    public String index(Model model) {
        return "index.jsp";
    }
    
    @RequestMapping("/date")
    public String date(Model model) {
    	// here we use SimpleDateFormat to display our date as seen in the wireframe
    	// we have to use a separate variable for each piece because we will add additional text later
    	// for more help, have a look at the official documentation: https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html
    	SimpleDateFormat dayNameFormat = new SimpleDateFormat("EEEE");
    	SimpleDateFormat dayFormat = new SimpleDateFormat("dd");
    	SimpleDateFormat monthFormat = new SimpleDateFormat("MMMM");
    	SimpleDateFormat yearFormat = new SimpleDateFormat("Y");
    	
    	Date date = new Date();
    	
    	String dayNameString = dayNameFormat.format(date);
    	String dayString = dayFormat.format(date);
    	String monthString = monthFormat.format(date);
    	String yearString = yearFormat.format(date);
    	
    	String dateString = dayNameString + ", " + "the " + dayString + " of " + monthString + ", " + yearString;
    	// for an extra challenge, try to add 'st', 'nd', 'rd', or 'th' based on the date
    	// Example: Monday, the 3rd of March, 2023
    	
    	model.addAttribute("dateString", dateString);
    	
        return "date.jsp";
    }
    
    @RequestMapping("/time")
    public String time(Model model) {
    	SimpleDateFormat format = new SimpleDateFormat("h:mm a");
    	
    	Date date = new Date();
    	
    	String timeString = format.format(date);
    	
    	model.addAttribute("timeString", timeString);
    	
        return "time.jsp";
    }
}