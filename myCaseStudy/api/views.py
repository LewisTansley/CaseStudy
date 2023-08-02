'''
Define functions in this file that perform calls to the database
return the data so the front end can use it
Use classes.

Research sqlalchemy for constructing databse schema
'''
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getData(request):
    person = {'name':'Dennis', 'age':28}
    return Response(person)