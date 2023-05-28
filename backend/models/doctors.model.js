const mongoose = require('mongoose');

const User = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        min: 3,
        max: 20
    },
    email: {
        type: String,
        required: true,
        min: 3,
        max: 20
    },
    password: {
        type: String,
        required: true,
        min: 3,
        max: 20
    },
    date: {
        type: Date,
        default: Date.now
    }
},
{collection: 'users-data'}
)   


const model = mongoose.model('users-data', User)


model.exports = User;

