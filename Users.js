const Users = (users) => {
  return (
    <>
      {users.map((user) => (
        <User user={user} />
      ))}
    </>
  )
}

export default Users