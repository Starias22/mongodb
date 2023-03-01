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

simple show

````mongo
show dbs
````

````mongo
db.getMongo().getDBNames()
````

That method returns an array that contains all the databases.

````mongo
db.adminCommand('listDatabases')
````

That command return anobject containing all the available databases with more accurate details, concerning the size occupied.

### Create or Switch to another database

````mongo
use my_new_database
````

The database ````my_new_database```` is created in case of non-existance.

## Show collections

````mongo
show collections
````

or

````mongo
show tables
````

or

````mongo
db.getCollectionNames()
````

The last method returns an array that contains all collections.

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

## CRUD basics operations

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

or

````mongo
db.student.updateOne({name:'Jane'},{$set:{new1:'xxx',new2:true,name:'JaneX'}})
````

By default, ````update```` updates the first document matching the specified query criteria.

* Verify the result

````mongo
db.student.findOne({name:'JaneX'},{_id:false})
````

* set the  good field of all students to false

````mongo
db.student.updateMany({},{$set:{good:false}})
````

or

````mongo
db.student.update({},{$set:{good:false},{multi:true}})
````

````update```` can take a third(optional) parameter, which is an object with ````multi```` as key.

By default, ````multi```` ````false```` and then ony the first matching document is updted.

By setting ````multi```` to ````true````, we can also update all documents matching a condition.

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
db.student.remove({})
````

or:

````mongo
db.student.remove(null)
````

### Query criteria array using positional operator

* create a collection named mark

````mongo
db.createCollection('mark')
````

* assure the collection is created

````mongo
show collections
````

* add new mark values to the collection

````mongo
db.mark.insertOne({values:[15,20,13,14]})
db.mark.insertMany([
    {values:[2,13,7,12]},
    {values:[12,11,6,11]},
    {values:[2,11,13,12]},
    {values:[5,1,11,1]}
    ])
````

* show the mark values inserted in the collection

````mongo
db.mark.find(null,{_id:false})
````

* pretty show  the mark values that contain 12

````mongo
db.mark.find({values:12},{_id:false}).pretty()
````

* Let's set all mark values equal to 11, to 12

````mongo
db.mark.updateMany({values:11},{$set:{'values.$':12}})
````

* check the result: there could not be any 11 in the mark collection now

````mongo
db.mark.find(null,{_id:false}).pretty()

````

### More update operators

\$push: add a value to an array

\$pull: remove a value from an array

\$pop: remove the first or the last value of an array

## Query operators: not,and,or

* Create a collection named person

