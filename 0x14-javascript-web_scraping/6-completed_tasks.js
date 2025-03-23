#!/usr/bin/node
const request = require('request');

// Check if URL argument is provided
if (process.argv.length < 3) {
  console.error('Usage: ./6-completed_tasks.js <URL>');
  process.exit(1);
}

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error(`Failed with status code: ${response.statusCode}`);
    process.exit(1);
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
