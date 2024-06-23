# coding=utf-8
import re
# from param_dict.param_dict import ParamDict

class SetGlobal():
    def __init__(self,driver):
        self.driver = driver
        # self.gl = ParamDict()

    # 核心代码
    # # 抽取接口的返回值存储到全局变量字典中
    # if set_global_vars and isinstance(set_global_vars, list):
    #  for set_global_var in set_global_vars:
    #      if isinstance(set_global_var, dict):
    #          name = set_global_var.get('name') # name 代表全局变量的名字
    #          query = set_global_var.get('query') # query 代表全局变量的查询语句
    #          value = common.dict_get(response_json, query) # response_json 代表接口的响应数据
    #          self.global_vars[name] = value

    import re

    # 解析字符串中全局变量并进行替换
    def resolve_global_var(pre_resolve_var, global_var_dic, global_var_regex='\${.*?}',
                           match2key_sub_string_start_index=2, match2key_sub_string_end_index=-1):

        '''
        :param pre_resolve_var: 准备进行解析的变量<str>
        :param global_var_dic: 全局变量字典<dict>
        :param global_var_regex: 识别全局变量正则表达式<str>
        :param match2key_sub_string_start_index: 全局变量表达式截取成全局变量字典key值字符串的开始索引<int>
        :param match2key_sub_string_end_index: 全局变量表达式截取成全局变量字典key值字符串的结束索引<int>
        :return: 解析后的变量<str>
        '''

        if not isinstance(pre_resolve_var, str):
            raise TypeError('pre_resolve_var must be str！')

        if not isinstance(global_var_dic, dict):
            raise TypeError('global_var_dic must be dict！')

        if not isinstance(global_var_regex, str):
            raise TypeError('global_var_regex must be str！')

        if not isinstance(match2key_sub_string_start_index, int):
            raise TypeError('match2key_sub_string_start_index must be int！')

        if not isinstance(match2key_sub_string_end_index, int):
            raise TypeError('match2key_sub_string_end_index must be int！')

        re_global_var = re.compile(global_var_regex)

        def global_var_repl(match_obj):
            start_index = match2key_sub_string_start_index
            end_index = match2key_sub_string_end_index
            match_value = global_var_dic.get(match_obj.group()[start_index:end_index])
            return match_value if match_value else match_obj.group()

        resolved_var = re.sub(pattern=re_global_var, string=pre_resolve_var, repl=global_var_repl)
        return resolved_var

if __name__ == '__main__':
    pre_resolve_var = 'left ${status} right, left ${data} right'
    global_var_dic = {'status': 'STATUS', 'data': 'DATA'}
    resolved_str = SetGlobal.resolve_global_var(pre_resolve_var=pre_resolve_var, global_var_dic=global_var_dic)
    print(resolved_str)