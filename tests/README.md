# USSP Test Suite Implementation

This tool performs automated tests to validate UAS Service Provider (USP) compliance with standards and regulations.

### Setting up your environment

This project is powered by pytest. Running it on your **local machine** requires a working python installation. Once you have that setup:

- Configure environment variables, use [env file template](../example.env).
- Execute setup and run locally:

```
make local-setup && make run-locally
```

The presented tool is a synchronous executable built into the `ussp-validator` **Docker** image.  This image usage requires a docker installation.

- Execute:

```
make run
```

Currently, the test suite execution result will be shown only in docker log.
