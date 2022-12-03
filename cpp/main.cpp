#include <iostream>
using namespace std;

int addNum(int a, int b);
int greatestNum(int c, int d);
int sumOf(int z);

// main() is where program execution begins
int main() {
   cout << "Hello World!\n"; // Prints Hello World with new line
   cout << "Add 36 and 50: " << addNum(36,50) << endl; // Adds 36 and 50 to get 86
   cout << "Greatest number between 100 and 40: " << greatestNum(100,40) << endl; // Determines 20 as
   // the greatest number, so it chooses 20 over 20.
   cout << "Sum from 1 to 35: " << sumOf(35) << endl; // Calculate the sum of values from 1 to 35
   return 0;
}

// Make sure you’ve implemeted at least one function that takes in at least one parameter and returns a value
int addNum(int a, int b){
   return a + b;   
}

// If statement
int greatestNum(int c, int d){
   if (c > d){
      return c;
   }else{
      return d;
   }
}

// For loop
int sumOf(int z){
   int counter = 0;
   for(int i = 1; i <= z; i++){
      counter = counter + i;
   }
   return counter;
}