# Fractal-Style GraphQL Schema

This is an example of a fractal style GraphQL schema for Graphene-Python, where each entity is in its own module. Within each module are `mutation`, `type`, `query`, `subscription`, etc. files that contain all of the types, queries, mutations, etc. for that entity. This organisation method avoids the issue of overly-long schema files that contain dozens or hundreds of types and resolvers.

The `graphql_api.auto.schema_operations_builder` function assembles each part into a whole Query/Mutation, which can then be passed to `graphene.Schema` to create a schema.

This specific example is a simple read-only query API for video games and characters.

Based on code examples by [ahopkins](https://github.com/graphql-python/graphene/issues/545#issuecomment-329630141) (Adam Hopkins) and [ProjectCheshire](https://github.com/graphql-python/graphene/issues/714#issuecomment-391211693) (Jessamyn Hodge).
