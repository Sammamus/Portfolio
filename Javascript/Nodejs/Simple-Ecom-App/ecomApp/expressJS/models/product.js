const mongodb = require('mongodb');
const getDb = require('../util/database').getDb;

class Product {
    constructor(title, price, description, imageUrl) {
        this.title = title;
        this.price = price;
        this.description = description;
        this.imageUrl = imageUrl;
    }

    save() {
        const db = getDb();
        return db.collection('products')
            .insertOne(this)
            .then(result => {
                console.log(result);
            })
            .catch(err => {
                console.log(err);
            });
    }

    update(prodId) {
        const db = getDb();
        return db.collection('products')
            .replaceOne({_id: new mongodb.ObjectId(prodId)}, this)
            .then(result => {
                console.log(result);
            })
            .catch(err => {
                console.log(err);
            })
    }

    static deleteById(prodId) {
        const db = getDb();
        return db.collection('products')
            .deleteOne({_id: new mongodb.ObjectId(prodId)})
            .then(result => {
                console.log(result);
            })
            .catch(err => {
                console.log(err);
            })
    }

    static fetchAll() {
        const db = getDb();
        return db.collection('products')
            .find()
            .toArray()
            .then(products => {
                console.log(products);
                return products;
            })
            .catch(err => {
                console.log(err);
            });
    }

    static fetchById(prodId) {
        const db = getDb();
        return db.collection('products')
            .findOne({_id: new mongodb.ObjectId(prodId)})
            .then(product => {
                console.log(product);
                return product;
            })
            .catch(err => {
                console.log(err);
            })
    }
}


module.exports = Product;