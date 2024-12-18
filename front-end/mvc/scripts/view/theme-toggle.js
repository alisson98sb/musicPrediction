const themeToggleButton = document.getElementById('theme-toggle');
const body = document.body;

// Verificar o tema armazenado no localStorage
const savedTheme = localStorage.getItem('theme');
if (savedTheme) {
  body.classList.toggle('light', savedTheme === 'light');
}

// Alternar entre temas
themeToggleButton.addEventListener('click', () => {
  body.classList.toggle('light');
  
  // Salvar o tema escolhido no localStorage
  const newTheme = body.classList.contains('light') ? 'light' : 'dark';
  localStorage.setItem('theme', newTheme);
});
