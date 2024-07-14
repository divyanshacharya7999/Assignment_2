using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    { 
        List<string> fruits = new List<string>
        {
            "Apple",
            "Banana",
            "Melon",
            "Graps",
            "Watermelon"
        };

        
        Console.WriteLine(" List of fruits:");
        PrintList(fruits);

       
        fruits.Add("Papaya");
        Console.WriteLine("\nAfter adding a new fruit:");
        PrintList(fruits);

        
        fruits.RemoveAt(1); 
        Console.WriteLine("\nAfter removing the second fruit:");
        PrintList(fruits);

       
        Console.WriteLine($"\nThe third fruit in the list is: {fruits[2]}");

       
        string fruitToCheck = "Apple";
        bool containsFruit = fruits.Contains(fruitToCheck);
        Console.WriteLine($"\nDoes the list contain '{fruitToCheck}'? {containsFruit}");
    }

    static void PrintList(List<string> list)
    {
        foreach (string item in list)
        {
            Console.WriteLine(item);
        }
    }
}
