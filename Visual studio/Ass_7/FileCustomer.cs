public class FileCustomer : ICustomer
{
    private readonly string _filePath = "logger.txt";

    public void SaveToFile(List<Customer> customers)
    { 
        using (StreamWriter writer = new StreamWriter(_filePath, true))
        {
            foreach (var customer in customers)
            {
                Console.WriteLine($"{customer.Name}, {customer.Phone}, {customer.Email}, {customer.Age}");
            }
        }
    }
}