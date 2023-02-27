# Mongodb notes

## Open a mongodb shell

````bash
mongo
````

## Basics mongodb shell commands

### Version

````mongo
db.version()
````

### Check the current database

````mongo
db
````

### Show all available databases

````mongo
show dbs
````

### Create or Switch to another database

````mongo
use my_new_database
````

The database ````my_new_database```` is created in case of non-existance.

## Show collections

````mongo
show collections
````

It shows all available collections in the selected(current) database.

### Help

Use the command below to show all available methods ont the database ````mydb````

````mongo
db.mydb.help()
````

Use the folllowing one to show all general config methods available

````mongo
db.help()
````

## Drop database

Drop the selected database with:

````mongo
db.dropDatabase()
````

## CRUD operations

### Create a collection

````mongo
db.createCollection('my_collection')
````

show the  available collections using:

````mongo
show collections
````

### Create document

#### Insert

 create an object obj

````mongo
obj={name;'James', age:15}
````

 Insert the created object obj to the collection student

````mongo
db.student.insert(obj)
````

#### At once

````mongo
db.student.insert({name:'Landry'})
````

#### Insert one

````mongo
db.student.insertOne({name:'Landry',good:true})
````

#### Insert many

````mongo
db.student.insertMany([{name:'Roland',good:true},{name:'François',good:false},{name:'Jane',good:true},{name:'Tresoral',good:false},{name:'Grenade',age:28,good:true}])
````

### Read: find, findOne

We use ````find```` to find all matching records and ````findOne```` to find the first matching record.

With ````null````, or ````{}```` as argument, or without argument(default), all records are found.

* Find all records(documents) in the collection student

````mongo
db.student.find()
````

* Find the first student document

````mongo
db.student.find()
````

#### Basic selection

Selection consists to find, to retrieve records that verify some condition(s), to filter records.

* Find all students whose good field is false

````mongo
db.student.find({good:false})
````

* Find the first student named 'Jérémie'

````mongo
db.student.findOne({name:'Jérémie'})
````

* Find all the students who are 20 years old:

````mongo
db.student.find({age:20})
````

* Find all  the records where student name is not specified

````mongo
db.student.find({name:null})
````

#### Projection

Projection consist in specifing the field(s) to include in the records result.

By default, all the fiels are included in the records result, and one field more, named ````_id```` which represents the primary key of the collection.

* Find all records(documents) in the collection student, all fields included

````mongo
db.student.find()
````

Both ````find```` and ````findOne```` can take a second(optional) parameter, which is an object that represents the field(s) to include in or  to exclude out from the result: Use 1 or true to include a field and 0 or false to exclude it.

The primary key is always added if not present in the second parameter of find or findOne. Set it to false(or 0) to exclude it from the result.

* Find all students whose good field is set to false,  and exclude the primary key from the result

````mongo
db.student.find({good:false},{_id:false})
````

* Find all students record and exclude the primary key field and the age one.

````mongo
db.student.find({},{_id:false,age:false})
````

or

````mongo
db.student.find(null,{_id:false})
````

* Find (only) the name of the first student who is 20 years old

````mongo
db.student.find({age:28},{_id:false,name:true})
````

* Find the primary key of the first student

````mongo
db.student.findOne({},{_id:true})
````

#### Pretty print

The function pretty can be used with both find and finOne to pretty print the records(in JSON format).

* Pretty prints the records of all students

````mongo
db.student.find().pretty()
````

### Update: update, updateOne, updateMany, replaceOne

#### update, updateOne, updateMany

Both update, updateOne, and updateMany can be used to update documents; they require two(2) parameters  where the first one is the object that represents the condition of update, the query criteria.

* ````update```` and  ````updateMany```` update all the records matching the specified query(condition)
* ````updateOne```` updates the  first record record matching the specified query(condition).

The second parameter specified is an object that must contain as key, an atomic operator and as value the new record.

#### Atomic operators

An atomic operator specify how the record(s) will be updated.

Atomic operators are often preceeded by '$' symbol.

There are many atomic operators such as:$set,$push,$pull.

The value of the atomic operator, which represents the new record to apply for each record matching the query,can contain new fields.

For example, by using $set as atomic operator, all the fields absent in the new record specified are conserved in the matching records, the rest are added if not exist and updated if exist.

* Check the good field of the first student named 'James'

````mongo
db.student.findOne({name:'Jane'},{_id:0,good:1})
````

* Set here the record obj={new1:'xxx',new2:true,name:'JaneX'}

````mongo
db.student.updateOne({name:'Jane'},{$set:{new1:'xxx',new2:true,name:'JaneX'}})
````

* Verify the result

````mongo
db.student.findOne({name:'JaneX'},{_id:false})
````

* set the  good field of all students to false

````mongo
db.student.updateMany({},{$set:{good:false}})
````

* Checks your result

````mongo
db.student.find(null,{_id:0,good:1})
````

#### replaceOne

 replaceOne takes two parameter, the first one is the query criteria, and the second is the new record to apply for  the first matching record.

The old record is totally replaced in that case, by the new specified.

* Replace the entry of the first student by {only:true}

````mongo
 db.student.replaceOne({},{only:true})
 ````

* check the result

````mongo
db.student.find({only:true},{_id:false,only:true})
````

### Delete: remove, deleteMany, deleteOne

#### Remove all documents matching a condition

To remove all students of 12  years old, use:

````mongo
db.student.remove({age:12})
````

or:

````mongo
db.student.deleteMany({age:12})
````

#### Remove the first document matching a condition

To remove the first student of 12  years old, use:

````mongo
db.student.remove({age:12},true)
````

or:

````mongo
db.student.deleteOne({age:12})
````

#### Remove all documents inside a collection

To remove all documents of student, use:

````mongo
db.student.remove()
````

or:

````mongo
db.student.remove({})
````

or:

````mongo
db.student.remove(null)
````

