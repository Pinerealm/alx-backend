import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
}

function displaySchoolValue(schoolName) {
  const asyncGet = promisify(client.get).bind(client);
  asyncGet(schoolName).then(console.log);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
