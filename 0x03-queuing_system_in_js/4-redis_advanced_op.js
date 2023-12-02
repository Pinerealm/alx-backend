import redis from 'redis';

const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

const hash = 'HolbertonSchools';
const values = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// Store the above object in Redis as a Hash
for (const [key, value] of Object.entries(values)) {
  client.hset(hash, key, value, redis.print);
}

// Retrieve all values of the hash
client.hgetall(hash, (error, reply) => {
  console.log(reply);
});
