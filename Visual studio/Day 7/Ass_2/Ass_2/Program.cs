using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
      
        List<int> numbers = new List<int> { 42, 16, 23, 8, 4, 15, 29, 91, 60, 37 };

        numbers.Sort();
        Console.WriteLine("List sorted in ascending order:");
        PrintList(numbers);

       
        numbers.Sort((a, b) => b.CompareTo(a));
        Console.WriteLine("\nList sorted in descending order:");
        PrintList(numbers);

        
        int searchNumber = 15;
        bool found = numbers.Contains(searchNumber);
        Console.WriteLine($"\nIs the number {searchNumber} in the list? {found}");
    }

    static void PrintList(List<int> list)
    {
        foreach (int item in list)
        {
            Console.WriteLine(item);
        }
    }
}
