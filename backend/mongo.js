const { MongoClient } = require('mongodb');

const uri = 'mongodb://localhost:27017'; // Replace with your MongoDB connection string
const client = new MongoClient(uri, { useUnifiedTopology: true });

// Connect to the MongoDB database
client.connect((err) => {
  if (err) {
    console.error('Failed to connect to the database:', err);
    return;
  }
  console.log('Connected to the database');
});
