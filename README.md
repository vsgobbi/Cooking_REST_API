# Example of Cooking API using Nested Serializers

Note: When accessing API routers inside browser panel, if you try opening the form to add information, you will see a message as: **Lists are not currently supported in HTML input**,
this is normal normal because Django Rest does not support forms for many to many nested serializers, you should use raw data our 'curl' or 'httpie' instead.

### Installation
1. Create your own environment (virtualenv)
``` shell
        virtualenv -p python3.6 venv
        source venv/bin/activate
```
1.1 Check your python version and pip requirements:
``` shell
        python --version #should be 3.6 or greater
        pip install -r requirements.txt
```
2.0 Create db, make migrations and run the server:
``` shell

        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver
```
2.1 Check your API-Root at localhost:8000

### Creating Raw data
``` json
{
    "ingredients": [],
    "name": "",
    "description": "",
    "directions": ""
}
```

Adding existing ingredients, and recipe.
``` json
{
    "ingredients": [
      {"name":"pepper"},
      {"name":"salt"},
      {"name":"cheese"}
    ],
    "name": "Sandwich",
    "description": "",
    "directions": "Put all ingredients together in a nice toasted bread"
}
```

Adding existing ingredients to a new recipe
``` json
{
    "ingredients": [
      {"id": 1, "name":"pepper"},
      {"id": 2, "name":"salt"},
      {"id": 2, "name":"salami"}
    ],
    "name": "Salami Sandwich",
    "description": " ",
    "directions": " "
}
```

Adding exist ingredients and recipe and its cooker
``` json
{
    "name" : "John",
    "age" : 25,
    "recipes" : [
	{'name' : "Sandwich"}
	]
}
```


Direct assignment adding non existing ingredients and recipes for its cooker
The nested serializer lib for this API will handle the create and update methods to it's nested fields.
``` json
{
    "name" : "Erick Jacao",
    "age" : 54,
    "recipes" : [
    {
    "name" : "Sandwich",    
    "ingredients": [
      {"name":"pepper"},
      {"name":"salt"},
      {"name":"cheddar"},
      {"name":"oregano"},
      {"name":"bread"}
    ],
    "description": "How to make a nice sandwich",
    "directions": "Put all together and its done"
     }
  ]
}


{
     "age": 28,
     "name": "Vitao",
     "recipes": [
            {
                "id": 1,
                "name": "Protein Porridge",
                "description": "How to make a tasty protein porridge after gym workout",
                "directions": "Take everything to a bowl, mix it and heat, done!",
                "ingredients": [
                    {
                        "id": 4,
                        "name": "Powdered Milk"
                    },
                    {
                        "id": 5,
                        "name": "Water"
                    },
                    {
                        "id": 6,
                        "name": "Cocoa"
                    },
                    {
                        "id": 7,
                        "name": "Oats"
                    }

                ]
            }
        ]
    }
```

> Scripts:

    rmdb.sh is a short extension to clear your database before migrating again
    runserver.sh will make completed migrations and start server quickly

### GPL v.0.3
### Django RESTFUL API free to use under GPL license, created by vitorsgobbi@hotmail.com
