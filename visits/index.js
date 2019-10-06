// holds all of our actual application code
//requre libraries
const express = require('express');
const redis = require('redis');

// instance of express application
const app = expreess();
// set up connection to redis server
// eventually we'll specify the host/url/address we're trying to connect to
const client = redis.createClient();
client.set('visits', 0);

// route handler for root route
app.get('/', (req, res) => {
    client.get('visits', (err, visits) => {
        res.send('Number of visits is ' + visits);
        // update number of times this page has been visited
        client.set('visits', parseInt(visits) + 1);
    });
});

app.listen(8081, () => {
     console.log('Listening on port 8081');
});