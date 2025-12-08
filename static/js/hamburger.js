let hamburger = document.getElementById('hamburger');
let hamburgerSidebar = document.getElementById('hamburger-sidebar');
let content = document.getElementById('content');
let sidebar = document.getElementById('sidebar');

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
