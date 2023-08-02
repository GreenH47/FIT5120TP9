using coredemo.Data;
using System.ComponentModel;

namespace coredemo.Models
{
    public class BillEntity
    {
        private AppDbContext context;
        public int Id { get; set; }
        [DisplayName("Subarea you living")]
        public string Subarea { get; set; }
        [DisplayName("Electricity Bill")]
        public float Electricity { get; set; }
        [DisplayName("Gas Bill")]
        public float Gas { get; set; }
        [DisplayName("Carbon emmission")]
        public float Carbon { get; set; }
    }

}
