/* Program Description: 
* This program connects to an animal shelter database housed on Mongo DB. It then demonstrates the
* ability to perform all CRUD operations. The program can add a record, find that record, update
* that record, and then delete that record. Most of the functions are performed as asyncronous 
* functions that use the await feature to ensure that promises are fulfilled before the program 
* moves on. This is necessary as the script is interacting with a server that could take a varying
* amount of time to fulfill requests.
*/

// Creates a constant representing the MongoClient
const {MongoClient} = require('mongodb');

// Declares main function as async due to use of await for connections that return promises
async function main() {

    // Constant representing uri of the database used for demonstration
    const uri = "mongodb+srv://AdminRoss:RossSecure@project-animal-shelter.m9n4i7l.mongodb.net/?retryWrites=true&w=majority";
    
    // Constant Mongo Client created with uri
    const client = new MongoClient(uri);

    // Try where we connect to and manipulate data
    try {
        // Connects the client to Mongodb
        await client.connect();

        // Creates a record, then finds it to ensure it was added, updates the record, and then deletes it
        await addRecord(client, {animalName: "Anya", 
            animalSpecies: "Cat", 
            animalBreed: "Japanese Bobtail", 
            animalColor: "White", 
            animalAge: "1", 
            animalGender: "Female", 
            wasAdopted: "N"});

        await findRecord(client, "Anya");

        await updateRecord(client, "Anya", "Y");

        await deleteRecord(client, "Anya");

    } 
    // Catches errors from asyncronous function calls and prints the error
    catch (e) {
        console.error(e);
    } 
    // Ensures close of client
    finally {
        await client.close();
    }

}

// Function to list available databases from Mongo Client
async function listDatabases(client) {

    const databaseList = await client.db().admin().listDatabases();

    // Prints each database in the client
    console.log("Databases:");
    databaseList.databases.forEach(db => {console.log(`- ${db.name}`)});
}

// Adds a new record to the database
async function addRecord(client, newRecord) {
    const result = await client.db("animalShelter").collection("animalShelter").insertOne(newRecord);

    // Message alerting user that record has been added
    console.log(`New record has been added with ID: ${result.insertedId}`);
}

// Searches for records based on user input
async function findRecord(client, valueToSearch) {
    const result = await client.db("animalShelter").collection("animalShelter").findOne({animalName: valueToSearch});

    // Informs user where a record was found or not
    if (result) {
        console.log(`Record found`);
    }
    else {
        console.log("No record found");
    }
}

// Function that receives a record value, and then updates the record with new values
async function updateRecord(client, query, update) {
    const result = await client.db("animalShelter").collection("animalShelter").updateOne({animalName: query}, {$set: {wasAdopted: update}});

    // Informs user whether the record could be found and updated
    if(result) {
        console.log(`Record was found and updated.`);
    }
    else {
        console.log("No record was found to update.")
    }

}

// Function that receives a record and deletes it
async function deleteRecord(client, record) {
    const result = await client.db("animalShelter").collection("animalShelter").deleteOne({animalName: record});

    // Informs user that the record was deleted from the database properly
    if(result) {
        console.log(`Document was found and deleted!`);
    }
    else {
        console.log("No documents were found with that name.")
    }
}

// Execute main function
main().catch(console.error);