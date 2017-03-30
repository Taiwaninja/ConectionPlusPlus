#!/usr/bin/python
import APIConsts
import urllib2


class RestApiUtils(object):
    @classmethod
    def build_request_url(cls, api_root_url, parameters_dict):
        """
        Return url for use.
        
        :param api_root_url: Root api urls 
        :param parameters_dict: Dict of "param name" : "param value"
        :return: string url
        """
        if not parameters_dict:
            return api_root_url
        request_url = api_root_url
        first_parameter = True
        for param_name, param_value in parameters_dict.iteritems():
            if first_parameter:
                request_url += APIConsts.PARAMETER_PREFIX
                first_parameter = False
            else:
                request_url += APIConsts.PARAMETER_DELIMITER
            request_url += APIConsts.PARAMETER_FORMAT.format(param_name, param_value)
        return request_url

    @classmethod
    def rest_api_request(cls, api_root_url, parameters_dict):
        url = cls.build_request_url(api_root_url, parameters_dict)
        return urllib2.urlopen(url).read()

    @classmethod
    def parse_response(cls, response, output_format_dict):
        """
        PArses response to given ouptut format
        :param response: 
        :param output_format_dict: output format dict
        Key is wanted output field value
        Value:
            if str = Direct key from response
            if list = Direct keys from response recursive (e.g. dict[a][b])
            if dict = Need to create inner dict, you may use this recursively.
        :return: 
        """
        desired_output = {}
        for key, value in output_format_dict.iteritems():
            value_type = type(value)
            if value_type == str:
                desired_output[key] = response[value]
                continue
            if value_type == list:
                curr_val = response
                response_key_list = value
                for response_key in response_key_list:
                    curr_val = curr_val[response_key]
                desired_output[key] = curr_val
                continue
            if value_type == dict:
                desired_output[key] = cls.parse_response(response, value)
                continue
        return desired_output
