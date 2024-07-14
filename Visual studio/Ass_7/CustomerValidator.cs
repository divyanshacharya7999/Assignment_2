public class CustomerValidator
{
    public bool IsValid(Customer customer)
    {
        if (customer.Age < 18)
        {
            Console.WriteLine("Error: Age must be 18 or older.");
            return false;
        }
        return true;
    }
}