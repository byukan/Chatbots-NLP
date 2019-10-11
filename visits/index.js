// holds all of our actual application code
//requre libraries
// import express from 'express';
// import { createClient } from 'redis';
const express = require('express');
const redis = require('redis');
const process = require('process');

// instance of express application
const app = express();
// set up connection to redis server
// specify the host/url/address we're trying to connect to
const client = redis.createClient({
    host: 'redis-server',
    post: 6379
});
client.set('visits', 0);

// route handler for root route
app.get('/', (req, res) => {
    process.exit(0);  // exit status code, 0 means we exited and everything is OK
    client.get('visits', (err, visits) => {
        res.send('Number of visits is ' + visits);
        // update number of times this page has been visited
        client.set('visits', parseInt(visits) + 1);
    });
});

app.listen(8081, () => {
     console.log('Listening on port 8081');
});