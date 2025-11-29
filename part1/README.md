Here is the part 1 of the HBnB project
Hope you find it beneficial

1. Introduction

This technical document describes the architecture and design of the HBnB Evolution application.
Its purpose is to provide a clear blueprint for the system before implementation.

The document includes:

High-level system architecture

Business Logic class structure

Sequence diagrams showing API interactions

Short explanations supporting the diagrams

This documentation will be used as a reference during development and ensures that the structure of the application is well understood before coding begins.

2. High-Level Architecture
2.1 Overview

The application follows a three-layer architecture:

Presentation Layer: Handles incoming requests (API, service functions)

Business Logic Layer: Contains models and core logic

Persistence Layer: Repositories for database interaction

Communication across layers is simplified using a Facade, which acts as a unified interface for the Business Logic.

2.2 High-Level Package Diagram
flowchart TB

subgraph Presentation ["Presentation Layer"]
    API["API"]
    Service["Service"]
end

subgraph Business ["Business Logic Layer"]
    Facade["Facade"]
    User["User"]
    Place["Place"]
    Review["Review"]
    Amenity["Amenity"]
end

subgraph Persistence ["Persistence Layer"]
    RepoUser["UserRepo"]
    RepoPlace["PlaceRepo"]
    RepoReview["ReviewRepo"]
    RepoAmenity["AmenityRepo"]
    DB["Database"]
end

API --> Facade
Service --> Facade

Facade --> User
Facade --> Place
Facade --> Review
Facade --> Amenity

User --> RepoUser
Place --> RepoPlace
Review --> RepoReview
Amenity --> RepoAmenity

RepoUser --> DB
RepoPlace --> DB
RepoReview --> DB
RepoAmenity --> DB

2.3 Explanation

The Presentation Layer communicates only with the Facade.

The Facade contains logic to coordinate operations between entities.

Repositories in the Persistence Layer handle the actual database work.

Layers do not interact directly except through their defined interfaces.

3. Business Logic Layer
3.1 Class Diagram
classDiagram

class User {
    id
    first_name
    last_name
    email
    password
    is_admin
}

class Place {
    id
    title
    description
    price
    latitude
    longitude
}

class Review {
    id
    rating
    comment
}

class Amenity {
    id
    name
    description
}

User "1" --> "many" Place
User "1" --> "many" Review
Place "1" --> "many" Review
Place "many" --> "many" Amenity

3.2 Explanation

Users own multiple Places and can write multiple Reviews.

Places have many Reviews and can contain multiple Amenities.

All objects have an ID and timestamps (created_at, updated_at).

Relationships reflect the core business requirements of the HBnB system.

4. API Interaction Flow

Below are simple sequence diagrams showing how the layers interact during key operations.

4.1 User Registration
sequenceDiagram
User ->> API: send registration data
API ->> Facade: validate & request createUser
Facade ->> User: create new user object
User ->> UserRepo: save to DB
UserRepo -->> Facade: success
Facade -->> API: result
API -->> User: response

4.2 Place Creation
sequenceDiagram
User ->> API: create place request
API ->> Facade: createPlace(data)
Facade ->> Place: build place object
Place ->> PlaceRepo: insert into DB
PlaceRepo -->> Facade: ok
Facade -->> API: place created
API -->> User: response

4.3 Review Submission
sequenceDiagram
User ->> API: submit review
API ->> Facade: addReview(data)
Facade ->> Review: new review
Review ->> ReviewRepo: save review
ReviewRepo -->> Facade: stored
Facade -->> API: done
API -->> User: response

4.4 Fetch List of Places
sequenceDiagram
User ->> API: request places
API ->> Facade: getPlaces()
Facade ->> PlaceRepo: fetch all
PlaceRepo -->> Facade: list
Facade -->> API: return list
API -->> User: data

5. Conclusion

This technical documentation summarizes the architecture, components, and interaction flows of the HBnB Evolution application.
It provides a structured foundation for the upcoming implementation phase and ensures consistency across the development process.
