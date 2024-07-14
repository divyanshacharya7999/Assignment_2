using System;
using System.Collections.Generic;

namespace Ass_3
{
    class Program
    {
        static void Main(string[] args)
        {
            
            Dictionary<string, int> studentScores = new Dictionary<string, int>();
           
            studentScores.Add("Divyansh", 95);
            studentScores.Add("Obaid", 92);
            studentScores.Add("Aryan", 78);
            studentScores.Add("Chandragupt", 89);
            studentScores.Add("Uday", 85);
          
            Console.WriteLine("Student Scores:");
            foreach (var student in studentScores)
            {
                Console.WriteLine($"{student.Key}: {student.Value}");
            }
        
            studentScores["Aryan"] = 82;
            Console.WriteLine("\nUpdated Scores:");
            foreach (var student in studentScores)
            {
                Console.WriteLine($"{student.Key}: {student.Value}");
            }

            studentScores.Remove("Uday");
            Console.WriteLine("\nAfter Removing Uday:");
            foreach (var student in studentScores)
            {
                Console.WriteLine($"{student.Key}: {student.Value}");
            }

            Console.WriteLine($"\nScore of Divyansh: {studentScores["Divyansh"]}");
        }
    }
}
