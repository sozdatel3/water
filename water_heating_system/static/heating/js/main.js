window.addEventListener('scroll', () => {
    if (window.scrollY > 50 || window.pageYOffset >= 50) {
      document.getElementsByTagName('header')[0].classList.add('backdrop-blur-md', 'bg-black/20')
    } else {
      document.getElementsByTagName('header')[0].classList.remove('backdrop-blur-md', 'bg-black/20')
    }
  })