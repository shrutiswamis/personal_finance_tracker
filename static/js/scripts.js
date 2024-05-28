document.addEventListener('DOMContentLoaded', function() {
    // Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        target.scrollIntoView({
          behavior: 'smooth'
        });
      });
    });
  
    // Format stock prices and changes
    const stockPrices = document.querySelectorAll('.stock-price');
    const stockChanges = document.querySelectorAll('.stock-change');
    stockPrices.forEach(price => {
      price.textContent = formatCurrency(price.textContent);
    });
    stockChanges.forEach(change => {
      const value = parseFloat(change.textContent);
      if (value >= 0) {
        change.classList.add('positive');
        change.textContent = '+' + formatPercent(value);
      } else {
        change.classList.add('negative');
        change.textContent = '-' + formatPercent(Math.abs(value));
      }
    });
  
    // Format currency values
    function formatCurrency(value) {
      return '$' + parseFloat(value).toFixed(2);
    }
  
    // Format percent values
    function formatPercent(value) {
      return (value * 100).toFixed(2) + '%';
    }
  
    // Filter stock prices
    const stockFilter = document.getElementById('stock-filter');
    const stockTableRows = document.querySelectorAll('#stock-table tbody tr');
    stockFilter.addEventListener('input', function() {
      const filterValue = this.value.toLowerCase();
      stockTableRows.forEach(row => {
        const symbol = row.querySelector('td:first-child').textContent.toLowerCase();
        const name = row.querySelector('td:nth-child(2)').textContent.toLowerCase();
        if (symbol.includes(filterValue) || name.includes(filterValue)) {
          row.style.display = 'table-row';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });