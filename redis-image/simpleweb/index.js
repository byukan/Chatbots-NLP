// index.js contains server logic
const express = require('express');

const app = express();

// set up a single route handler
app.get('/', (req, res) => {
    res.send('Stop right now thank you very much.  I need somebody with a human touch');
});

// set up application to listen on a port
app.listen(8080, () => {
    console.log('Listening on port 8080')
});