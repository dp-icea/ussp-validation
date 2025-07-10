# USSP Test Suite Implementation

This repository contains BR-UTM's implementation of a validation tool for UAS Service Provider (USP) implementation compliance with standards and regulations and it's functionalities.

## Standards and Regulations

Compliance with the following standards and regulations:

- ``WIP`` [ASTM F3411-22](https://www.astm.org/f3411-22.html): Remote ID;
- ``DONE`` [ASTM F3548-21](https://www.astm.org/f3548-21.html): UAS Traffic Management (UTM), UAS Service Supplier (USS) and Interoperability Specification.

## Test plan documentation

Test cases are documented in the BR-UTM wiki.

- [BR-UTM Wiki](<https://servicos2.decea.mil.br/br-utm/wiki/books/documentacao-tecnica/page/tp-strategic-deconfliction>)

## Development Practices

- [Contributing](./CONTRIBUTING.md)
- [Style Guide](./STYLEGUIDE.md)

## Getting started

Follow these steps to set up and run the tests.

### Environment Variables

This application relies on environment variables for configuration. You'll need to create a .env file in the root directory of this project (if one doesn't already exist) and populate it with the necessary variables. Please use the example.env in the root folder as a template.

### Build and run the docker image

```
make run
```
