  // Fetch Name
  const fetchUsers = async () => {
    const res = await fetch('http://localhost:5000/users')
    const data = await res.json()

    return data
  }

    // Add Task
    const addUser = async (user) => {
      const res = await fetch('http://localhost:5000/users', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json',
        },
        body: JSON.stringify(user),
      })
  
      const data = await res.json()
  
      setUser([...user, data])
  
      // const id = Math.floor(Math.random() * 10000) + 1
      // const newTask = { id, ...task }
      // setTasks([...tasks, newTask])
    }