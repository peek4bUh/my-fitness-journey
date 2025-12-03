var hamburger = document.getElementById('hamburger');
var hamburgerSidebar = document.getElementById('hamburgerSidebar');
var content = document.getElementById('content');
var sidebar = document.getElementById('sidebar');

hamburger.addEventListener('click', () => {
  sidebar.classList.toggle('hidden');
});

hamburgerSidebar.addEventListener('click', () => {
  sidebar.classList.toggle('hidden');
});

content.addEventListener('click', () => {
  if (!sidebar.classList.contains('hidden')) {
    sidebar.classList.add('hidden');
  }
});
