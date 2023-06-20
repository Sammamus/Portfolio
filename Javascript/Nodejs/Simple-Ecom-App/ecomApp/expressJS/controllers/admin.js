const Product = require('../models/product');
const evalBool = require('../util/boolEval');

exports.getAddProduct = (req, res, next) => {
    res.render('admin/edit-product', {
        docTitle: 'Add Product', 
        path: '/admin/add-product',
        editing: false
    });
}

exports.postAddProduct = (req, res, next) => {
    const title = req.body.title;
    const imageUrl = req.body.imageUrl;
    const price = req.body.price;
    const description = req.body.description;
    const product = new Product(title, price, description, imageUrl);

    product
    .save()
    .then(result => {
        console.log('Created Product!');
        res.redirect('/admin/products');
    })
    .catch(err => {
        console.log(err);
    });
}

exports.getEditProduct = (req, res, next) => {
    const editMode = evalBool(req.query.edit);
    if (!editMode) {
        return res.redirect('/');
    }
    const prodId = req.params.productId;
    console.log(req.params);

    Product.fetchById(prodId)
    .then(product => {
        // console.log(product[0].dataValues)
        res.render('admin/edit-product', {
            product: product, 
            docTitle: 'Edit Product', 
            path: '/admin/edit-product',
            editing: editMode
        });
    })
    .catch(err => {
        console.log(err);
    });
}

exports.postEditProduct = (req, res, next) => {
    const prodId = req.body.productId;
    const title = req.body.title;
    const imageUrl = req.body.imageUrl;
    const price = req.body.price;
    const description = req.body.description;

    const product = new Product(title, price, description, imageUrl);

    product
    .update(prodId)
    .then(result => {
        console.log('Item Updated');
        res.redirect("/admin/products");
    })
    .catch(err => {
        console.log(err);
    });
}

exports.getProducts = (req, res, next) => {
    Product
    .fetchAll()
    .then(products => {
        res.render('admin/products', {
            prods: products, 
            docTitle: 'Admin Products', 
            path: '/admin/products'
        });
    })
    .catch(err => {
        console.log(err);
    });
}

exports.postDeleteProduct = (req, res, next) => {
    const prodId = req.body.productId;
    Product.deleteById(prodId) 
    .then(result => {
        console.log("Item Deleted");
        res.redirect('/admin/products');
    })
    .catch(err => {
        console.log(err);
    });
}