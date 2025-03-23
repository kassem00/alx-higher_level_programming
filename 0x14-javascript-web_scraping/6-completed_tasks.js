#!/usr/bin/node
const request = require('request');

request('https://jsonplaceholder.typicode.com/todos', function (error, response, body) {
  if (error) {
    console.error(`Error: ${error.message}`);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed with status code: ${response.statusCode}`);
    return;
  }

  const todos = JSON.parse(body);
  const completedByUser = {};

  todos.forEach((todo) => {
    if (todo.completed) {
      completedByUser[todo.userId] = (completedByUser[todo.userId] || 0) + 1;
    }
  });

  console.log(completedByUser);
});
