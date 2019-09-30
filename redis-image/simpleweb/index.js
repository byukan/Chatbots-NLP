// index.js contains server logic
const express = require('express');

cosnst app = express();

// set up a single route handler
app.get('/', (req, res) => {
    res.send('Hi there');
});

// set up application to listen on a port
app.listen(8080, () => {
    console.log('Listening on port 8080')
});