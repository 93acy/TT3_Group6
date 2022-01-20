  // Fetch User
  const fetchUser = async ({username, password}) => {
    const res = await fetch(`http://localhost:5000/login/${username}${password}`)
    const data = await res.json()

    return data
  }

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