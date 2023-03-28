#!/usr/bin/node dev
import {createClient, print} from 'redis'

const client = createClient();
const key = 'HolbertonSchools';

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString())
})

const updateHash = (hash, field, value) => {
    client.HSET(hash, field, value, print)
}

const printHash = (hash) => {
    client.HGETALL(hash, (err, reply) => console.log(reply))
}

const data = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
}

function main(){
    for (const [field, value] in Object.entries(data)){
        updateHash(key, field, value)
    }
    printHash(key)
}
client.on('connect', () => {
    console.log('Redis client connect to the server');
    main();
})
