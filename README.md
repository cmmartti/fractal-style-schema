# Fractal-Style GraphQL Schema Example (Graphene-Python)

This is an example of a fractal style GraphQL schema for Graphene-Python, where each entity has its own module. Within each module are the files `mutation`, `type`, `query`, and `subscription` that contain all of the types, queries and mutations (root), etc. for that entity. This avoids the issue of overly-long schema files that contain dozens or hundreds of types and resolvers.

This specific example is a simple read-only query API for video games and characters.

Based on code examples by [ahopkins](https://github.com/graphql-python/graphene/issues/545#issuecomment-329630141) (Adam Hopkins) and [ProjectCheshire](https://github.com/graphql-python/graphene/issues/714#issuecomment-391211693) (Jessamyn Hodge).
