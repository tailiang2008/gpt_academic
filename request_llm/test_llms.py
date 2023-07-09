# """
# 对各个llm模型进行单元测试
# """
def validate_path():
    import os, sys
    dir_name = os.path.dirname(__file__)
    root_dir_assume = os.path.abspath(os.path.dirname(__file__) +  '/..')
    os.chdir(root_dir_assume)
    sys.path.append(root_dir_assume)
    
validate_path() # validate path so you can run from base directory
if __name__ == "__main__":
    from request_llm.bridge_chatglmft import predict_no_ui_long_connection
    # from request_llm.bridge_newbingfree import predict_no_ui_long_connection
    # from request_llm.bridge_moss import predict_no_ui_long_connection
    # from request_llm.bridge_jittorllms_pangualpha import predict_no_ui_long_connection
    # from request_llm.bridge_jittorllms_llama import predict_no_ui_long_connection

    llm_kwargs = {
        'max_length': 512,
        'top_p': 1,
        'temperature': 1,
    }

    result = predict_no_ui_long_connection(inputs="你好", 
                                        llm_kwargs=llm_kwargs,
                                        history=[],
                                        sys_prompt="")
    print('final result:', result)

