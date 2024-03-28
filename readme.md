# Guias Online Backend

## Project Overview

This repository contains the backend for the Guías Scouts project, an integral software for efficient management of educational materials, evaluations, and participant progress. Designed to optimize activities, simplify evaluations, and provide easy and quick access to educational resources, this system aligns with the corporate objectives of Guías Scouts, promoting efficient resource management and enhancing the participant experience in the program.

## Requirements

> Docker

> MinIO client (mc)

## Getting Started

### Prerequisites

Ensure Docker is installed and running on your machine. Additionally, the MinIO client (mc) should be installed for managing files within the project.

### Running the Project

#### On Windows:

To start the development environment:

> make wstart_dev_env

To run the development server:

> make wrun_dev

To tear down the environment:

> make wdestroy_dev_env

### On Linux/macOS:

To start the development environment:

> make start_dev_env

To run the development server:

> make run_dev

To tear down the environment:

> make destroy_dev_env

## Accessing the Swagger Documentation

To view the Swagger API documentation, navigate to:

`localhost:5000/apidocs`

## Building the Docker Database Image

To build the database image with a specific tag:

> make build_db TAG=n.n

## Project Structure

The backend is built with a focus on security, efficiency, and maintainability. It utilizes Docker for containerization, ensuring a consistent and isolated environment for development and production. The MinIO client (mc) is used for file management, adhering to the project's requirements for handling educational materials and user data securely.

## Licenses

This project is will only accept BSD, MIT or Apache Licence packages. Any other type of Copyleft licence is out of the scope and prohibited in this product.

## Acknowledgments

This project was made possible by the dedicated work of the Guías Scouts project team. Special thanks to the Institute of Technology of Costa Rica for supporting this project.

This README provides a comprehensive guide for developers, contributors, and users to understand the project's setup, requirements, and contribution guidelines.
