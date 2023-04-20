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

## Mongodb basics data types

* string
* object
* boolean
* number
* array
* null
* date

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

````update```` can take a third(optional) parameter, which is an object  that specify how the update wiil be performed.

That object can contains  ````multi```` as key.

By default, ````multi```` ````false```` and then ony the first matching document is updted.

By setting ````multi```` to ````true````, we can also update all documents matching a condition.

* Checks your result

````mongo
db.student.find(null,{_id:0,good:1})
````

It can also contains ````upsert```` as key.

If ````upsert```` is set to true the document is inserted if the query criteria doesn't match.

* Find  all students named 'Isidore' and insert one if not exists, with good field equals false

````mongo
db.student.update({name:'Isidore'},
{$set:{good:false}},{multi:true,upsert:true})
````

* Check the result

````mongo
db.student.find({name:'Isidore'},{_id:0})
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
db.student.find()
````

### Delete: remove, deleteMany, deleteOne

#### Remove all documents matching a condition

* remove all students of 12  years old:

````mongo
db.student.remove({age:12})
````

or:

````mongo
db.student.deleteMany({age:12})
````

#### Remove the first document matching a condition

* remove the first student of 12  years old:

````mongo
db.student.remove({age:12},true)
````

or:

````mongo
db.student.deleteOne({age:12})
````

#### Remove all documents inside a collection

* remove all documents of student:

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

#### on arrays

##### \$pop

 remove the first or the last value of an array

* remove the first mark value of each student

 ````mongo
db.mark.updateMany({},{$pop:{values:1}})

````

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

* remove the last mark value of students who have 11 as a mark

 ````mongo
db.mark.updateMany({values:11},
{$pop:{values:-1}})

````

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

##### \$push

 add a value at to the back of an array

* add 20 as mark value for the first student

 ````mongo
db.mark.updateOne({},
{$push:{values:20}})
````

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

##### \$addToSet

 similar to \$push but omits and or avoid duplicate values.

* add 20 as mark value for the first student

 ````mongo
db.mark.updateOne({},
{$addToSet:{values:20}})
````

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

##### \$pull

 remove from an array any value equals the one specified.

* remove for each student, if exists, 11s from mark values

 ````mongo
db.mark.updateMany({},
{$pull:{values:11}})
````

There will not be any 11 as mark value now.

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

#### on fields

### \$set

set document value

### \$currentDate

set field value to the current date

* replace the mark values of the first student by the current date

````mongo
db.mark.updateOne({},
//use a boolean
{$currentDate:{values:true}})
````

### \$rename

rename field

* for each student,rename the field values to 'mark_of_students'

 ````mongo
db.mark.updateMany({},
{$rename:{values:'mark_of_students'}})
````

* check the result

````mongo
db.mark.find(null,{_id:false}).pretty()
````

### \$unset

remove field value from document

* for each student,remove the field  'mark_of_students'

 ````mongo
db.mark.updateMany({},
{$unset:{'mark_of_students':true}})
````

* check the result

````mongo
db.mark.find().pretty()
````

### \$inc

increment or decrement(add positive or negative value to) field value

* Let's consider these people

````mongo
db.people.insertMany
([{name:'Roland',good:true},
{name:'François',age:15},
{name:'Jane',good:true},
{name:'Tresoral',age:15},
{name:'Grenade',age:28,}])
````

* Show ages of people

````mongo
db.people.find({},{_id:false,age:true})
````

* add 2 to  the age of each person

````mongo
db.people.update({},
            {$inc:{age:2}},
            {multi:true}
)
````

* Show again ages of people

````mongo
db.people.find({},{_id:false,age:true})
```

* subtract 4 from  the age of each person

````mongo
db.people.update({},
            {$inc:{age:-4}},
            {multi:true}
)
````

* Show again ages of people

````mongo
db.people.find({},{_id:false,age:true})
```


## Query operators

* Create a collection named person

