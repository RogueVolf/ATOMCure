const express = require('express')
const cors = require('cors')
const mongoose = require('mongoose')
const app = express()
app.use(cors())
app.use(express.json())
app.get('/',(req,res)=>{
    res.send("ghbjn")
})

app.post('/api/doctor/register',(req,res)=>{
console.log(req.body)
res.json( {status: "ok"})

})

app.listen(8000,()=>{
    console.log("Server Running Okay")
})