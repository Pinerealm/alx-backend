import redis from 'redis';
import { createClient } from 'redis';

const client = createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, reply) => {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
