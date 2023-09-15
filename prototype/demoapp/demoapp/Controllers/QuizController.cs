using Microsoft.AspNetCore.Mvc;
using System.Text.Encodings.Web;

namespace MvcMovie.Controllers;
using System.Net.Http;
using System.Threading.Tasks;

public class QuizController : Controller
{
    
    public IActionResult Index()
    {
        return View();
    }


}