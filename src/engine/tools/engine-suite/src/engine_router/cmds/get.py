import sys
from google.protobuf.json_format import ParseDict
from shared.dumpers import dict_to_str_yml

from api_communication.client import APIClient
import api_communication.proto.router_pb2 as erouter
import api_communication.proto.engine_pb2 as engine


def run(args):

    # Get the params
    api_socket: str = args['api_socket']
    route: str = args['route']

    # Create API client
    client = APIClient(api_socket)

    # Create the request
    request = erouter.RouteGet_Request()
    request.name = route

    # Send the request
    error, response = client.send_recv(request)
    if error:
        sys.exit(f'Error getting route: {error}')

    # Parse the response
    parsed_response = ParseDict(response, erouter.RouteGet_Response())
    if parsed_response.status == engine.ERROR:
        sys.exit(f'Error getting route: {parsed_response.error}')

    # Print the response
    data: str = dict_to_str_yml(response['route'])
    print(data)

    return 0


def configure(subparsers):
    parser = subparsers.add_parser('get', help='Get a route details')
    parser.add_argument('route', type=str, help='Route to get')
    parser.set_defaults(func=run)
