const mongodb = require('mongodb');
const MongoClient = mongodb.MongoClient;

// const dbName = process.env.MYSQL_DB || 'node-complete';
// const dbUser = process.env.MYSQL_USER || 'root';
// const dbPass = process.env.MYSQL_PASSWORD || 'password';
// const dbHost = process.env.MYSQL_HOST || 'localhost'

const dbUser = process.env.MONGO_USER || 'ecom';
const dbPass = process.env.MONGO_PASSWORD || 'password';
const dbHost = process.env.MONGO_HOST || 'localhost'



let url = `mongodb://${dbUser}:${dbPass}@${dbHost}/shop?retryWrites=true`
let _db;

const mongoConnect = (callback) => {
    console.log(url);
    MongoClient.connect(url)
    .then(client => {
        console.log('Connected!');
        _db = client.db();
        callback();
    })
    .catch(err => {
        console.log(err);
        throw err;
    });
}

const getDb = () => {
    if (_db) {
        return _db;
    }
    throw 'No database found!';
}

exports.mongoConnect = mongoConnect;
exports.getDb = getDb;


// var MongoClient = require('mongodb').MongoClient;

// var url = 'mongodb://localhost/EmployeeDB';

// MongoClient.connect(url, function(err, db) {
// var cursor = db.collection('Employee').find();

//  cursor.each(function(err, doc) {
//         cursor.each(function(err, doc) {
//             console.log(doc);

//     });
// });