````mongo
db.createCollection('person)
````

* assure the collection is created

````mongo
show collections
````

* insert some objects in that collection

````mongo
db.person.insertMany([
    {name:'Jonh',age:23},
    {name:'Emilie',age:15},
    {name:'Ezéchiel',age:18},
    {name:'Pio'},
    {name:'Mathias',age:15},
    {name:'André',age:13},
    {name:'Saoul'},
    {name:'Perez',age:13},
    {name:'Gildas',age:13},
    {name:'Henry',age:18},
    {name:'Jacob',age:20},
    {name:'Octave',age:20}
])
````

* check insertion

````mongo
db.person.find().pretty()
````

### Comparison operators

#### \$eq

equal

* Get people of 13 years old

````mongo
db.person.find({age:13})
````

* Do the same using \$eq

````mongo
db.person.find({age:{$eq:13}})
````

* find  the name of all people whose age is not specified(null)

````mongodb
db.person.find({age:{$eq:null}},{_id:0,name:1})
````

#### \$ne

not equal

* find name of people whose age is not 13

````mongo
db.person.find({age:{$ne:13}},{_id:0,name:1})
````

#### \$gt

greater than

* find name of people whose age is above 13

````mongo
db.person.find({age:{$gt:13}},{_id:0,name:1})
````

#### \$gte

greater than or equal

* find name and age of people  are major

````mongo
db.person.find({age:{$gte:18}},{_id:0})
````

#### \$lt

less than

* find name and age of people who are minor

````mongo
db.person.find({age:{$lt:18}},{_id:0})
````

#### \$lte

less than or equal

* find name of people whose age is 15 or less

````mongo
db.person.find({age:{$lte:15}},{_id:0,name:1})
````

#### \$in

in

* find name and age of people whose age is 15, 18 or 20

````mongo
db.person.find({age:{$in:[15,18,20]}},{_id:0})
````

### Logical operators

#### \$not

Allows to get alll documents where a condition is not verified

* get all people whose age is not 20

````mongo
db.person.find({ age: { $not: { $eq: 20 } } })
````

* find  people whose

````mongo
db.person.find({name:{$not:{}}})
````

#### \$and

* find the  first person whose name is 'Gildas' and age is 13

````mongodb
db.person.findOne({
    $and:[
        {name:'Gildas'},
        {age:13}
        ]
        })
````

* find  the name and age of people whose age is in the range [12;18] and not equal to 15

````mogo
db.person.find({
    $and:[
        {age:{$gte:12}},
        {age:{$lte:18}},
        {age:{$ne:15}}
        ]
        },
        {_id:false})
````

#### \$or

* find all people whose name is 'Gildas' or age is either 13 or  null.

````mongodb
db.person.find({
    $or:[
        {name:'Gildas'},
        {age:13},
        {age:null}
        ]
        })
````

#### \$nor

* find name of  all people whose name is neither 'Gildas' nor 'Ezéchiel', nore 'André'.

````mongodb
db.person.find({
    $nor:[
        {name:'Gildas'},
        {name:'Ezéchiel'},
        {name:'André'}
        ]
        },
        {_id:0,name:1})
````

* find name and age of  all people whose name is neither 'Gildas', nor 'André' and whose age is not 18

````mongodb
db.person.find({
    $nor:[
        {name:'Gildas'},
        {name:'André'},
        {age:18}
        ]
        },
        {_id:0})
````

### Evaluation operators

#### \$regex

* get people whose name contains a

````mongo
db.person.find({name:{$regex:'a'}})
````

* get people whose name  starts with 'M'

````mongo
db.person.find({name:{$regex:'.{0}M'}})
````

* get people whose name  ends with 's'

````mongo
db.person.find({name:{$regex:'s.{0}'}})
````

### \$exists

Allows to get documents where a field exist or not

* get people whose age is not specified

````mongo
db.person.find({age:{$exists:false}})
````

* get people whose age is specified

````mongo
db.person.find({age:{$exists:true}})
````

#### \$text

#### \$where

\$where is used to pass a js expression as a query

* find all documents where the sum of age and the length of name is greater than or equaal to 25

````mongo
db.person.find({ $where: function() { return (this.age + this.name.length) >=25;} })
````

++++++++++++++

* get people whose name  ends with 's'

````mongo
db.person.find({$where:{age:15}})
````

+++++++++++++++

## limit,skip,sort,count

* limit  the results to the first three(3) documents.

````mongo
db.find().limit(3)
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

Let's consider the following collection

````mongo
db.marks.insertMany([
    {name:'Andre', mark:15, subject:'math'},
    {name:'Peter', mark:18, subject:'english'},
    {name:'Saoul', mark:12, subject:'french'},
    {name:'Peter', mark:09, subject:'french'},
    {name:'Saoul', mark:15, subject:'french'},
    {name:'Andre', mark:15, subject:'math'},
    {name:'Peter', mark:18, subject:'math'},
    {name:'Saoul', mark:11, subject:'english'},
    {name:'Andre', mark:8, subject:'english'}
    ])
````

* show student marks documents excluding the primary key field

````mongo
db.marks.find({},{_id:false}).pretty()
````

Aggregate operations are used with the ````aggregate```` function.

aggregate without parameter is as same as find without parameter.

````mongo
db.marks.aggregate()
````

* get the group of subject

````mongo
db.marks.aggregate({
    $group:{
        _id:'$subject'
        }
})
````

db.marks.aggregate({
    $group:{
        _id:'$subject',
        }
})

* group of the mark obtained

````mongo
db.marks.aggregate({
    $group:{
        _id:'$mark'
        }
})
````

* group of the students

````mongo
db.marks.aggregate({
    $project:{
        _id:0,
        'Subjects of assessment':'$subject',
        }
})
````

* get the  5 first documents

````mongo
db.marks.aggregate({
    $limit:5
})
````

* select from the third document

````mongo
db.marks.aggregate({
    $skip:2
})
````

* ASC sort documents on name field

````mongo
db.marks.aggregate({
    $sort:{name:1}
})
````

* DESC sort document on mark field

````mongo
db.marks.aggregate({
    $sort:{mark:-1}
})
````

* DESC sort documents on mark field, ASC sort on name field

````mongo
db.marks.aggregate({
    $sort:{mark:-1,name:1}
})
````

* Get randomly 3 documents from the collection of marks

````mongo
db.marks.aggregate({
    $sample:{size:3}
})
````

* find documents where mark=15

````mongo
db.marks.aggregate({
    $match:{mark:15}
})
````

* Add the field 'field_name' to the mark collection and set all values of doc to 899

````mongo
db.marks.aggregate({
    $addFields:{field_name:899}
})
````

* add more than one field

````mongo
db.marks.aggregate({
    $addFields:{field_name:true,second:'test'}
})
````

We can embed(nest) aggregate operators.

* Count the number of documents for each subject

````mongo
db.marks.aggregate({
    $group:{
        _id:'$subject',
        nb_marks:{$sum:1} //add 1 for each
        }
})
````

* get the mark totalised by each student

````mongo
db.marks.aggregate({
    $group:{
        _id:'$subject',
        'mark tot:':{$sum:'$mark'}
        }
})
````

* get the average of the marks of  each student

````mongo
db.marks.aggregate({
    $group:{
        _id:'$name',
        'definitive mark':{$avg:'$mark'}
        }
})
````

* get the minimum and the maximum mark and the decisive mark  obtained by each student

````mongo
db.marks.aggregate({
    $group:{
        _id:'$name',
        'min mark':{$min:'$mark'},
        'max mark':{$max:'$mark'},
        final:{$avg:'$mark'}
        }
})
````

* group students mark by name and get the first document for each group

````mongo
db.marks.aggregate({
    $group:{
        _id:'$subject',
        xx:{$first:'$name'}
        }
})
````

* group students mark by name and get the last document for each group, onlythe name field and the _id one are considered

````mongo
db.marks.aggregate({
    $group:{
        _id:'$subject',
        result:{$last:'$name'}
        }
})
````

We can  also use more than one aggregate operator in the function aggregate. In that case we should specify as parameter to ````aggregate````, the array containing the list of the concerned aggregate operators.

* get the list of the max marks of students(without their name)

````mongo
db.marks.aggregate([
    {$group:{
        _id:'$name',
        'max mark':{$max:'$mark'}
        }},
    {$project:{
            _id:0//exclude _id,
            //,'max mark':0 exclude
        }}
])
````

* show the name and the adverage of the more brilliant student

````mongo
db.marks.aggregate([
    {$group:{
        _id:'$name',
         'avg':{$avg:'$mark'}
        }},
        //sort in DESC of avg
    {$sort:{'avg':-1}},
    //get the first document
    {$limit:1}
])
````

* show the documents and add a field specifing either the student

++++++++++++++++++++++++++++

````mongo
db.marks.aggregate([
    {$project:{
        _id:false,
        mark:'$mark'

    }},
        //add the validation field
    {$addFields:{
        'validate':
        {mark:{'$gte':12}}
        //{'$gte':{'mark':12}}
        }}
])
````

+++++++++++++++++++++++++++++

## Driver

Drivers allow us touse programming language to interact with databases.

There are MOngo  drivers for many programming languages such as C, C++, java, Python, etc.

### Python driver

The python mongodb driver is called pymongo.

#### Installlation

pip install pymongo

#### Usage

## Save document

We can alse use the method ````save```` to insert a document in a collection. The difference with insert is that during document with save by specifing a primary key(_id for example) that already exists, the document is updated.

The usage is as same as insert.

## Schema validation

Mongo database collections are used in flexibe way. By default, contrayry to relational databases, there is no requirement in structure for the different documents. The documents we insert may not hava the same structure.

We can insert for example:

````mongo
{name:'Henry',age:25}
````

and

````mongo
{mark:15,good:true}
````

as documents in the same collection.

That can be avoide. We can pre-define the sructure, the schama of our database in mongodb by using the operator ````$jsonSchema````: that is called ````schema validation````.

That operator is using during the creation of the concerned colllection(with the method ````createCollection````)

In fact, the method ````createCollection```` can take a part from the name of the collection to create, which a string,  a second optional parameter which is an object that contains the characteristics of the collection such as the fields with their data type, the eventual required field(s), etc.

### Example

````mongodb
db.createCollection("posts", {
    validator: {
      $jsonSchema: {
        //the data type of a document
        bsonType: "object",
        required: [ "title", "body" ],
        properties:{
            //list the fields of the collection
          title: {
            bsonType: "string",
            description: "Title of post - Required."
          },
          body: {
            bsonType: "string",
            description: "Body of post - Required."
          },
          category: {
            bsonType: "string",
            description: "Category of post - Optional."
          },
          likes: {
            bsonType: "int",
            description: "Post like count. Must be an integer - Optional."
          },
          tags: {
            bsonType: ["string"],
            description: "Must be an array of strings - Optional."
          },
          date: {
            bsonType: "date",
            description: "Must be a date - Optional."
          }
        }
      }
    }
  })
````

* Show these properties using:

````mongo
db.posts.exists()
````

* Insert documents inside that collection

````mongo
db.posts.insert({title:'title of my post',body:'body of my post'})
````

There, all the fields required by the collection(title and body) are provided and in the document and their data type (string) is valid. So the insertion will be successfull.

 We get an error while inserting a document that doesn't obey the validation schema.

### Example-validation failure: required fields missing

* Run:

````mongo
db.posts.insert({wrong:'fff'})
````

* Run this to assure the document is not inserted

````mongodb
db.posts.find()
````

In that example, validation will fail simply because, for examples:

* title and body fields are required but they are not specified in the docuemnt
* the field named ````wrong```` provided doesn't belong to the list of fields to provide.

Other error such as wrong field type will lead insertion to fail too.

### Example-validation failure: wrong field type provided

* Run

````mongo
db.posts.insert({title:2,body:'body of my post'})
````

In that example, title should be a string but an integer is provided instead.

## Run js file

We can run a java script(js) file that contain mongodb script using either the bash terminal or the the mongodb shell.

### Via mongodb shell

We use the function ````load```` by specifing the path of the js file to run(as a string).

````mongo
load('path/to/js/file.js')
````

### Via bash terminal

````bash
mongo localhost:27017/mydb path/to/my/jsfile.js
````

 This operation executes the 'path/to/my/jsfile.js' script in a mongo shell that connects to the mydb database on the mongod instance accessible via the localhost interface on port 27017. localhost:27017 is not mandatory as this
is the default port mongodb uses.

## Backup and restore data

### Backing up

#### Basic mongodump of local default mongod instance

````bash
mongodump --db mydb --gzip --out folder/path
````

This command will dump a bson gzipped archive of your local mongod 'mydb' database to the
'folder/path' directory

#### Basic mongorestore of local default mongodump

````bash
mongorestore --db mydb dump_dir --drop --gzip
````

This command will first drop your current 'mydb' database and then restore your gzipped bson dump from the 'dump_dir' archive dump file.

#### Import file to mongodb

##### mongoimport with JSON

````bash
mongoimport --db test --collection "coll_name" --drop --type json --host
"localhost:47019" --file "path/to/json/file.json"
````

* --db : name of the database where data is to be imported to
* --collection: name of the collection in the database where data is to be improted
* --drop : drops the collection first before importing
* --type : document type which needs to be imported. default JSON
* --host : mongodb host and port on which data is to be imported.
* --file : path where the json file is

##### mongoimport with csv

Relace the file type in the bash command above by csv.

++++++++++++++++++++++++++++++++++++++++++++++++

$search $caseSensitive $$diacriticSensitive $text,  $unwind

partial indexes , indexes creation

collections joining

python driver, C++ driver