````mongo
db.createCollection('person)
````

* check the connection is created

````mongo
show collections
````

* insert some objects in that collection

````mongo
db.person.insertMany([
    {name:'Jonh',age:23},
    {name:'Emilie',age:15},
    {name:'Pio'},
    {name:'André',age:13},
    {name:'Saoul'},
    {name:'André',age:13},
    {name:'Gildas',age:13}
])
````

* check insertion

````mongo
db.person.find().pretty()
````

### \$not

* find  the name of all people whose age is not 13

````mongodb
db.person.find({age:{$not:13}},{_id:0,name:1})
````

* find  the name of all people whose age is not  null(is  specified)

````mongodb
db.person.find({age:{$not:null}},{_id:0,name:1})
````

### \$and

* find the  first person whose name is 'Gildas' and age is 13

````mongodb
db.person.findOne({
    $and:[
        {name:'Gildas'},
        {age:13}
        ]
        })
````

### \$or

* find all people whose name is 'Gildas' or age is 13 or age is null.

````mongodb
db.person.find({
    $or:[
        {name:'Gildas'},
        {age:13},
        {age:null}
        ]
        })
````

### \$in

That operator works as same as the \$or and \$and operators.

### Comparaison operators: \$gte, \$lte, \$gt, \$lt

The four folllowing operator are used as same as the $not operator.

#### \$gte

greater than or equal

#### \$lte

less than or equal

#### \$gt

greater than

#### \$lt

less than

## limit,skip,sort,count

* limit first three(3) documents of person

````mongo
db.find().limit()
````

* list all ages in ASC order

````mongo
db.find(null,{_id:false,age:true}).sort({age:1})
````

* list all names in DESC order

````mongo
db.find(null,{_id:false,name:true}).sort({name:-11})
````

* count all documents of persons

````mongo
db.find().count()
````

* list from the third document to end

````mongo
db.find().skip(3)
````

## Insert document

For each document inserted an _id is generated.
An id is an hexadecimal object with 12 byes:

* the 4 first: the timestamp is seconds
* the next 3: the machine id(identifier)
* the next 2: the process id
* the last 3: the number of the _id
An id is a primary key, that assure the uniqueness for each document.

We can either specify or not the \_id during insertion, as long as the _id is unique.

## Indexes: createIndex, dropIndex, getIndexes, unique, sparse, partial

Indexes are constraints we make to a filed of collections in a database.

* Let us have a set of books inside a book collection.

````mongo
db.createCollection('book')
db.book.insertMany([
    {bname:'Les tresseurs de corde',author:'Jean Pliya'},
    {bname:'Le gong a bagaiyé',author:'Appolinaire AGBAZAHOU'},
    {bname:'La secrétaire particulière',author:'Jean Pliya'},
    {bname:'Un piège sans fin',author:'Ousmane Sembène'},
    {bname:'Une si longue lettre',author:'Mariama Ba'},
    {bname:'Sous l\'orage',author:'Seydou Badian'}

])
````

* Now  pretty show all books in the collection

````mongo
db.book.find().pretty()
````

* show all indexe(s) in the collection

````mongo
db.book.getIndexes()
````

That mehod returns an array containing all indexes in the book collection, with their details.

Actually, there is only one indexe created.

In fact, mongodb, by default creates  unique indexe on the _id field(the primary key), that prevent having two or many documents with the same \_id.

* Let us create an indexe on the bname field of our book collection

````mongo
db.book.createIndexes({my_index:1})
````

We've specified in an object the field concerned as key, and it's value as the value of the object.

The concerned indexe will be created if not exist

Typically, we use 1 or -1 for value of index; 1 for ASC indexes and -1 for DESC indexes.

````mongo
db.collocetion.createIndex({field:1})
````

* Now print the list of indexes again

````mongo
db.book.getIndexes()
````

Now we have two indexes created.

* Note that there is the name of the each indexe among the details on indexes.

By default, mongodb names, for example, ind_1 an indexe on a field ind with the value 1.

We can provide the name of our index as another argument to the createCollection method.

* Create an indexe named 'index on author name' on the author field, whith the value 1

````mongo
db.book.createIndexe({author:1},{name:'index on author name'})
````

* List indexes to check the result

````mongo
db.book.getIndexes()
````

We use  the dropIndex method to drop an indexe.

We can specifier either the name of the indexe to drop or the concerned field with the value of the indexe for example when we don't know the name of the index.

* drop the index we just created on the author field:

````mongo
db.book.dropIndex('index on author name')
````

* drop the index we created on the bname field above

````mongo
db.book.dropIndex({bname:1})
````

createIndex can take another (optional) parameter, which is an oject that specify whitch kind of indexe will be created.

* Let's create an unique index on the bname field.

````mongo
db.book.createIndex({bname:1},{name:'book name is unique'},{unique:true})
````

* Show the available indexes for checking

````mongo
db.book.getIndexes()
````

Now we cannot have two documents with the same book name, because unique index is set on bname field:

* Try to insert a document named 'Les tresseurs de corde' and you'll get an issue.

````mongo
db.book.insertOne(b,ame:'Les tresseurs de corde',author:'another')
````

* show all the books in the collection

````mongo
db.book.find().pretty()
````

* insert the following documents into the collection an you'll get an error

````mongo
db.book.insertOne({author:'Victor Hugo'})
db.book.insertOne({
    author:'Jean de la Fontaine',
    bname:'Le laboureur et ses enfants'
    })
db.book.insertOne({author:'Daté Akayi Barnabé'})

````

In fact, when we don't specified a value for a field during insertion of a document, it's set to null. In the example above we've inserted two documents without bname, so both their bname will be set to null,  and that violates the unique key set on the bname field.

To solve that issue, and so allow having two or more documents without bname specified, we can use sparse indexe.

* First of all drop the index we created above, on the bname field.

````mongo
db.book.dropIndex({bname:1})
````

* Now recreate the indexe by setting it unique and sparse indexex

````mongo
db.book.createIndex({bname:1},{unique:true,sparse:true})
````

* Show indexes list to check

````mongo
db.book.getIndexes()
````

We can drop all non _id indexes by usind dropIndexes

* Drop all indexes in the book collection:

````mongo
db.book.dropIndexes()
````

### Partial indexes

Partial indexes is the generalisation of sparse indexes.

We can use that to determine the indexe entries based on the specified filter.

* Create a DESC index on name field of student collection if the age of student is less than 18

````mongo
db.student.createIndex(
    {name:-1},
    {partialFilterExpression:{age: {$lt:15}})
````

### Compound

We can create indexes on multiple fields

* Create an index on bname and author fields, ASC in bname and DESC in author.

````mongo
db.book.createIndex({bname:1,author:-1})
````

Will be  ASC sorted first by bname and then DESC sort by author.

## Collection

### Create collection

createCollection accepts a second(optional) parameter

````mongo
db.createCollection("newCollection", {capped :true, autoIndexId : true, size : 6142800, max :
10000})
````

A collection can also be created during document insertion or index creation if the concerned collection doesn't exist.

````mongo
db.collection.insert(obj)
````

or

````mongo
db.collection.createIndex({ind_name:8})
````

will create the collection if it doesn't exist.

### Drop a collection: drop

````mongo
db.collection.drop()
````

That methodes return true is the drop is success and false otherwise.

## Aggregation

Aggregation operators are operators that can be applied to fields of collection.

Mongodb provides aggregations to compute the sum, to get the count, the min and max, the average,  and perform much more operations on fields of collection.

Let's consider that collection

````mongo
db.mark.insertMany([
    {name:''}
])
````

## Driver

## Schema validation

## Backup and restore data

## Run js file
