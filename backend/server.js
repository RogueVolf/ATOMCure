const express = require('express')
const cors = require('cors')
const app = express()
const mongoose = require('mongoose')
app.use(express.json())
app.use(cors())




mongoose.connect('mongodb+srv://admin:admin@cluster0.m42pgzw.mongodb.net/?retryWrites=true&w=majority',)



app.listen(8000,()=>{
    console.log("Server Running Okay")
}
)