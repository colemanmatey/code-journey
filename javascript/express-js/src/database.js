import 'dotenv/config';
import { MongoClient } from "mongodb";

const password = encodeURIComponent(process.env.DB_PASSWORD) // handle special characters in password
const uri = `mongodb+srv://${process.env.DB_USERNAME}:${password}@babysteps.xbrc2ub.mongodb.net/?retryWrites=true&w=majority&appName=BabySteps`;

async function execute(task) {
    const client = new MongoClient(uri);

    try {
        await client.connect();
        console.log("Connected to MongoDB");

        return await task(client);
    } catch (error) {
        console.error("Error interacting with MongoDB:", error);
    } finally {
        await client.close();
        console.log("MongoDB connection closed");
    }
}


export async function getDBList(client) {
    const dbList = await client.db().admin().listDatabases();
    dbList.databases.forEach(db => console.log(db.name));
}

export async function getAllMovies(client) {
    return await client.db("sample_mflix").collection("movies").find({year: 2015}).toArray();;
}


export async function createUser(client, user) {
    const result = await client.db("sample_mflix").collection("users").insertOne(user);
    console.log("New user created with id:" + result.insertedId);
}

export default execute;