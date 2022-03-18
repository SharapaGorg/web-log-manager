const express = require('express')
const axios = require('axios')

let app = new express()

const API = 'https://shg.radolyn.com/'

app.get('/logs/', (req, res) => {
  // get list of the logs from database
  axios
    .get(API + 'logs')
    .then(result => {
      res.send(result.data)
    })
    .catch(error => {
      res.send(error)
    })
})

module.exports = {
  path: "/api/",
  handler: app
};
