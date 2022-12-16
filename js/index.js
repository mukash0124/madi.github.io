const links = document.getElementById('links')
const db = JSON.parse(localStorage.getItem('db'))
const email = sessionStorage.getItem('email')

function logOut() {
    sessionStorage.clear()
}

if(email){
    const name = `${db[email]['name']} ${db[email]['surname']}`
    links.innerHTML = `
    <li class="nav-item">
        <a class="nav-link active" href="#">${name}</a>
    </li>
    <li class="nav-item">
        <a class="nav-link" href="/" id="logout">Выйти</a>
    </li>
    `
}
else{
    links.innerHTML = `
    <li class="nav-item">
        <a class="nav-link active" href="/auth.html">Войти</a>
    </li>
    <li class="nav-item">
        <a class="nav-link active" href="/signup.html">Зарегистрироваться</a>
    </li>
    `
}

const button = document.getElementById('logout')
button.addEventListener('click', logOut)