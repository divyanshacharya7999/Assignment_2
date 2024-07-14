class Program
{
    static void Main(string[] args)
    {
        var customers = new List<Customer>();
        var validator = new CustomerValidator();
        var SaveFile = new FileCustomer();


        while (true)
        {
            Console.WriteLine("Enter Customer Details");
            Console.Write("Name: ");
            var name = Console.ReadLine();
            if (name == "exit") break;


            Console.Write("Phone: ");
            var phone = Console.ReadLine();

            Console.Write("Email: ");
            var email = Console.ReadLine();

            Console.Write("Age: ");
            var age = int.Parse(Console.ReadLine());

            var customer = new Customer
            {
                Name = name,
                Phone = phone,
                Email = email,
                Age = age
            };


            customers.Add(customer);


            SaveFile.SaveToFile(customers);
            Console.WriteLine("Customer details saved to logger.txt.");

        }
    }
}