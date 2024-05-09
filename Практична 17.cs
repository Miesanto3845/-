using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;

namespace NobelLaureatesApp.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class NobelLaureatesController : ControllerBase
    {
        private readonly IHttpClientFactory _clientFactory;

        public NobelLaureatesController(IHttpClientFactory clientFactory)
        {
            _clientFactory = clientFactory;
        }

        [HttpGet]
        public async Task<IEnumerable<NobelLaureate>> Get(string search = "")
        {
            var client = _clientFactory.CreateClient();
            var response = await client.GetAsync("https://api.nobelprize.org/v1/laureate/");
            
            if (response.IsSuccessStatusCode)
            {
                var responseStream = await response.Content.ReadAsStreamAsync();
                var laureates = await JsonSerializer.DeserializeAsync<List<NobelLaureate>>(responseStream);
                
                if (!string.IsNullOrWhiteSpace(search))
                {
                    // Фільтруємо за пошуковим запитом
                    return laureates.FindAll(laureate => laureate.FullName.Contains(search, StringComparison.OrdinalIgnoreCase));
                }

                return laureates;
            }
            else
            {
                // Обробка помилок
                return null;
            }
        }
    }

    public class NobelLaureate
    {
        public string Id { get; set; }
        public string FullName { get; set; }
        public string BirthDate { get; set; }
        public string BirthPlace { get; set; }
        public string Motivation { get; set; }
        // Додаткові поля
    }
}
