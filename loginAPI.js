function handleClick({username, password})

document.write(document.getElementById('username').value);
document.write(document.getElementById('password').value);

const requestOptions = {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({username:document.getElementById('username').value, password:document.getElementById('password').value
})};

fetch('http://localhost:5000/login/', requestOptions)
.then(response => response.json())
.then(data => element.innerHTML = data.id );