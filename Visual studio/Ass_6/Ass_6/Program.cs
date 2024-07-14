using System;

namespace ShoppingPortal
{
    public interface IShoppingPortal
    {
        void PlaceOrder();
    }

    public class AmazonPortal : IShoppingPortal
    {
        public void PlaceOrder()
        {
            Console.WriteLine("Ordered from Amazon");
            Console.ReadLine();
        }
    }

    public class FlipkartPortal : IShoppingPortal
    {
        public void PlaceOrder()
        {
            Console.WriteLine("Ordered from Flipkart");
            Console.ReadLine();
        }
    }

    public class ShoppingManager
    {
        public readonly IShoppingPortal _shoppingPortal;

        public ShoppingManager(IShoppingPortal shoppingPortal)
        {
            _shoppingPortal = shoppingPortal;
        }

        public void Order()
        {
            _shoppingPortal.PlaceOrder();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            
            string portal = "Amazon"; 

            IShoppingPortal shoppingPortal;
            if (portal == "Amazon")
            {
                shoppingPortal = new AmazonPortal();
            }
            else if (portal == "Flipkart")
            {
                shoppingPortal = new FlipkartPortal();
            }
            else
            {
                throw new Exception("Unknown shopping portal");
            }

            ShoppingManager manager = new ShoppingManager(shoppingPortal);
            manager.Order();
        }
    }
}

