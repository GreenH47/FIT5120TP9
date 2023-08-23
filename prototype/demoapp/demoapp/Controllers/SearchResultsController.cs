using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;
using System;
using System.Net.Http;
using System.Threading.Tasks;
using Newtonsoft.Json;
using System.Text;

namespace demoapp.Controllers
{
    public class SearchResultsController : Controller
    {
        public async Task<IActionResult> Index(string search)
        {
            var searchObject = new { searchWord = search };
            var searchJson = JsonConvert.SerializeObject(searchObject);

            ViewData["SearchJson"] = searchJson;
            ViewData["SearchWord"] = search;

            var apiUrl = "https://2rfrtk7vz4.execute-api.us-east-1.amazonaws.com/deploy";
            var content = new StringContent(searchJson, Encoding.UTF8, "application/json");

            
            using (var client = new HttpClient())
            {
                var response = await client.PostAsync(apiUrl, content);
                var searchResultJson = await response.Content.ReadAsStringAsync();
                ViewData["SearchResult"] = searchResultJson;

            }
            

            return View("Index");

        }
    }



}
