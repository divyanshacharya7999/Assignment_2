using System;
using System.Collections.Generic;
using System.Linq;

namespace Ass_5
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<string, List<int>> studentScores = new Dictionary<string, List<int>>();

            studentScores.Add("Aryan", new List<int> { 85, 90, 78 });
            studentScores.Add("Divyansh", new List<int> { 92, 88, 84 });
            studentScores.Add("Obaid", new List<int> { 78, 85, 80 });

            Console.WriteLine("Student Scores:");
            foreach (var student in studentScores)
            {
                Console.WriteLine($"{student.Key}: {string.Join(", ", student.Value)}");
            }

            Console.WriteLine("\nAverage Scores:");
            Dictionary<string, double> studentAverages = new Dictionary<string, double>();
            foreach (var student in studentScores)
            {
                double average = student.Value.Average();
                studentAverages.Add(student.Key, average);
                Console.WriteLine($"{student.Key}: {average}");
            }

            var topStudent = studentAverages.Aggregate((x, y) => x.Value > y.Value ? x : y);
            Console.WriteLine($"\nTop Student: {topStudent.Key} with an average score of {topStudent.Value}");
        }
    }
}
