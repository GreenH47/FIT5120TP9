using coremysql.Models;
using Microsoft.AspNetCore.Mvc;
using MySql.Data.MySqlClient;
using System.Diagnostics;

namespace coremysql.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }
        // connect to mysql and fetch data
        //tutorial https://www.youtube.com/watch?v=KRnW3CedU58
        public IActionResult Index()
        {
            List<Bill> bills = new List<Bill>();


            var connectionString = "Server=carbonvic.clx2a8hznypy.us-east-1.rds.amazonaws.com;Database=test;User=greenh47;Password=RRCgwXAfWw53cej";
            //connect to mysql
            using(MySqlConnection mysqlCon = new MySqlConnection(connectionString))
            {
                mysqlCon.Open();
                // test connection
                MySqlCommand cmd = new MySqlCommand("select * from bill", mysqlCon);

                MySqlDataReader reader = cmd.ExecuteReader();

                while(reader.Read())
                {
                    // fetch and extract data
                    Bill bill = new Bill();
                    bill.Id = Convert.ToInt32(reader["id"]);
                    bill.Subarea = reader["subarea"].ToString();
                    bill.Electricity = Convert.ToSingle(reader["electricity"]);
                    bill.Gas = Convert.ToSingle(reader["gas"]);
                    bill.Carbon = Convert.ToSingle(reader["carbon"]);

                    // add to list
                    bills.Add(bill);
                }
                reader.Close();
                mysqlCon.Close();
            }
            return View(bills);
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}