using Microsoft.AspNetCore.Mvc;

namespace demoapp.Controllers
{
    public class CouncilController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
