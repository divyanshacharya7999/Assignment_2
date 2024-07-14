namespace Ass_6
{ 
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<Person, string> personEmails = new Dictionary<Person, string>();

            var person1 = new Person("Divyansh", "Acharya");
            var person2 = new Person("Aryan", "Awasthi");
            var person3 = new Person("Harsh", "Kapoor");

            personEmails[person1] = "divyanshacharya13@gmail.com";
            personEmails[person2] = "aryanawasthi138@gmail.com";
            personEmails[person3] = "kapoorharsh123@gmail.com";

            Console.WriteLine("Person Emails:");
            foreach (var entry in personEmails)
            {
                Console.WriteLine($"{entry.Key.FirstName} {entry.Key.LastName}: {entry.Value}");
            }

            personEmails[person2] = "aryanawasthi123@newemail.com";
            Console.WriteLine("\nUpdated Emails:");
            foreach (var entry in personEmails)
            {
                Console.WriteLine($"{entry.Key.FirstName} {entry.Key.LastName}: {entry.Value}");
            }

            personEmails.Remove(person3);
            Console.WriteLine("\nAfter Removing Harsh Kapoor:");
            foreach (var entry in personEmails)
            {
                Console.WriteLine($"{entry.Key.FirstName} {entry.Key.LastName}: {entry.Value}");
            }
        }
    }
}
