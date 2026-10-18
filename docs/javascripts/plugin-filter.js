// Plugin filter for UCV README.md cards
// Expects each card to have data-category attribute and filter buttons with data-filter

document.addEventListener('DOMContentLoaded', function () {
  const filterButtons = document.querySelectorAll('.filter-buttons .md-button');
  const cards = document.querySelectorAll('.md-typeset .grid.cards > *');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const filter = btn.textContent.trim();
      filterButtons.forEach(b => b.classList.remove('md-button--primary'));
      btn.classList.add('md-button--primary');
      cards.forEach(card => {
        const category = (card.getAttribute('data-category') || '').trim();
        const categoryLabel = card.querySelector('.plugin-category, .plugin-category-label')?.textContent.trim();
        const cat = category === 'Plugin' ? categoryLabel : category;
        if (filter === 'All' || category === 'Plugin' || cat === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
});
