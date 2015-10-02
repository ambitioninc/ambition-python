Ambition Python Bindings
=============================

Import these bindings in your project to integrate Ambition's public API.

Examples
--------

Listing Usernames for All Accounts
----------------------------------

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

Listing All Data Types
----------------------

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

Uploading File Contents to the API
----------------------------------

.. code-block:: python

    import io

    from ambition.apis import DataApi

    api_client_kwargs = {
        'api_key': environ.get('AMBITION_API_KEY'),
        'subdomain': environ.get('AMBITION_SUBDOMAIN'),
    }
    api = DataApi.create_client(**api_client_kwargs)
    # get data file contents
    csv_file = io.open('/path/to/some.csv')
    body = csv_file.read()
    # make api call
    api.public_api_data_create(data_type, body, content_type='text/csv')
    
