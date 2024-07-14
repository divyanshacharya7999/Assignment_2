using System;
using System.Collections.Generic;
using System.Linq;

namespace Ass_4
{
    class Program
    {
        static void Main(string[] args)
        { 
            Dictionary<string, double> productPrices = new Dictionary<string, double>();

            productPrices.Add("Apple", 20);
            productPrices.Add("Banana", 15);
            productPrices.Add("Orange", 10);
            productPrices.Add("Graps", 25);
            productPrices.Add("Bread", 30);

            Console.WriteLine("Product Prices:");
            foreach (var product in productPrices)
            {
                Console.WriteLine($"{product.Key}: {product.Value}");
            }

            double averagePrice = productPrices.Values.Average();
            Console.WriteLine($"\nAverage Price: {averagePrice}");

            var mostExpensiveProduct = productPrices.Aggregate((x, y) => x.Value > y.Value ? x : y);
            Console.WriteLine($"\nMost Expensive Product: {mostExpensiveProduct.Key} - {mostExpensiveProduct.Value}");
        }
    }
}
