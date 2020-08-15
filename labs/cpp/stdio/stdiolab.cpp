/*	
	Lab 1 - ASCII Art and Standard IO

 	By: FIXME - Your name
 	CSCI 111
 	Date: FIXME…

 	This program produces an ASCII art on the console.

	Algorithm Steps: Write a series of cout statements to print 
	the art to the console.
*/

#include <iostream> //library for input and output 
#include <string>

using namespace std; //resolve cout, cin, and endl names

//main entry point of the program
int main()
{
  string name; // variable to store user's name
  cout << "Hi there, what's your full name? ";
  getline(cin, name);
  cout << "Nice meeting you, " << name << "!" << endl;
  cout << "Hope you'll like my ASCII art...\n";

  cout << "  |\\_/|   ******************    (\\_/)" << endl;
  cout << " / @ @ \\  *       Lab 1    *   (=\'.\'=)" << endl;

  //FIXME: complete the rest of the ASCII art as shown in the description

  return 0; //exit program by returning 0 status to the system
}