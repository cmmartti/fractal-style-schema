# Fractal-Style GraphQL Schema

This is an example of a fractal style GraphQL schema for [Graphene-Python](http://graphene-python.org/), where each entity is in its own module. Within each module are `mutation`, `type`, `query`, `subscription`, `resolvers` etc. files that contain all of the types, queries, mutations, etc. for that entity. This organisation method avoids the issue of overly-long schema files that contain dozens or hundreds of types and resolvers.

This specific example is a simple read-only query API for video games and characters.

The `graphql_api.auto.schema_operations_builder` function assembles each part into a whole Query/Mutation, which can then be passed to `graphene.Schema` to create a schema.

Circular dependencies are met using Graphene's [`lazy_import`](https://github.com/graphql-python/graphene/blob/master/graphene/utils/module_loading.py) utility function.

This GraphQL API is built on Django. To run it, first create a virtual environment:

Python2: `virtualenv venv`

Python3: `python venv venv`

Then install dependencies:

`pip install -r requirements.txt`

Then start the dev server:

`python manage.py runserver`

Open your browser to localhost:8000/graphql to view the GraphiQL IDE.

---

Based on code examples by [ahopkins](https://github.com/graphql-python/graphene/issues/545#issuecomment-329630141) (Adam Hopkins) and [ProjectCheshire](https://github.com/graphql-python/graphene/issues/714#issuecomment-391211693) (Jessamyn Hodge).
