using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using Newtonsoft.Json;

namespace demoapp.Controllers
{
    public class SearchResultsController : Controller
    {
        public IActionResult Index(string search)
        {
            var searchObject = new { searchWord = search };
            var searchJson = JsonConvert.SerializeObject(searchObject);

            ViewData["SearchJson"] = searchJson;
            ViewData["SearchWord"] = search;

            return View("Index");

        }
    }



}
