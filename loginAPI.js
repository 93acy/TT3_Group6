  // Fetch User
  const fetchUser = async ({username, password}) => {
    const res = await fetch(`http://localhost:5000/login/`, {body:JSON.stringify(data)}), 
    const data = await res.json()

    return data
  }



 
const element = document.querySelector('#post-request .article-id');
const requestOptions = {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({username:'username', password:'password'})
};
fetch('http://localhost:5000/login/', requestOptions)
.then(response => response.json())
.then(data => element.innerHTML = data.id );






  body: JSON.stringify(`http://localhost:5000/login/${username}/${password}`)

    // Add User
    const addUser = async (user) => {
      const res = await fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(user),
      })
  
      const data = await res.json()
  
      setUser([...user, data])

    }