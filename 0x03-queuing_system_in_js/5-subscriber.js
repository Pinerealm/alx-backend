import redis from 'redis';

const client = redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.error(`Redis client not connected to the server: ${error.message}`));

  // Subscribe to the 'holberton school channel'
  client.subscribe('holberton school channel');
  // Log to the console when a message is received
  client.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe();
      client.quit();
    }
  });
