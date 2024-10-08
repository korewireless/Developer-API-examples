# coding: utf-8

"""
    ClientsAPI-Production

    The Client Management APIs provide a comprehensive set of endpoints for managing clients within the system. These APIs facilitate operations such as creating, retrieving, updating, and deleting client information.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_ping_status(self, **kwargs):  # noqa: E501
        """get_ping_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ping_status(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_mock_response_id:
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_ping_status_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_ping_status_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_ping_status_with_http_info(self, **kwargs):  # noqa: E501
        """get_ping_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ping_status_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_mock_response_id:
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_mock_response_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ping_status" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_mock_response_id' in params:
            header_params['x-mock-response-id'] = params['x_mock_response_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['LambdaTokenAuthorizer', 'api_key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/ping', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ping_options(self, **kwargs):  # noqa: E501
        """v1_ping_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ping_options(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_mock_response_id:
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ping_options_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_ping_options_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_ping_options_with_http_info(self, **kwargs):  # noqa: E501
        """v1_ping_options  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ping_options_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_mock_response_id:
        :param str authorization:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_mock_response_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_ping_options" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_mock_response_id' in params:
            header_params['x-mock-response-id'] = params['x_mock_response_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/ping', 'OPTIONS',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
