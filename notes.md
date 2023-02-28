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
