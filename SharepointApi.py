from os import sysconf
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential


print(100 * '-')
site_url = 'insert'

app_principal = {
'client_id': 'insert',
'client_secret': 'insert',
}
ctx_auth = AuthenticationContext(site_url)
if ctx_auth.acquire_token_for_app(client_id=app_principal['client_id'], client_secret=app_principal['client_secret']):
    ctx = ClientContext(site_url, ctx_auth)
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    print('Authenticated into sharepoint app for: ',web.properties['Title'])
    lists = ctx.web.lists
    ctx.load(lists)
    ctx.execute_query()
    for l in lists:
        print("This is a list object: {0}".format(l.properties['Title']))
    list_object = ctx.web.lists.get_by_title('Documents')
    items = list_object.items
    ctx.load(items)
    ctx.execute_query()
    for l in items:
        print("This is a item object: {0}".format(l.properties['Title']))

else:
    print(ctx_auth.get_last_error())