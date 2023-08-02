using Microsoft.EntityFrameworkCore;
using coredemo.Models;
namespace coredemo.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions options) : base(options)
        {
        }

        public DbSet<BillEntity> Bills { get; set; }
    }
}
