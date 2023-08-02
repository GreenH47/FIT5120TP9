using System.ComponentModel.DataAnnotations;

namespace coremysql.Models
{
    public class Bill
    {
        /*
         CREATE TABLE bill (
               id INT AUTO_INCREMENT PRIMARY KEY,
               subarea VARCHAR(100),
               electricity FLOAT,
               gas FLOAT,
               carbon FLOAT
            );

         */
        [Key]
        public int Id { get; set; }
        [Required]
        public string Subarea { get; set; }
        public float Electricity { get; set; }
        public float Gas { get; set; }
        public float Carbon { get; set; }
    }
}
