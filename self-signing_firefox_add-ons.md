#Notes for Self-Signing Firefox Add-ons

Add-ons need to be self-signed in order to avoid the warning messages.
This may need to be updated regularly.


## Converting from cfx to jpm

If you already have an install.rdf, but do not have a package.json, follow these commands

1. Install jpm  
   `npm install -g jpm`

jpm is the new manager to replace cfx.

2. Run `jpm init` in directory to create a package.json
3. Run `jpm xpi` to create a new xpi. XPI will look at install.rdf instead of package.json

## Update Versioning

In install.rdf

1. Bump version number up.
2. targetApplication -> description -> minVersion, bump to valid version
3. targetApplication -> description -> maxVersion, bump to highest version

## Signing

1. Create an account on Mozilla Add-on.
	[https://addons.mozilla.org/en-US/firefox/users/register](https://addons.mozilla.org/en-US/firefox/users/register)
2. Go to Manage my API Keys
3. Generate a new set of Credentials
4. Use credentials in the following command 
   `jpm sign --api-key {key} --api-secret {secret}`
5. A new xpi will be generated if it succeeds, or a validation error would be created.

