Ambition Python Bindings
=============================

Import these bindings in your project to integrate Ambition's public API.

Examples
--------

.. code-block:: python

    from os import environ

    from ambition.apis import AccountApi

    api_client_kwargs = {
        'api_key': environ.get('AMBITION_API_KEY'),
        'subdomain': environ.get('AMBITION_SUBDOMAIN'),
    }
    api = AccountApi.create_client(**api_client_kwargs)
    for account in api.public_api_account_list():
        print account.username

Listing usernames for all accounts in your organization.

.. code-block:: python

    from os import environ

    from ambition.apis import DataApi

    api_client_kwargs = {
        'api_key': environ.get('AMBITION_API_KEY'),
        'subdomain': environ.get('AMBITION_SUBDOMAIN'),
    }
    api = DataApi.create_client(**api_client_kwargs)
    for data_type in api.public_api_data_type_list_list():
        print data_type.name

Listing data type identifier/name for all data types supported by your organization.
