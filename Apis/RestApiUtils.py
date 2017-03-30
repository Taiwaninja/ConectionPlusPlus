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
            request_url += APIConsts.PARAMETER_FORMAT.format(param_name=param_name, param_value=param_value)
        return request_url

    @classmethod
    def rest_api_request(cls, api_root_url, parameters_dict):
        url = cls.build_request_url(api_root_url, parameters_dict)
        return urllib2.urlopen(url).read()


A
