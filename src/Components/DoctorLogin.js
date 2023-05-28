import React from 'react'
import { useState } from 'react'
import NavBar from './NavBar'

export default function DoctorLogin() {


  const [name,setName] = useState('')
  const [email,setEmail] = useState("")
  const [password,setPassword] = useState('')

  async function registerDoctor(event){
    event.preventDefault()
    const response = await fetch('http://localhost:8000/api/doctor/register',{
      method: 'POST',

    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      name: name,
      email: email,
      password: password
    }),
  })
  const data = await response.json()
  console.log(data)
}


  return (
    <>
      <NavBar/>


<p>DOCTOR's Login</p>





<form onSubmit={registerDoctor}>
<input type="text" placeholder='Name' value={name} onChange={(e) => setName(e.target.value)} />
<br/><input type="email" placeholder='Email' value={email} onChange={(e) => setEmail(e.target.value)}/>
<br/><input type="passworrd" placeholder='password' value={password} onChange={(e) => setPassword(e.target.value)}/>
<br/><input type="submit" value="Register" />
</form>




    </>
  )
}
