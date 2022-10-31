package com.codingdojo.zoo;

public class Bat extends Mammal {

	private int energyLevel;
	public Bat() {
		super(300);
		// TODO Auto-generated constructor stub
	}

	public Bat(int energyLevel) {
		super(energyLevel);
		// TODO Auto-generated constructor stub
	}
	public void flyBat() {
		System.out.println("sound a bat taking off ");
		this.energyLevel-=50;
	}
	public void eatHumans(){
		System.out.println("so- well, never mind,  ");	
		this.energyLevel+=25;
		
	}
	public void attackTown() {
		System.out.println("sound of a town on fire");	
		this.energyLevel-=100;
	}

	public void displayEnergy() {
		// TODO Auto-generated method stub
		
	}
	
}